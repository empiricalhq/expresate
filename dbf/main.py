import marimo

__generated_with = "0.17.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import geopandas as gpd
    import pandas as pd
    import os

    dbf = "test.dbf"

    try:
        df = gpd.read_file(dbf)
        df = df.drop(columns='geometry', errors='ignore')
    except Exception:
        from simpledbf import Dbf5
        df = Dbf5(dbf, codec='utf-8').to_dataframe()

    csv_path = os.path.splitext(dbf)[0] + ".csv"
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')
    print(f"Saved: {csv_path}")
    return gpd, pd


@app.cell
def _(pd):
    df2 = pd.read_csv("test.csv")
    df2
    return (df2,)


@app.cell
def _(df2):
    df3 = df2.drop(columns=['contacto', 'whatsapp', 'descargar', 'ARCHIVO', 'IDPROV', 'NOMBDEP', 'NOMBPROV', 'AREA', 'CODCCPP', 'LLAVE_MZS'])
    df3.head()
    return


@app.cell
def _(df2, gpd):
    # Read shapefile
    gdf = gpd.read_file("test.shp")

    # Merge with df2 (the one that still has T_TOTAL)
    merged = gdf.merge(df2[["Mz", "T_TOTAL"]], on="Mz", how="left")

    print(f"Total features: {len(merged)}")
    merged.head()
    return (merged,)


@app.cell
def _(merged):
    merged.plot(column="T_TOTAL", legend=True, figsize=(8, 8), cmap="viridis", edgecolor="white")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
