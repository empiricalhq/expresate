# Gasto reportado (S/ mil millones)
GASTO_PRIV_2022 = 11.2    # Empresas reportaron al INEI (2022)
GASTO_PUB_2024  = 5.7     # Sector público (2024)

# PIB nominal (USD mil millones)
# Fuente: https://www.imf.org/external/datamapper/NGDPD@WEO/PER?zoom=PER&highlight=PER
PIB_2022_USD = 244.42
PIB_2024_USD = 289.07
PIB_2025_USD = 303.29

# Tipo de cambio promedio 2025 (USD → S/)
# Fuente: https://www.exchange-rates.org/
TIPO_CAMBIO = 3.85

# --- CÁLCULOS ---

# Factores de crecimiento del PIB nominal
factor_2022_2025 = PIB_2025_USD / PIB_2022_USD
factor_2024_2025 = PIB_2025_USD / PIB_2024_USD

# Ajuste de gastos a valores 2025 (S/ mil millones)
gasto_priv_2025 = GASTO_PRIV_2022 * factor_2022_2025
gasto_pub_2025  = GASTO_PUB_2024  * factor_2024_2025

# PIB 2025 en soles (S/ mil millones)
PIB_2025_Soles = PIB_2025_USD * TIPO_CAMBIO

# Porcentajes respecto al PIB 2025
pct_priv = (gasto_priv_2025 / PIB_2025_Soles) * 100
pct_pub  = (gasto_pub_2025  / PIB_2025_Soles) * 100
pct_total = pct_priv + pct_pub

# --- SALIDA ---

print(f"PIB nominal 2025: USD {PIB_2025_USD:,.2f} mil millones")
print(f"PIB 2025 en soles: S/ {PIB_2025_Soles:,.2f} mil millones\n")

print(f"Gasto privado ajustado 2025: S/ {gasto_priv_2025:.2f} mil millones")
print(f"Gasto público ajustado 2025:  S/ {gasto_pub_2025:.2f} mil millones\n")

print("Proporciones sobre PIB 2025:")
print(f"  - Sector privado: {pct_priv:.2f}%")
print(f"  - Sector público: {pct_pub:.2f}%")
print(f"  - Total:          {pct_total:.2f}%")
