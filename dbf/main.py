import marimo

__generated_with = "0.17.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    # Población limeña por distritos

    Thanks to geogpsperu for the data: https://drive.google.com/file/d/1qqVdEiCWofxUhPPgSHU0Le82FLUaA7-H/view
    """
    )
    return


@app.cell
def _():
    import geopandas as gpd
    import pandas as pd
    return gpd, pd


@app.cell
def _(gpd):
    dbf_path = "dbf/test.dbf"
    
    # Read DBF and convert to CSV
    df = gpd.read_file(dbf_path)
    df = df.drop(columns="geometry", errors="ignore")
    df.columns = df.columns.str.strip()

    csv_path = dbf_path.replace(".dbf", ".csv")
    df.to_csv(csv_path, index=False, encoding="utf-8-sig")

    print(f'File was saved at {csv_path}')
    return


@app.cell
def _(pd):
    df_attrs = pd.read_csv("dbf/test.csv")
    df_attrs.columns = df_attrs.columns.str.strip()

    # We don't need these columns for our initial tests
    cols_to_drop = [
        "contacto", "whatsapp", "descargar", "ARCHIVO", "IDPROV",
        "NOMBDEP", "NOMBPROV", "AREA", "CODCCPP", "LLAVE_MZS"
    ]
    df_attrs = df_attrs.drop(columns=cols_to_drop, errors="ignore")

    df_attrs
    return (df_attrs,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Merge the shp file (geometry data) with the attribute data""")
    return


@app.cell
def _(df_attrs, gpd):
    gdf = gpd.read_file("dbf/test.shp")
    gdf.columns = gdf.columns.str.strip()

    # We drop T_TOTAL to avoid duplication on merge
    gdf = gdf.drop(columns=["T_TOTAL"], errors="ignore")

    # Merge on Mz key
    merged = gdf.merge(df_attrs[["Mz", "T_TOTAL"]], on="Mz", how="left")

    merged[['Mz', 'T_TOTAL']]
    return (merged,)


@app.cell
def _(merged):
    ax = merged.plot(
        column="T_TOTAL",
        legend=True,
        figsize=(10, 10),
        cmap="viridis",
        edgecolor="white",
        linewidth=0.3,
        missing_kwds={"color": "lightgrey"}
    )

    ax.set_title("Distribución de la población (T_TOTAL) por Manzana en Lima", fontsize=14)
    ax.set_axis_off()

    ax
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
