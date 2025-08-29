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
