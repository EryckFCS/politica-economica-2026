# 📚 Reporte de Auditoría y Sanitización Bibliográfica

Este documento detalla el estado físico y la sanitización de las referencias bibliográficas clave utilizadas en el diagnóstico de políticas de empleo adecuado para el mercado laboral de Ecuador (ENEMDU 2024).

---

## 🟢 Referencias Disponibles Físicamente en el Data Lake (`~/.capital/lake/`)

Estas referencias ya se encuentran descargadas en formato PDF de alta fidelidad, vinculadas en el archivo maestro de referencias del nodo (`docs/writing/references.bib`) y listas para indexación semántica (RAG):

### 1. Cuadrado Roura (2014) — Política Económica
*   **Clave BibTeX:** `cuadrado2014politica`
*   **Ubicación en Lake:** `~/.capital/lake/bibliography/raw/cuadrado-roura-economic-policy-2014.pdf`
*   **Estado:** ✅ **DISPONIBLE** (Symlink activo en `bibliography/raw/`)
*   **Referencia APA 7:**
    > Cuadrado Roura, J. R., Mancha Navarro, T., Villena Peña, J. E., Casares Ripol, J., González Moreno, M., Marín Quemada, J. M., & Peinado Gracia, M. L. (2014). *Política económica. Elaboración, objetivos e instrumentos* (5.ª ed.). McGraw-Hill Education.

### 2. Weller (2006) — Los jóvenes y el empleo en América Latina
*   **Clave BibTeX:** `weller2006`
*   **Ubicación en Lake:** `~/.capital/lake/bibliography/raw/weller2006_los_jovenes_y_el_empleo_en_america_latina.pdf`
*   **Estado:** ✅ **DISPONIBLE** (Descargado y verificado en el Lake exitosamente)
*   **Referencia APA 7:**
    > Weller, J. (Ed.). (2006). *Los jóvenes y el empleo en América Latina: desafíos y perspectivas ante el nuevo escenario laboral*. CEPAL, Mayol Ediciones.

### 3. CEPAL (2024) — Panorama Social de América Latina y el Caribe 2024
*   **Clave BibTeX:** `cepal2024`
*   **Ubicación en Lake:** `~/.capital/lake/bibliography/raw/cepal2024_panorama_social_de_america_latina_y_el_caribe.pdf`
*   **Estado:** ✅ **DISPONIBLE** (Descargado y verificado en el Lake exitosamente)
*   **Referencia APA 7:**
    > Comisión Económica para América Latina y el Caribe (CEPAL). (2024). *Panorama Social de América Latina y el Caribe, 2024: desafíos de la protección social no contributiva para avanzar hacia el desarrollo social inclusivo*. Naciones Unidas.

### 4. INEC (2025a) — Boletín Técnico de Empleo, Diciembre 2024
*   **Clave BibTeX:** `inec2025a`
*   **Ubicación en Lake:** `~/.capital/lake/bibliography/raw/inec2024boletin_bolet_n_t_cnico_de_empleo_diciembre_2024.pdf`
*   **Estado:** ✅ **DISPONIBLE**
*   **Referencia APA 7:**
    > Instituto Nacional de Estadística y Censos (INEC). (2025). *Boletín Técnico de Empleo, Diciembre 2024*. INEC.

### 5. INEC (2025b) — ENEMDU IV Trimestre 2024
*   **Clave BibTeX:** `inec2025b`
*   **Ubicación en Lake:** `~/.capital/lake/bibliography/raw/inec2025boletin_bolet_n_t_cnico_n_03_2025_enemdu_iv_trimestre_2024.pdf`
*   **Estado:** ✅ **DISPONIBLE**
*   **Referencia APA 7:**
    > Instituto Nacional de Estadística y Censos (INEC). (2025). *Encuesta Nacional de Empleo, Desempleo y Subempleo (ENEMDU), IV Trimestre 2024*. INEC.

---

## ⚠️ Referencias Faltantes (Para Descarga Manual / Búsqueda local)

Las siguientes referencias **no se pudieron descargar automáticamente** debido a restricciones de seguridad de sus servidores (Cloudflare Challenge 403) o redireccionamientos dinámicos obsoletos (404 en el gestor de decretos de Colombia).

Puedes descargarlos manualmente y colocarlos en la carpeta de descargas o en la raíz del proyecto para que sean indexados en el Data Lake:

### 1. Alaimo et al. (2015) — Empleos para crecer (BID)
*   **Clave BibTeX:** `alaimo2015`
*   **Nombre de archivo esperado en Lake:** `alaimo2015_empleos_para_crecer.pdf`
*   **Problema de descarga:** Cloudflare 403 Forbidden.
*   **Enlace de descarga oficial:** [https://publications.iadb.org/es/empleos-para-crecer](https://publications.iadb.org/es/empleos-para-crecer) (Haz clic en "Descargar" resolviendo el Captcha si se te solicita).
*   **Referencia APA 7:**
    > Alaimo, V., Bosch, M., Kaplan, D. S., Pagés, C., & Ripani, L. (2015). *Empleos para crecer: Cómo aumentar la productividad y fomentar la formalidad en América Latina*. Banco Interamericano de Desarrollo.

### 2. Congreso de Colombia (2010) — Ley 1429 (Ley de Formalización y Generación de Empleo)
*   **Clave BibTeX:** `colombia2010`
*   **Nombre de archivo esperado en Lake:** `colombia2010_ley_1429_formalizacion_y_generacion_de_empleo.pdf`
*   **Problema de descarga:** 404 en Función Pública.
*   **Enlace de descarga alternativo:** [http://hdl.handle.net/11520/13640](http://hdl.handle.net/11520/13640) (Cámara de Comercio de Bogotá) o directamente en la Secretaría del Senado de Colombia [http://www.secretariasenado.gov.co/senado/basedoc/ley_1429_2010.html](http://www.secretariasenado.gov.co/senado/basedoc/ley_1429_2010.html).
*   **Referencia APA 7:**
    > Congreso de la República de Colombia. (2010). *Ley 1429 de 2010: Por la cual se expide la Ley de Formalización y Generación de Empleo*. Diario Oficial No. 47.937.

### 3. J-PAL (s.f.) — Vocational training for disadvantaged youth in Colombia
*   **Clave BibTeX:** `jpal_s_f`
*   **Nombre de archivo esperado en Lake:** `jpal_colombia_vocational_training.pdf`
*   **Estado:** ⚠️ Pendiente de descarga.
*   **Enlace de descarga sugerido:** Busca en el portal oficial de J-PAL [https://www.povertyactionlab.org/es/policy-insight/subsidios-la-capacitacion-laboral-para-jovenes-vulnerables](https://www.povertyactionlab.org/es/policy-insight/subsidios-la-capacitacion-laboral-para-jovenes-vulnerables) y descarga el resumen de evaluación o Teaching Case en PDF.
*   **Referencia APA 7:**
    > Abdul Latif Jameel Poverty Action Lab (J-PAL). (2018). *Subsidizing Vocational Training for Disadvantaged Youth in Colombia*. J-PAL Policy Insights.

### 4. SENCE (s.f.) — Subsidio al Empleo Joven (Chile)
*   **Clave BibTeX:** `sence_s_f`
*   **Nombre de archivo esperado en Lake:** `sence_subsidio_empleo_joven_chile.pdf`
*   **Estado:** ⚠️ Pendiente de descarga.
*   **Enlace de descarga sugerido:** Disponible en la biblioteca digital de DIPRES Chile [https://www.dipres.gob.cl/598/w3-propertyvalue-15822.html](https://www.dipres.gob.cl/598/w3-propertyvalue-15822.html) o la web oficial del SENCE.
*   **Referencia APA 7:**
    > Servicio Nacional de Capacitación y Empleo (SENCE). (2016). *Evaluación de Impacto del Subsidio al Empleo Joven*. Ministerio del Trabajo y Previsión Social de Chile.

---

## 🛠️ Entrada Completa del Archivo BibTeX del Nodo (`references.bib`)

Puedes ver y copiar las entradas exactas que hemos añadido y sanitizado en el archivo maestro de referencias del nodo para su correcta compilación en LaTeX/Quarto:

```bibtex
@book{cepal2024,
  title={Panorama Social de Am{\'e}rica Latina y el Caribe, 2024: desaf{\'i}os de la protecci{\'o}n social no contributiva para avanzar hacia el desarrollo social inclusivo},
  author={{Comisi{\'o}n Econ{\'o}mica para Am{\'e}rica Latina y el Caribe (CEPAL)}},
  year={2024},
  publisher={Naciones Unidas},
  address={Santiago de Chile},
  file={/home/erick-fcs/.capital/lake/bibliography/raw/cepal2024_panorama_social_de_america_latina_y_el_caribe.pdf}
}

@book{weller2006,
  title={Los j{\'o}venes y el empleo en Am{\'e}rica Latina: desaf{\'i}os y perspectivas ante el nuevo escenario laboral},
  author={Weller, J{\"u}rgen},
  year={2006},
  publisher={CEPAL, Mayol Ediciones},
  address={Santiago de Chile},
  file={/home/erick-fcs/.capital/lake/bibliography/raw/weller2006_los_jovenes_y_el_empleo_en_america_latina.pdf}
}

@book{alaimo2015,
  title={Empleos para crecer: C{\'o}mo aumentar la productividad y fomentar la formalidad en Am{\'e}rica Latina},
  author={Alaimo, Ver{\'o}nica and Bosch, Mariano and Kaplan, David S. and Pag{\'e}s, Carmen and Ripani, Laura},
  year={2015},
  publisher={Banco Interamericano de Desarrollo},
  address={Washington, D.C.},
  file={/home/erick-fcs/.capital/lake/bibliography/raw/alaimo2015_empleos_para_crecer.pdf}
}

@misc{colombia2010,
  title={Ley 1429 de 2010: Por la cual se expide la Ley de Formalizaci{\'o}n y Generaci{\'o}n de Empleo},
  author={{Congreso de la Rep{\'u}blica de Colombia}},
  year={2010},
  note={Diario Oficial No. 47.937},
  file={/home/erick-fcs/.capital/lake/bibliography/raw/colombia2010_ley_1429_formalizacion_y_generacion_de_empleo.pdf}
}

@techreport{jpal_s_f,
  title={Subsidizing Vocational Training for Disadvantaged Youth in Colombia},
  author={{Abdul Latif Jameel Poverty Action Lab (J-PAL)}},
  institution={J-PAL Policy Insights},
  year={2018},
  file={/home/erick-fcs/.capital/lake/bibliography/raw/jpal_colombia_vocational_training.pdf}
}

@techreport{sence_s_f,
  title={Evaluaci{\'o}n de Impacto del Subsidio al Empleo Joven},
  author={{Servicio Nacional de Capacitaci{\'o}n y Empleo (SENCE)}},
  institution={Ministerio del Trabajo y Previsi{\'o}n Social},
  year={2016},
  address={Santiago de Chile},
  file={/home/erick-fcs/.capital/lake/bibliography/raw/sence_subsidio_empleo_joven_chile.pdf}
}
```
