import os
import pandas as pd
import numpy as np
import duckdb
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración del estilo visual de los gráficos
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 11,
    'ytick.labelsize': 11,
    'figure.titlesize': 16,
    'font.family': 'sans-serif'
})

# Umbrales del Salario Básico Unificado (SBU) por año en Ecuador (2021-2025)
SBU_DICT = {
    2021: 400.0,
    2022: 425.0,
    2023: 450.0,
    2024: 460.0,
    2025: 475.0
}

DATASET_PATHS = {
    2021: "/home/erick-fcs/.capital/lake/inec/enemdu_2021/personas_2021.parquet",
    2022: "/home/erick-fcs/.capital/lake/inec/enemdu_2022/personas_2022.parquet",
    2023: "/home/erick-fcs/.capital/lake/inec/enemdu_2023/personas_2023.parquet",
    2024: "/home/erick-fcs/.capital/lake/inec/enemdu_2024/personas_2024.parquet",
    2025: "/home/erick-fcs/.capital/lake/inec/enemdu_2025/personas_2025.parquet"
}

def weighted_gini(y, w):
    """Calcula el Coeficiente de Gini ponderado por el factor de expansión."""
    valid = (y >= 0) & (w > 0) & (~np.isnan(y)) & (~np.isnan(w))
    y = y[valid]
    w = w[valid]
    
    if len(y) == 0:
        return np.nan
        
    idx = np.argsort(y)
    y = y[idx]
    w = w[idx]
    
    cum_w = np.cumsum(w)
    cum_wy = np.cumsum(w * y)
    
    p = cum_w / cum_w[-1]
    q = cum_wy / cum_wy[-1]
    
    p = np.insert(p, 0, 0.0)
    q = np.insert(q, 0, 0.0)
    
    gini = 1.0 - np.sum(np.diff(p) * (q[1:] + q[:-1]))
    return float(gini)

def process_year(year, path):
    print(f"--- Procesando ENEMDU {year} ---")
    sbu = SBU_DICT[year]
    
    query = f"""
    SELECT 
        {year} as anio,
        fexp,
        p02 as sexo,
        p03 as edad,
        condact,
        secemp,
        ingrl,
        ingpc
    FROM read_parquet('{path}')
    WHERE p03 >= 15
    """
    df = duckdb.query(query).to_df()
    
    df['fexp'] = pd.to_numeric(df['fexp'], errors='coerce').fillna(0)
    df['condact'] = pd.to_numeric(df['condact'], errors='coerce')
    df['secemp'] = pd.to_numeric(df['secemp'], errors='coerce')
    df['ingrl'] = pd.to_numeric(df['ingrl'], errors='coerce')
    df['ingpc'] = pd.to_numeric(df['ingpc'], errors='coerce')
    
    # --- Cálculos del Mercado Laboral (PEA) ---
    pea_filter = (df['condact'] >= 1) & (df['condact'] <= 8)
    df_pea = df[pea_filter]
    pea_weight_sum = df_pea['fexp'].sum()
    
    # Tasa de Desempleo (condact = 7, 8)
    desempleados = df_pea[df_pea['condact'].isin([7, 8])]['fexp'].sum()
    tasa_desempleo = (desempleados / pea_weight_sum) * 100 if pea_weight_sum > 0 else 0
    
    # Tasa de Subempleo (condact = 2, 3)
    subempleados = df_pea[df_pea['condact'].isin([2, 3])]['fexp'].sum()
    tasa_subempleo = (subempleados / pea_weight_sum) * 100 if pea_weight_sum > 0 else 0
    
    # Tasa de Empleo Adecuado (condact = 1)
    adecuados = df_pea[df_pea['condact'] == 1]['fexp'].sum()
    tasa_adecuado = (adecuados / pea_weight_sum) * 100 if pea_weight_sum > 0 else 0
    
    # Tasa de Informalidad: secemp = 2 sobre total ocupados (condact in [1..6])
    ocupados_filter = (df['condact'] >= 1) & (df['condact'] <= 6)
    df_ocupados = df[ocupados_filter]
    ocupados_weight_sum = df_ocupados['fexp'].sum()
    informales = df_ocupados[df_ocupados['secemp'] == 2]['fexp'].sum()
    tasa_informalidad = (informales / ocupados_weight_sum) * 100 if ocupados_weight_sum > 0 else 0
    
    # --- Cálculos de Desigualdad y Salarios (Ocupados con ingresos válidos) ---
    df_ingrl_valid = df_ocupados[(df_ocupados['ingrl'] >= 0) & (~df_ocupados['ingrl'].isna())]
    gini_laboral = weighted_gini(df_ingrl_valid['ingrl'].values, df_ingrl_valid['fexp'].values)
    
    df_ingpc_valid = df[(df['ingpc'] >= 0) & (~df['ingpc'].isna())]
    gini_percapita = weighted_gini(df_ingpc_valid['ingpc'].values, df_ingpc_valid['fexp'].values)
    
    df_ingrl_pos = df_ocupados[df_ocupados['ingrl'] > 0]
    total_pos_weight = df_ingrl_pos['fexp'].sum()
    
    if total_pos_weight > 0:
        bajo_sbu = df_ingrl_pos[df_ingrl_pos['ingrl'] < sbu]['fexp'].sum()
        exacto_sbu = df_ingrl_pos[(df_ingrl_pos['ingrl'] >= sbu * 0.99) & (df_ingrl_pos['ingrl'] <= sbu * 1.01)]['fexp'].sum()
        alto_sbu = df_ingrl_pos[df_ingrl_pos['ingrl'] > sbu * 1.01]['fexp'].sum()
        
        pct_bajo_sbu = (bajo_sbu / total_pos_weight) * 100
        pct_exacto_sbu = (exacto_sbu / total_pos_weight) * 100
        pct_alto_sbu = (alto_sbu / total_pos_weight) * 100
    else:
        pct_bajo_sbu = pct_exacto_sbu = pct_alto_sbu = 0
        
    metrics = {
        "anio": int(year),
        "sbu": float(sbu),
        "tasa_desempleo": float(tasa_desempleo),
        "tasa_subempleo": float(tasa_subempleo),
        "tasa_adecuado": float(tasa_adecuado),
        "tasa_informalidad": float(tasa_informalidad),
        "gini_laboral": float(gini_laboral),
        "gini_percapita": float(gini_percapita),
        "pct_bajo_sbu": float(pct_bajo_sbu),
        "pct_exacto_sbu": float(pct_exacto_sbu),
        "pct_alto_sbu": float(pct_alto_sbu)
    }
    
    return metrics, df

def generate_plots(df_agg):
    assets_dir = "docs/vaults/u2-acd-02-analisis-politica/assets"
    os.makedirs(assets_dir, exist_ok=True)
    
    # Gráfico 1: Evolución del Empleo Adecuado, Informalidad y Subempleo
    plt.figure(figsize=(10, 6))
    plt.plot(df_agg['anio'], df_agg['tasa_adecuado'], marker='o', linewidth=2.5, label='Empleo Adecuado (%)', color='#2b5c8f')
    plt.plot(df_agg['anio'], df_agg['tasa_informalidad'], marker='s', linewidth=2.5, label='Informalidad (%)', color='#d95f02')
    plt.plot(df_agg['anio'], df_agg['tasa_subempleo'], marker='^', linewidth=2.5, label='Subempleo (%)', color='#7570b3')
    
    plt.title('Evolución de las Tasas de Empleo e Informalidad en Ecuador (2021-2025)')
    plt.xlabel('Año')
    plt.ylabel('Porcentaje (%)')
    plt.xticks(df_agg['anio'].astype(int))
    plt.legend(loc='best')
    plt.tight_layout()
    plot1_path = os.path.join(assets_dir, "employment_trends.png")
    plt.savefig(plot1_path, dpi=300)
    plt.close()
    print(f"Gráfico 1 guardado en: {plot1_path}")
    
    # Gráfico 2: SBU vs Porcentaje de trabajadores que ganan menos del SBU
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    color = '#1f77b4'
    ax1.set_xlabel('Año')
    ax1.set_ylabel('Salario Básico Unificado (USD)', color=color)
    ax1.plot(df_agg['anio'], df_agg['sbu'], marker='o', linewidth=2.5, color=color, label='SBU (USD)')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_xticks(df_agg['anio'].astype(int))
    
    ax2 = ax1.twinx()
    color = '#d62728'
    ax2.set_ylabel('Porcentaje de Ocupados < SBU (%)', color=color)
    ax2.plot(df_agg['anio'], df_agg['pct_bajo_sbu'], marker='x', linewidth=2.5, linestyle='--', color=color, label='Ocupados < SBU (%)')
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.title('Salario Básico Unificado vs. Incumplimiento del Piso Salarial (2021-2025)')
    fig.tight_layout()
    plot2_path = os.path.join(assets_dir, "sbu_inequality.png")
    plt.savefig(plot2_path, dpi=300)
    plt.close()
    print(f"Gráfico 2 guardado en: {plot2_path}")

def main():
    aggregated_results = []
    sample_dfs = []
    
    for year, path in DATASET_PATHS.items():
        if os.path.exists(path):
            metrics, df_year = process_year(year, path)
            aggregated_results.append(metrics)
            
            sample_size = min(len(df_year), 4000)
            df_sample = df_year.sample(n=sample_size, random_state=42).copy()
            sample_dfs.append(df_sample)
        else:
            print(f"Archivo no encontrado para el año {year}: {path}")
            
    df_agg = pd.DataFrame(aggregated_results)
    os.makedirs("data", exist_ok=True)
    agg_csv_path = "data/processed_employment_inequality.csv"
    df_agg.to_csv(agg_csv_path, index=False)
    print(f"\nSeries agregadas guardadas en {agg_csv_path}")
    print(df_agg.to_string())
    
    # Generar los gráficos estadísticos
    generate_plots(df_agg)
    
    # Combinar muestras y exportar
    df_sample_all = pd.concat(sample_dfs, ignore_index=True)
    df_sample_all['sexo'] = df_sample_all['sexo'].fillna(-1).astype(int)
    df_sample_all['edad'] = df_sample_all['edad'].fillna(-1).astype(int)
    df_sample_all['condact'] = df_sample_all['condact'].fillna(-1).astype(int)
    df_sample_all['secemp'] = df_sample_all['secemp'].fillna(-1).astype(int)
    
    sample_csv_path = "data/enemdu_sample_2019_2025.csv"
    sample_dta_path = "data/enemdu_sample_2019_2025.dta"
    
    df_sample_all.to_csv(sample_csv_path, index=False)
    df_sample_all.to_stata(sample_dta_path, write_index=False, version=117)
    print(f"Muestra de microdatos (N={len(df_sample_all)}) guardada en:")
    print(f" - CSV: {sample_csv_path}")
    print(f" - DTA (Stata): {sample_dta_path}")

if __name__ == "__main__":
    main()
