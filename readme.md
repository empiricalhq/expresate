## ODS 11

[Datos abiertos del sector ambiente](https://sinia.minam.gob.pe/portal/datos-abiertos/):

| Dataset                                                                                                                                                                                                              	| Descripción                                                                                                                                                               	|
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| [Valorización de residuos sólidos Inorgánicos a nivel distrital](https://datosabiertos.gob.pe/dataset/valorizaci%C3%B3n-de-residuos-s%C3%B3lidos-nivel-distrital-ministerio-del-ambiente-minam)                      	| Información sobre el reaprovechamiento y valorización de residuos inorgánicos (plásticos, metales, vidrio, papel, etc.) gestionados por los municipios a nivel distrital. 	|
| [Valorización de residuos sólidos Orgánicos a nivel distrital](https://datosabiertos.gob.pe/dataset/valorizaci%C3%B3n-de-residuos-s%C3%B3lidos-nivel-distrital-ministerio-del-ambiente-minam)                        	| Datos sobre el reaprovechamiento y valorización de residuos orgánicos (restos de alimentos, residuos vegetales) gestionados a nivel distrital.                            	|
| [Composición de residuos sólidos domiciliarios](https://datosabiertos.gob.pe/dataset/composici%C3%B3n-de-residuos-s%C3%B3lidos-domiciliarios)                                                                        	| Proporción de diferentes tipos de residuos generados en los hogares (orgánicos, plásticos, metales, vidrio, papel, entre otros).                                          	|
| [Disposición final adecuada de residuos sólidos](https://datosabiertos.gob.pe/dataset/disposici%C3%B3n-final-adecuada-de-residuos-s%C3%B3lidos-ministerio-del-ambiente-minam)                                        	| Registra la cantidad de residuos que son llevados a infraestructuras autorizadas (rellenos sanitarios, celdas de seguridad, entre otros).                                 	|
| [Generación anual de residuos sólidos domiciliarios y municipales](https://datosabiertos.gob.pe/dataset/generaci%C3%B3n-anual-de-residuos-s%C3%B3lidos-domiciliarios-y-municipales-ministerio-del-ambiente)          	| Estadísticas anuales de generación de residuos en hogares y a nivel municipal.                                                                                            	|
| [Residuos municipales generados anualmente](https://datosabiertos.gob.pe/dataset/residuos-municipales-generados-anualmente)                                                                                          	| Cantidad de residuos generados por los municipios del país, con variación por año.                                                                                        	|
| [Implementación del Programa Municipal EDUCCA](https://www.datosabiertos.gob.pe/dataset/implementaci%C3%B3n-del-programa-municipal-de-educaci%C3%B3n-cultura-y-ciudadan%C3%ADa-ambiental-programa)                   	| Información sobre la ejecución a nivel distrital del Programa EDUCCA, orientado a educación y cultura ambiental en la ciudadanía.                                         	|
| [Disposición final adecuada de residuos sólidos (duplicado)](https://www.datosabiertos.gob.pe/dataset/disposici%C3%B3n-final-adecuada-de-residuos-s%C3%B3lidos-ministerio-del-ambiente-minam)                        	| Mismo dataset que el anterior sobre disposición final adecuada de residuos, listado dos veces en el portal.                                                               	|
| [Generación de residuos sólidos municipales](https://www.datosabiertos.gob.pe/dataset/generaci%C3%B3n-anual-de-residuos-s%C3%B3lidos-domiciliarios-y-municipales-ministerio-del-ambiente)                            	| Estadísticas de generación de residuos sólidos municipales; similar al dataset de domiciliarios y municipales, pero enfocado en lo municipal.                             	|
| [Inventario Nacional de Áreas Degradadas por residuos sólidos municipales](https://www.datosabiertos.gob.pe/dataset/inventario-nacional-de-%C3%A1reas-degradadas-por-residuos-s%C3%B3lidos-municipales-organismo-de) 	| Registro de sitios degradados por acumulación o disposición inadecuada de residuos sólidos municipales en el país.                                                        	|

# Roadmap de Dashboard para Gestión de Residuos Sólidos (Perú)

Este dashboard busca mostrar la historia completa de los residuos: 
desde la **generación**, pasando por la **valorización**, la **disposición final**, 
la **composición**, los **programas ambientales** y finalmente los **impactos**.

---

## 1. Generación de residuos
**Datasets:**
- Generación anual de residuos sólidos domiciliarios y municipales
- Residuos municipales generados anualmente
- Generación de residuos sólidos municipales

**Gráficos sugeridos:**
- Serie de tiempo (línea): evolución de toneladas de residuos generados (2000–2024).
- Mapa temático: intensidad de generación por distrito/provincia.
- Ranking (barras): Top 10 municipios que más generan.
- Indicador: kg de residuos per cápita por año.

---

## 2. Valorización de residuos
**Datasets:**
- Valorización de residuos sólidos Inorgánicos a nivel distrital
- Valorización de residuos sólidos Orgánicos a nivel distrital

**Gráficos sugeridos:**
- Barras agrupadas: comparación de valorización orgánica vs inorgánica por distrito.
- Serie temporal: evolución de valorización en toneladas por año.
- Indicador circular (%): proporción de residuos valorizados frente al total generado.
- Mapa: municipios con mayores tasas de valorización.

---

## 3. Disposición final de residuos
**Dataset:**
- Disposición final adecuada de residuos sólidos

**Gráficos sugeridos:**
- Serie de tiempo: % de residuos dispuestos adecuadamente vs total generado.
- Mapa: ubicación de rellenos sanitarios y distritos que atienden.
- Indicador KPI: cobertura nacional (ej. 65% residuos con disposición adecuada).
- Comparación regional: barras apiladas mostrando disposición adecuada vs inadecuada.

---

## 4. Caracterización de residuos
**Dataset:**
- Composición de residuos sólidos domiciliarios

**Gráficos sugeridos:**
- Gráfico circular: % de orgánicos, plásticos, vidrio, papel, metales, otros.
- Evolución temporal: cambios en la proporción de plásticos u orgánicos en 10 años.
- Comparación entre regiones: barras horizontales por tipo de residuo.

---

## 5. Programas y gestión ambiental
**Dataset:**
- Implementación del Programa Municipal EDUCCA

**Gráficos sugeridos:**
- Mapa de cobertura: distritos con y sin EDUCCA.
- Indicador: % de municipios implementando el programa.
- Cruce de datos: comparar valorización promedio de municipios con EDUCCA vs sin EDUCCA.
- Línea temporal: crecimiento del programa en los últimos años.

---

## 6. Impactos ambientales
**Dataset:**
- Inventario Nacional de Áreas Degradadas por residuos sólidos municipales

**Gráficos sugeridos:**
- Mapa: localización de áreas degradadas.
- Serie temporal: evolución de áreas degradadas detectadas por año.
- Comparación con generación: scatter plot (eje X: toneladas generadas, eje Y: áreas degradadas).
- Indicador: número total de hectáreas degradadas registradas.

---

## Flujo narrativo del dashboard
1. **Generación** → mostrar cuánto y dónde se produce.
2. **Valorización** → mostrar cuánto se reaprovecha.
3. **Disposición** → mostrar cuánto se maneja correctamente.
4. **Composición** → mostrar de qué están hechos los residuos.
5. **Programas EDUCCA** → mostrar esfuerzos de gestión y educación ambiental.
6. **Impactos** → mostrar consecuencias de la mala gestión.

## ODS 16

The project will explore **the alignment between citizen security needs and
police resource distribution in Peru**, with a focus on Lambayeque. The idea is
to connect crime data, perceptions of insecurity, and the allocation of police
personnel to evaluate whether resources are being deployed where they are most
needed.

Datasets we can use:

- [Victimización, percepción de inseguridad y confianza en la PNP](https://datosabiertos.gob.pe/dataset/victimizaci%C3%B3n-percepci%C3%B3n-de-inseguridad-y-confianza-en-la-pnp)
  – citizen perception of insecurity and trust in the police.
- [Delitos denunciados ante el Ministerio Público de Lambayeque 2019–2023](https://datosabiertos.gob.pe/dataset/delitos-denunciados-ante-el-ministerio-publico-de-lambayeque-2019-2023)
  – reported crimes in Lambayeque.
- [Denuncias policiales – Enero 2018 a Junio 2025](https://datosabiertos.gob.pe/dataset/denuncias-policiales/resource/64c01d53-4402-4e5a-936a-4bce5b3d1008)
  – national-level police reports.
- [Personal policial](https://datosabiertos.gob.pe/dataset/personal-policial) –
  staffing and distribution of police personnel.
- [Producción policial](https://www.datosabiertos.gob.pe/dataset/producci%C3%B3n-policial)

Additional datasets:
- [Violencia Contra la Mujer](https://datosabiertos.gob.pe/dataset/violencia-contra-la-mujer)
- [Personas desaparecidas](https://datosabiertos.gob.pe/dataset/personas-desaparecidas)
- [Trata de Personas](https://datosabiertos.gob.pe/dataset/trata-de-personas)
- [Registros delictivos del Observatorio Regional de Seguridad Ciudadana en la Provincia Constitucional del Callao GORECALLAO](https://www.datosabiertos.gob.pe/dataset/registros-delictivos-del-observatorio-regional-de-seguridad-ciudadana-en-la-provincia)

**What approach we could take**:

1. Compare perceptions of insecurity with actual reported crimes (Lambayeque as
   a case study).
2. Analyze whether police personnel distribution corresponds to crime incidence
   and perception hotspots.
3. Highlight mismatches that may reduce institutional trust and propose
   evidence-based reallocation strategies.

## ODS 8

1. [Precios de Cotización BVL](https://www.datosabiertos.gob.pe/dataset/informaci%C3%B3n-de-precios-de-cotizaci%C3%B3n-de-valores-seg%C3%BAn-fecha-de-cotizaci%C3%B3n-en-la-bvl)
   - Período: 2008 – presente
   - Contenido: Precio máximo, mínimo, monto diario
   - Columnas:
     - FechaCotizacion (fecha de la operación en BVL)
     - Valor (ticker o código del valor)
     - Descripcion (nombre de la empresa/activo)
     - FechaAnterior (última fecha de negociación previa)
     - Cierre_Anterior (precio de cierre anterior)
     - Cierre_Actual (precio de cierre actual)
     - Apertura_Actual (precio de apertura del día)
     - Maxima_Actual (precio máximo alcanzado en el día)
     - Minima_Actual (precio mínimo alcanzado en el día)
     - Promedio_Actual (precio promedio negociado)
     - Monto_Negociado (volumen monetario negociado)
     - FechaRegistro (fecha y hora de registro en el sistema)

2. [Índices de Renta Variable BVL](https://www.datosabiertos.gob.pe/dataset/informaci%C3%B3n-de-%C3%ADndices-del-mercado-de-renta-variable-en-el-per%C3%BA-seg%C3%BAn-fecha-del-%C3%ADndice-en-la)
   - Período: 1996 – presente
   - Contenido: Datos diarios de índices de renta variable (lun–vie), agrupados
     por sectores, subsectores y mercado. La composición de los índices puede
     cambiar en el tiempo. Unas 10 entradas tiene el json.
   - Columnas:
     - Fecha (fecha del índice)
     - Clase (categoría, ej. “De Sector”)
     - Tipo (código del índice, ej. SPBLCPT)
     - Indice (nombre del índice, ej. S\&P/BVL Consumer)
     - ClaseIndice (tipo adicional, puede ser nulo)
     - anterior (valor del índice en la jornada previa)
     - ultimo (valor final del índice en la fecha)
     - variacion (% de variación diaria)
     - apertura (valor de apertura del índice)
     - maxima (valor máximo alcanzado en la jornada)
     - minima (valor mínimo alcanzado en la jornada)

3. [Empresas Inscritas SMV](https://www.datosabiertos.gob.pe/dataset/informaci%C3%B3n-de-valores-representativos-de-participaci%C3%B3n-patrimonial-inscritos-en-el-registro)
   - Período: 2000 – presente
   - Contenido: Por razón social/RUC, \~50 registros para el caso particular del
     BCP
   - Contenido: Información sobre los valores representativos de participación
     patrimonial inscritos en el **Registro Público del Mercado de Valores
     (RPMV)**, emitidos por sociedades emisoras.
     - Columnas:
       - Variable (nombre del campo / indicador del registro)
       - Emisor (razón social o entidad emisora)
       - Tipo Valor (categoría del valor emitido, ej. acción común, preferente,
         etc.)
       - Serie o clase (identificador de la emisión o subdivisión del valor)
       - Tipo Resolución (tipo de acto administrativo que aprueba la
         inscripción)
       - Nro. Resolución (número de la resolución que autoriza la inscripción)
       - Fecha Inscripción (fecha en la que el valor quedó inscrito en el RPMV)
       - Sección RPMV (sección del registro en la que está inscrito el valor)

4. [Estado de Cambios en Patrimonio](https://www.datosabiertos.gob.pe/dataset/estado-de-cambios-en-el-patrimonio-informaci%C3%B3n-financiera-de-empresas-supervisadas-por-la)
   - Período: 2000 – presente
   - Contenido: Información financiera trimestral sobre los **cambios en el
     patrimonio** de las empresas supervisadas por la SMV. Permite analizar
     crecimiento patrimonial y estructura de capital. Se consulta por **RPJ**
     (identificador único de cada empresa registrada en la SMV).
   - Columnas:
     - RPJ (código de empresa en el registro de la SMV)
     - Ejercicio (año del reporte)
     - TipoInformacion (tipo de presentación: Trimestral Individual,
       Consolidado, etc.)
     - Trimestre (ej. "1er Trimestre")
     - Cuenta (código de cuenta contable, ej. 4F0101)
     - DescripcionCuenta (nombre de la cuenta contable, ej. “Capital Social”)
     - OrdenColumna (posición de la columna en el estado financiero)
     - DescripcionColumna (nombre de la partida patrimonial, ej. “Capital
       Social”, “Capital Adicional”)
     - Monto1 (valor numérico reportado para la cuenta)
     - FechaRegistro (fecha en que se ingresó la información en el sistema)

5. [Estado de Flujo de Efectivo](https://www.datosabiertos.gob.pe/dataset/estado-de-flujo-de-efectivo-informaci%C3%B3n-financiera-de-empresas-supervisadas-por-la-smv)
   - Período: 1999 – presente
   - Contenido: Información financiera trimestral de los **flujos de efectivo**
     de empresas supervisadas por la SMV. El dataset contiene registros de
     múltiples compañías en cada periodo, cada una con diferentes cuentas de
     flujo de caja.
   - Columnas:
     - RPJ (código de la empresa en la SMV)
     - TipoEmpresa (categoría de la empresa, ej. bancos, fondos de inversión,
       etc.)
     - TipoSector (sector económico, a veces vacío)
     - NombreEmpresa (razón social completa)
     - RUC (número de RUC de la empresa)
     - CIIU (código de actividad económica, a veces vacío)
     - Ejercicio (año del reporte)
     - TipoInformacion (ej. Trimestral Individual, Consolidado)
     - Trimestre (ej. "1er Trimestre")
     - Moneda (ej. Soles, Dólares)
     - MetodoFlujoEfectivo (Directo o Indirecto)
     - Cuenta (código contable del flujo de efectivo, ej. 3D0101)
     - DescripcionCuenta (nombre de la cuenta, ej. “Venta de Bienes y Prestación
       de Servicios”)
     - Monto1 (importe en la primera columna de reporte)
     - Monto2 (importe en la segunda columna de reporte, usualmente comparativo)
     - FechaRegistro (fecha de ingreso en el sistema)

6. [Estado de Resultado Integral](https://www.datosabiertos.gob.pe/dataset/estado-de-resultado-integral-informaci%C3%B3n-financiera-de-empresas-supervisadas-por-la-smv)
   - Período: 2011 – presente
   - Contenido: Información financiera trimestral sobre los **resultados
     integrales** de empresas supervisadas por la SMV. Incluye resultados netos
     y partidas adicionales de ganancias/pérdidas, con hasta cuatro columnas de
     montos comparativos. La cobertura no es completa para todos los periodos y
     empresas (algunas aparecen en otros estados financieros pero no aquí).
   - Columnas:
     - RPJ (código de la empresa en la SMV)
     - TipoEmpresa (categoría de la empresa, ej. sociedades administradoras,
       bancos, etc.)
     - TipoSector (sector económico, a veces vacío)
     - NombreEmpresa (razón social completa)
     - RUC (número de RUC de la empresa)
     - CIIU (código de actividad económica, a veces vacío)
     - Ejercicio (año del reporte)
     - TipoInformacion (ej. Trimestral Individual, Consolidado)
     - Trimestre (ej. “1er Trimestre”)
     - Moneda (ej. Soles, Dólares)
     - MetodoFlujoEfectivo (campo heredado de la estructura, a veces aparece
       aunque no sea relevante aquí)
     - Cuenta (código contable, ej. 5D0101)
     - DescripcionCuenta (nombre de la cuenta, ej. “Ganancia (Pérdida) Neta del
       Ejercicio”)
     - Monto1 (primer valor reportado)
     - Monto2 (segundo valor comparativo)
     - Monto3 (tercer valor, si aplica)
     - Monto4 (cuarto valor, si aplica)
     - FechaRegistro (fecha de ingreso en el sistema)

7. [Estado de Resultados](https://www.datosabiertos.gob.pe/dataset/estado-de-resultados-informaci%C3%B3n-financiera-de-empresas-supervisadas-por-la-smv)
   - Período: 1999 – presente
   - Contenido: Información financiera trimestral y anual de los **resultados
     (ganancias, ingresos, gastos, etc.)** de empresas supervisadas por la SMV.
     Cada empresa reporta múltiples cuentas (entre 50 y 70 registros por
     periodo). Los datos están organizados por compañía, periodo y tipo de
     información (individual o consolidada).
   - Columnas:
     - RPJ → Código de la empresa en la SMV
     - TipoEmpresa → Tipo de empresa (ej. sociedades agentes de bolsa, bancos,
       etc.)
     - TipoSector → Sector económico (a veces vacío)
     - NombreEmpresa → Razón social completa
     - RUC → Número de RUC (si la empresa es peruana)
     - CIIU → Código de actividad económica (a veces vacío)
     - Ejercicio → Año del reporte
     - TipoInformacion → Tipo de información financiera:
       - TI = Trimestral Individual
       - AI = Anual Individual
       - TC = Trimestral Consolidado
       - AC = Anual Consolidado

     - Trimestre -> Periodo de reporte:
       - A = Anual
       - 1 = 1er Trimestre
       - 2 = 2do Trimestre
       - 3 = 3er Trimestre
       - 4 = 4to Trimestre

     - Moneda -> Moneda en la que se presenta la información:
       - 01 = Soles
       - 02 = Dólares

     - MetodoFlujoEfectivo -> Método de presentación del flujo de efectivo
       (aunque este dataset es de resultados, se hereda el campo de estructura):
       - MI = Método Indirecto
       - MD = Método Directo

     - Cuenta -> Código contable del estado de resultados (ej. 2I2000)
     - DescripcionCuenta -> Nombre de la cuenta (ej. “Ingresos Operacionales”)
     - Monto1 -> Importe del periodo actual
     - Monto2 -> Importe comparado
     - Monto3 -> Importe específico del periodo actual
     - Monto4 -> Importe específico del periodo comparado
     - FechaRegistro

8. [Estado de Situación Financiera](https://www.datosabiertos.gob.pe/dataset/estado-de-situaci%C3%B3n-financiera-informaci%C3%B3n-financiera-de-empresas-supervisadas-por-la-smv)
   - **Período:** 1999 – presente
   - **Contenido:** Información financiera trimestral y anual del **balance
     general** de empresas supervisadas por la SMV. Incluye activos, pasivos y
     patrimonio. Cada empresa reporta múltiples cuentas contables (entre 50 y
     120 registros por periodo). Los datos están organizados por compañía,
     periodo y tipo de información (individual o consolidada).
   - **Columnas:**
     - RPJ → Código de la empresa en la SMV
     - TipoEmpresa → Tipo de empresa (ej. emisoras, bancos, agentes de bolsa,
       etc.)
     - TipoSector → Sector económico (ej. bancos, seguros, etc.)
     - NombreEmpresa → Razón social completa
     - RUC → Número de RUC (si la empresa es peruana)
     - CIIU → Código de actividad económica (a veces vacío)
     - Ejercicio → Año del reporte
     - TipoInformacion → Tipo de información financiera:
       - TI = Trimestral Individual
       - AI = Anual Individual
       - TC = Trimestral Consolidado
       - AC = Anual Consolidado

     - Trimestre → Periodo de reporte:
       - A = Anual
       - 1 = 1er Trimestre
       - 2 = 2do Trimestre
       - 3 = 3er Trimestre
       - 4 = 4to Trimestre

     - Moneda → Moneda en la que se presenta la información financiera:
       - 01 = Soles
       - 02 = Dólares

     - MetodoFlujoEfectivo → Método de presentación del flujo de efectivo (se
       hereda la estructura del dataset, aunque aquí aplica al reporte
       financiero en general):
       - MI = Método Indirecto
       - MD = Método Directo

     - Cuenta → Código de cuenta del balance (ej. 1F0109)
     - DescripcionCuenta → Nombre de la cuenta (ej. “Otras disponibilidades”)
     - Monto1 → Importe de la cuenta en el periodo actual
     - Monto2 → Importe de la cuenta en el periodo comparado
     - FechaRegistro → Fecha de ingreso en el sistema

   Ejemplo de registros (Banco BBVA Perú, 2006, 1er trimestre):
   - Cuenta: **1F0109**, Descripción: _Otras disponibilidades_, Monto1: 8,969,
     Monto2: 10,423
   - Cuenta: **1F0110**, Descripción: _Rendimientos devengados del disponible_,
     Monto1: 5,254, Monto2: 4,738
   - Cuenta: **1F0201**, Descripción: _Fondos interbancarios_, Monto1: 57,512,
     Monto2: 25,253

9. [Principales Cuentas](https://www.datosabiertos.gob.pe/dataset/principales-cuentas-de-informaci%C3%B3n-financiera-de-empresas-supervisadas-por-la-smv)
   - **Período:** 1999 – presente
   - **Contenido:** Información financiera **consolidada en un solo registro por
     empresa y periodo**. Resume las principales cuentas del balance y del
     estado de resultados: activos, pasivos, patrimonio, ingresos y utilidad
     neta. Cada empresa aparece una sola vez por periodo (a diferencia de los
     otros datasets con 50–120 registros).
   - **Parámetros de consulta:**
     1. `sEjercicio` → Año de la información financiera (ej. 2015)
     2. `sPeriodo` → Periodo de reporte:
        - A = Anual
        - 1 = 1er Trimestre
        - 2 = 2do Trimestre
        - 3 = 3er Trimestre
        - 4 = 4to Trimestre

     3. `sTipoInf` → Tipo de información financiera:
        - I = Individual
        - C = Consolidada

   - **Columnas:**
     - RPJ → Código de la empresa en la SMV
     - TipoEmpresa → Tipo de empresa (ej. emisoras, bancos, agentes de bolsa,
       etc.)
     - TipoSector → Sector económico (ej. bancos, seguros, etc.)
     - NombreEmpresa → Razón social completa
     - RUC → Número de RUC (si la empresa es peruana)
     - CIIU → Código de actividad económica (a veces vacío)
     - Ejercicio → Año del reporte
     - TipoInformacion → Tipo de información financiera (TI, AI, TC, AC)
     - Trimestre → Periodo del reporte (A, 1, 2, 3, 4)
     - Moneda → Moneda de la información (01 = Soles, 02 = Dólares)
     - MetodoFlujoEfectivo → Método de flujo de efectivo (MI = Indirecto, MD =
       Directo)
     - ActivoTotal → Total de activos (miles)
     - PasivoTotal → Total de pasivos (miles)
     - PatrimonioTotal → Total del patrimonio (miles)
     - TotalIngreso → Total de ingresos (miles)
     - UtilidadNeta → Utilidad neta (miles)
     - FechaRegistro → Fecha de registro en el sistema

   Ejemplo (2015, 1er trimestre):
   - Banco BBVA Perú: ActivoTotal: 67,743,673 – PasivoTotal: 62,520,573 –
     PatrimonioTotal: 5,223,100 – TotalIngreso: 954,110 – UtilidadNeta: 326,448
   - Banco de Comercio: ActivoTotal: 1,520,571 – PasivoTotal: 1,333,546 –
     PatrimonioTotal: 187,025 – TotalIngreso: 41,975 – UtilidadNeta: 5,443

Algunas ideas que tenemos son:

| Prioridad | Proyecto                         | Descripción                                                                       | Datasets principales                         |
| --------- | -------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------- |
| **Alta**  | Impacto de Crisis Políticas      | Correlacionar eventos políticos con fluctuaciones en estado de resultado integral | Resultado Integral + Precios Cotización      |
| **Alta**  | Análisis de Sectores por Índices | Comparar impacto de diversos sectores usando índices de renta variable            | Índices Renta Variable + Principales Cuentas |
| **Media** | Efectos de Infraestructura       | Evaluar cómo apertura de puertos marítimos afecta la bolsa                        | Precios Cotización + Estado Flujo Efectivo   |
| **Media** | Crecimiento Empresarial          | Analizar trayectoria de crecimiento usando cambios patrimoniales                  | Cambios Patrimonio + Principales Cuentas     |
| **Media** | Inversores Clase Media           | Estudiar patrones de inversión de clase media peruana en BVL                      | Empresas Inscritas + Precios Cotización      |
| **Baja**  | Relaciones Internacionales       | Evaluar factores políticos, tratados y convenios internacionales                  | Todos los estados financieros                |

---

Looking at your datasets objectively, here are some compelling stories you could tell that actually leverage the data's strengths:

## **High-Impact Stories**

**1. "The Hidden Giants: Peru's Corporate Concentration Crisis"**
- Use Dataset #9 (Principales Cuentas) to show how market concentration has evolved
- Combine with Dataset #3 (Empresas Inscritas) to track new vs. established players
- **Story angle**: Are Peru's markets becoming oligopolistic? How do the top 10 companies compare to the bottom 90%?
- **Visual power**: Clear charts showing wealth concentration over time

**2. "The Great Dollarization: Currency Preferences in Peruvian Business"**
- Datasets #4-8 all have currency fields (Soles vs. Dollars)
- **Story angle**: Which sectors report in dollars vs. soles, and how has this changed?
- **Why it matters**: Reveals corporate currency risk strategies and economic sovereignty issues
- **Unique insight**: You might discover sectors that switched reporting currencies during crises

**3. "Quarterly vs. Annual: The Transparency Gap"**
- Compare companies that report quarterly vs. only annually across all financial datasets
- **Story angle**: Who's hiding behind minimal disclosure requirements?
- **Public interest**: Transparency is a major governance issue in Peru
- **Data advantage**: You can quantify transparency patterns across sectors

## **Sector-Specific Deep Dives**

**4. "Banking Empire: How Peru's Financial Giants Really Make Money"**
- Use all financial statement datasets focused on banks (TipoEmpresa = "bancos")
- **Story angle**: Break down revenue sources, profit margins, and growth strategies
- **Why compelling**: Everyone uses banks, few understand how they work
- **Data richness**: Banking data is typically the most complete in your datasets

**5. "The Mining Money Trail"**
- Focus on mining companies across all datasets
- **Story angle**: How do commodity cycles affect corporate behavior?
- **Combine with**: Dataset #1 (stock prices) for mining companies during commodity booms/busts
- **Relevance**: Mining is Peru's economic backbone but poorly understood by general public

## **Financial Health Stories**

**6. "Zombie Companies: The Walking Dead of Lima's Stock Exchange"**
- Use Dataset #9 to identify companies with negative equity or suspicious financials
- **Story angle**: How many listed companies are actually financially viable?
- **Public interest**: Retail investors need this information
- **Methodology**: Create a "financial health score" using multiple indicators

**7. "The Cash Flow Mirage"**
- Use Dataset #5 (Cash Flow) vs Dataset #7 (Income Statement)
- **Story angle**: Which companies report profits but burn cash?
- **Why important**: Classic red flag for investors and creditors
- **Visual appeal**: Scatter plots showing profit vs. cash generation

## **Temporal Analysis**

**8. "The 2008 Survivors: What Makes Companies Crisis-Proof?"**
- Track companies that survived 2008-2009 vs. those that didn't
- Use all datasets to build comprehensive survival profiles
- **Story angle**: Lessons from corporate Darwinism
- **Practical value**: Investment guidance for future crises

**9. "Growth vs. Leverage: The Peruvian Corporate Dilemma"**
- Use Dataset #4 (Patrimonio) and #8 (Balance Sheet) over time
- **Story angle**: How do Peruvian companies finance growth?
- **Economic insight**: Reveals capital market efficiency and corporate strategy patterns

## **Governance & Structure Stories**

**10. "The Consolidation Game: Individual vs. Group Reporting Patterns"**
- All datasets distinguish individual vs. consolidated reporting
- **Story angle**: Which companies use complex corporate structures and why?
- **Relevance**: Corporate transparency and tax optimization stories

**11. "The Registration Rush: SMV Listing Patterns Over Time"**
- Dataset #3 shows when companies registered with SMV
- **Story angle**: What drives companies to go public in Peru?
- **Economic context**: Correlate with economic cycles, regulatory changes

## **Why These Work Better**

1. **Data-driven**: Each story emerges from what the data actually contains
2. **Verifiable**: You can prove your findings with the datasets
3. **Public interest**: These stories matter to investors, policymakers, and citizens
4. **Uniquely accessible**: Only someone with this SMV data could tell these stories
5. **Actionable**: Readers can use these insights for investment/policy decisions

## **Execution Recommendation**

Start with **#1 (Corporate Concentration)** or **#4 (Banking Deep Dive)**. Both offer:
- Clear narrative arc
- Strong visual potential
- Broad public interest
- Manageable scope
- Multiple dataset integration

The key is picking stories that your data can definitively answer, rather than forcing the data to support a predetermined narrative about political impacts.

---

1. how hard is it to be a woman in Peru (violence, trata de personas, missing people, feminicidio) --- David, Pedro
---
1. how do the top 10 companies in Peru compare to the bottom 90% - pudding.cool -- David
2. which sectors report in dollar vs soles, and how has these changes in the last 20 years (covid impact, impeachments, 2008) - pudding.cool
3. app: sacar cita en una posta
4. app: para tracker la ubicacion de los camiones y basura
5. app: para uso interno de las gerencias de seguridad de las municipalidades para poder contar al oficial mas cercano en cuanto una queja se ha realizado
6. financial health for companies in the smv (como un dashboard), how volatile they are (riskier)
7. is the public perception of insecurity and the police real?
