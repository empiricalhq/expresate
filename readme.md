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

Relacioando al 

Super intendencia del mercado de valores (ver cómo las relaciones internacionales afectan):
1. Precios de Cotización de Valores
Esta información, disponible desde 1996, ofrece datos diarios sobre los precios de acciones en la Bolsa de Valores de Lima (BVL). Aunque los datos diarios son limitados (aproximadamente 10 puntos por día), son suficientes para un análisis macro.
  Detalles de la data:
    Precios: Incluye precios máximos y mínimos por día.
    Volumen: Registra el monto total transado en cada jornada.
    Cobertura: La información abarca de lunes a viernes y los índices de las empresas cambian con el tiempo.
  Uso para el análisis:
    Se puede identificar cómo eventos específicos, como la firma de tratados internacionales o crisis políticas, impactan la volatilidad y el volumen de negociación.
    Comparar el desempeño de distintos sectores (por ejemplo, minería vs. finanzas) para ver cuál es más sensible a ciertos factores externos.
    El uso de los índices de la BVL es crucial, ya que reflejan el comportamiento de grupos de empresas y pueden ser mejores indicadores del impacto de políticas o eventos.
2. Información de Empresas Inscritas
Esta categoría incluye una lista de empresas inscritas en la SMV por razón social. El dataset también menciona la existencia de datos sobre grupos de la clase media peruana invirtiendo en la BVL, con información desde 1996, aunque limitada.
  Detalles de la data:
    Empresas: La información se organiza por razón social.
    Inversionistas: Se menciona un dataset de inversores de la clase media, con aproximadamente 50 registros para el Banco de Crédito del Perú (BCP).
   Uso para el análisis:
    Estos datos permiten entender la composición de la base de inversores y cómo la participación local en el mercado evoluciona en respuesta a las condiciones económicas y políticas.
3. Información Financiera de Empresas Supervisadas
Esta sección se refiere a los estados financieros de las empresas, que son esenciales para evaluar su salud económica. Se mencionan dos tipos de informes: el Estado de Resultado Integral y las Cuentas Principales.
  Estado de Resultado Integral (ERI): Este informe muestra las ganancias y pérdidas de una empresa en un periodo, incluyendo ingresos y gastos no operativos. Es útil para analizar el impacto de crisis políticas en la rentabilidad de las empresas. El uso del RPJ (identificador de empresas) es necesario para vincular los datos financieros.
  Principales Cuentas de Información Financiera: Similar al anterior, pero descrito como un resumen de movimientos y ganancias totales por trimestre, lo que lo hace potencialmente más relevante para un análisis consolidado y preciso. Se puede utilizar para evaluar el crecimiento de las empresas.



Super intendencia del mercado de valores (ver cómo las relaciones interlacionales afectan)
	Información de Precios de Cotización de Valores según fecha de cotización en la BVL (pasa piola)
		data desde el 96 a la fecha, saber precio máximo y mínimo, monto por día
	Información de Índices del Mercado de Renta Variable en el Perú según fecha del índice en la BVL
		ver índices da mejores indicadores del impacto de la política
		La data diaria es limitada, aprox 10 puntos por día
		comparar cuál es el impacto de diversos sectores
		data dada de lunes a viernes
		los indicies cambian por años
		son indices de un grupo de empresas
	Información de valores representativos de participación patrimonial inscritos en el Registro Público del Mercado de Valores — RPMV, de la SMV, emitidos por sociedades emisoras (descartado)
	Información de los valores representativos de deuda inscritos en el Registro Público del Mercado de Valores — RPMV, de la SMV, emitidos por sociedades emisoras (descartado)
	Información de sanciones de personas jurídicas según fecha de resolución en la SMV (descartado)
	Información de fondos inscritos en la SMV por Razón Social (descartado)
		Información de fondos inscritos en la SMV por RUC (descartado)
	Información de las empresas inscritas en la SMV por Razón Social 
		datasets de grupos de la clase media peruana invirtiendo en la BVL, hay data desde el 96 pero es limitada, hay unos 50 para el BCP (B80004)
	Información de las empresas inscritas en la SMV por RUC (ver el anterior)
	Estado de Cambios en el Patrimonio Información financiera de empresas supervisadas por la SMV
		analizar crecimiento de empresas. se necesita su RPJ (identificador de empresas)
	Estado de Flujo de Efectivo Información financiera de empresas supervisadas por la SMV
		igual al anterior pero de flujo de efectivo
		incluye data desde el 99
	Estado de Resultado Integral Información financiera de empresas supervisadas por la SMV
		ver cómo las crisis politicas afectan la bolsa de valores
		qué es el resultado integral
		similar a los anteriores pero incluye pagos de deudas metodo de flujo efectivo es directo e indirecto
	Estado de Resultados Información financiera de empresas supervisadas por la SMV
		similar al anterior
	Estado de Situación financiera Información financiera de empresas supervisadas por la SMV
		similar al anterior
	Principales cuentas de Información financiera de empresas supervisadas por la SMV
		similar al anterior
		parece ser suma de movimientos y ganancias totales por trimestre, parece más certero y relevante
Ver cómo, por ejemplo, la apertura de puertos marítimos afectan en la bolsa de valores
De manera general, evaluar qué factores pueden influenciar en ella, sean políticos, tratados o convenios internacionales, etc
