from rich import print
import pandas as pd
import os

# Input and output
data_chunks = pd.read_csv(
    r"c:\Users\ghazkul\Downloads\jena_climate_2009_2016.csv", chunksize=10240000
)
data_folder = os.path.dirname(__file__)
output_filepath = os.path.join(data_folder, "Temperature_Celsius_5Col-2025.csv")

# Remove the file if it exists (optional: clean start)
if os.path.exists(output_filepath):
    os.remove(output_filepath)

write_header = True  # Initialize header flag

for chunk in data_chunks:
    if "T (degC)" in chunk.columns:
        num_rows = len(chunk)
        records = []

        for i in range(0, num_rows - 4):  # Slide by 1 row instead of 5
            record = {
                "sensor_1": chunk["T (degC)"].iloc[i],
                "sensor_2": chunk["T (degC)"].iloc[i + 1],
                "sensor_3": chunk["T (degC)"].iloc[i + 2],
                "sensor_4": chunk["T (degC)"].iloc[i + 3],
                "label": chunk["T (degC)"].iloc[i + 4],
            }
            records.append(record)

        if records:
            df_to_write = pd.DataFrame(records)
            df_to_write.to_csv(
                output_filepath, mode="a", header=write_header, index=False
            )
            write_header = False
    else:
        print(
            "[yellow]Warning: 'T (degC)' column not found in this chunk. Skipping chunk.[/yellow]"
        )

print(f"[green]Successfully wrote temperature columns to {output_filepath}[/green]")
