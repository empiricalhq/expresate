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

**What approach we could take**:

1. Compare perceptions of insecurity with actual reported crimes (Lambayeque as
   a case study).
2. Analyze whether police personnel distribution corresponds to crime incidence
   and perception hotspots.
3. Highlight mismatches that may reduce institutional trust and propose
   evidence-based reallocation strategies.

## ODS 8

| Dataset | Período | Contenido | Estado |
|---------|---------|-----------|--------|
| Precios de Cotización BVL | 1996-presente | Precio máximo, mínimo, monto diario | **Disponible** |
| Índices de Renta Variable BVL | Actual | ~10 puntos diarios, lun-vie, composición cambia | **Disponible** |
| Empresas Inscritas SMV | 1996-presente | Por razón social/RUC, ~50 registros BCP | **Disponible** |
| Estado de Cambios en Patrimonio | Variable | Análisis crecimiento empresarial, requiere RPJ | **Disponible** |
| Estado de Flujo de Efectivo | 1999-presente | Método directo/indirecto | **Disponible** |
| Estado de Resultado Integral | Variable | Incluye pagos de deudas | **Disponible** |
| Estado de Resultados | Variable | Resultados financieros empresariales | **Disponible** |
| Estado de Situación Financiera | Variable | Posición financiera empresarial | **Disponible** |
| Principales Cuentas | Variable | Datos trimestrales agregados (más certero) | **Disponible** |

Algunas ideas que tenemos son:

| Prioridad | Proyecto | Descripción | Datasets Principales |
|-----------|----------|-------------|---------------------|
| **Alta** | Impacto de Crisis Políticas | Correlacionar eventos políticos con fluctuaciones en estado de resultado integral | Resultado Integral + Precios Cotización |
| **Alta** | Análisis de Sectores por Índices | Comparar impacto de diversos sectores usando índices de renta variable | Índices Renta Variable + Principales Cuentas |
| **Media** | Efectos de Infraestructura | Evaluar cómo apertura de puertos marítimos afecta la bolsa | Precios Cotización + Estado Flujo Efectivo |
| **Media** | Crecimiento Empresarial | Analizar trayectoria de crecimiento usando cambios patrimoniales | Cambios Patrimonio + Principales Cuentas |
| **Media** | Inversores Clase Media | Estudiar patrones de inversión de clase media peruana en BVL | Empresas Inscritas + Precios Cotización |
| **Baja** | Relaciones Internacionales | Evaluar factores políticos, tratados y convenios internacionales | Todos los estados financieros |
