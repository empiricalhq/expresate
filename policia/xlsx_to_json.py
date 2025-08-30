import pandas as pd
import os
import json

# Carpeta con tus archivos
folder_path = ".\\datasets_csv_xlsx"
output_folder = ".\\datasets_json"
os.makedirs(output_folder, exist_ok=True)

for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if file_name.endswith(".csv"):
        print(f"Procesando CSV: {file_name}")
        df = pd.read_csv(file_path, encoding="latin1", sep="\t")


    elif file_name.endswith(".xlsx"):
        print(f"Procesando XLSX: {file_name}")
        df = pd.read_excel(file_path, sheet_name=0)
    else:
        continue 

    json_data = df.to_json(orient="records", indent=4, force_ascii=False)
    output_file = os.path.splitext(file_name)[0] + ".json"
    output_path = os.path.join(output_folder, output_file)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(json_data)

    print(f"Convertido y guardado en {output_path}")