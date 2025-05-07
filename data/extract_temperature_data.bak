from rich import print
import pandas as pd
import os

# Output file will contain 5 columns:
# Row 1: 1, 2, 3, 4, 5
# Row 2: 5, 6, 7, 8, 9 (note the overlapping value 5)
# Row 3: 9, 10, 11, 12, 13 (again overlapping on 9)

chunksize = 16384

# Input Data and output path
csv_path = r"c:\Users\ghazkul\Downloads\jena_climate_2009_2016.csv"
try:
    data_chunks = pd.read_csv(csv_path, chunksize=chunksize)
except FileNotFoundError:
    print(f"[red]File not found: {csv_path}[/red]")
    exit(1)

# Prepare output file
file_size = os.path.getsize(csv_path)  # in bytes
data_folder = os.path.dirname(os.path.abspath(__file__))
output_filepath = os.path.join(data_folder, "Temperature_Celsius_5Col-2025.csv")

# Remove old output file if it exists
if os.path.exists(output_filepath):
    print(f"Removing old output file: [blue]{output_filepath}[/blue]")
    os.remove(output_filepath)

write_header = True
buffer = pd.DataFrame()  # Stores the tail of the previous chunk

print("Processing Data: ", end="")

for chunk in data_chunks:
    if "T (degC)" not in chunk.columns:
        print("[red]Warning: 'T (degC)' column not found. Skipping chunk.[/red]")
        continue

    print("[green]▇▇▇[/green]", end="")

    # Combine last 4 rows from previous chunk with current chunk
    chunk = pd.concat([buffer, chunk], ignore_index=True)
    chunk = chunk.reset_index(drop=True)

    records = []
    for i in range(0, len(chunk) - 4, 4):
        window = chunk["T (degC)"].iloc[i : i + 5].tolist()
        record = {
            "sensor_1": window[0],
            "sensor_2": window[1],
            "sensor_3": window[2],
            "sensor_4": window[3],
            "label": window[4],
        }
        records.append(record)

    if records:
        pd.DataFrame(records).to_csv(
            output_filepath, mode="a", header=write_header, index=False
        )
        write_header = False

    # Store last 4 rows for next chunk
    buffer = chunk.iloc[-4:].copy()

print("")
print("")
print(
    f"[green]Successfully wrote temperature data to csv file:[/green] [blue]{output_filepath}[/blue]"
)

# Print the few first and last rows of the output file
try:
    output_df = pd.read_csv(output_filepath)
except FileNotFoundError:
    print("[red]Could not read the output file to verify.[/red]")

print("\n[bold green]First few rows of the output file:[/bold green]")
print(output_df.head(5).to_markdown(index=False))
print("\n[bold green]Last few rows of the output file:[/bold green]")
print(output_df.tail(5).to_markdown(index=False))
print("")
