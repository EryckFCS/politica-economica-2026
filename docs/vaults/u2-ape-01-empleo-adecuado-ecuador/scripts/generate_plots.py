import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Configuración de estilo
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Liberation Sans'],
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.titlesize': 14,
    'legend.fontsize': 10
})

# Crear figura con 2 subplots horizontales
fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

# Colores institucionales y sobrios
palette_labor = ['#1f77b4', '#aec7e8', '#ff7f0e', '#d62728'] # azul, azul claro, naranja, rojo
palette_informal = ['#2ca02c', '#d62728'] # verde, rojo

# --- GRAFICO 1: Estructura del Mercado Laboral ---
labels_labor = ['Empleo Adecuado\n(35.9%)', 'Otro Inadecuado\n(39.4%)', 'Subempleo\n(21.0%)', 'Desempleo\n(3.7%)']
sizes_labor = [35.9, 39.4, 21.0, 3.7]
colors_labor = ['#2b5c8f', '#7fa9cf', '#e68a00', '#c73a3a']

bars = axes[0].bar(labels_labor, sizes_labor, color=colors_labor, edgecolor='black', linewidth=0.7, width=0.6)
axes[0].set_title('Estructura del Mercado Laboral Ecuatoriano (2024)\n(% de la Población Económicamente Activa)', pad=15, weight='bold', color='#333333')
axes[0].set_ylabel('Porcentaje (%)', labelpad=10)
axes[0].set_ylim(0, 50)

# Añadir valores sobre las barras
for bar in bars:
    height = bar.get_height()
    axes[0].annotate(f'{height:.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 pt vertical offset
                textcoords="offset points",
                ha='center', va='bottom', weight='bold')

# --- GRAFICO 2: Tasa de Informalidad Urbana vs. Rural ---
categories_inf = ['Área Rural', 'Nivel Nacional', 'Área Urbana']
rates_inf = [75.8, 55.2, 43.6]
colors_inf = ['#bf4343', '#d97e2b', '#2b8f67']

bars_inf = axes[1].barh(categories_inf, rates_inf, color=colors_inf, edgecolor='black', linewidth=0.7, height=0.5)
axes[1].set_title('Tasa de Informalidad Laboral (IV Trimestre 2024)\n(% por Área Geográfica)', pad=15, weight='bold', color='#333333')
axes[1].set_xlabel('Porcentaje (%)', labelpad=10)
axes[1].set_xlim(0, 100)

# Añadir valores sobre las barras horizontales
for bar in bars_inf:
    width = bar.get_width()
    axes[1].annotate(f'{width:.1f}%',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(5, 0),  # 5 pt horizontal offset
                textcoords="offset points",
                ha='left', va='center', weight='bold')

# Ajustes generales
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Asegurar que existe la carpeta assets/
os.makedirs('docs/vaults/u2-ape-01-empleo-adecuado-ecuador/assets', exist_ok=True)

# Guardar imagen en alta resolución
output_path = 'docs/vaults/u2-ape-01-empleo-adecuado-ecuador/assets/diagnostico_laboral.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Gráfico generado exitosamente en: {output_path}")
