from rich import print
import pandas as pd
import os

# Output file will contain 5 columns:
# feature1, feature2, feature3, feature4, label
# (label is the next row's feature4)

# Input Data
csv_path = r"c:\Users\ghazkul\Downloads\jena_climate_2009_2016.csv"
try:
    data = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f"[red]File not found: {csv_path}[/red]")
    exit(1)

# Extract the temperature column
degc = data["T (degC)"]

# Trim to the nearest multiple of 4
trimmed_length = len(degc) - (len(degc) % 4)
degc_trimmed = degc.iloc[:trimmed_length]

# Reshape
reshaped = degc_trimmed.values.reshape(-1, 4)

# Convert to a DataFrame with named columns
df_reshaped = pd.DataFrame(
    reshaped, columns=["feature1", "feature2", "feature3", "feature4"]
)

# Create label from next row's feature4
df_reshaped["label"] = df_reshaped["feature4"].shift(-1)

# drop the last row, since it will have a NaN label
df_reshaped = df_reshaped.dropna()

# Prepare output file
data_folder = os.path.dirname(os.path.abspath(__file__))
output_filepath = os.path.join(data_folder, "Temperature_Celsius_5Col-2025.csv")

# Remove old output file if it exists
if os.path.exists(output_filepath):
    print(f"Removing old output file: [blue]{output_filepath}[/blue]")
    os.remove(output_filepath)

# Save to CSV
df_reshaped.to_csv(output_filepath, index=False)

print(
    f"[green]Successfully wrote temperature data to csv file:[/green] [blue]{output_filepath}[/blue]"
)

# Print the few first and last rows of the output file

print("\n[bold green]First few rows of the output file:[/bold green]")
print(df_reshaped.head(5).to_markdown(index=False))
print("\n[bold green]Last few rows of the output file:[/bold green]")
print(df_reshaped.tail(5).to_markdown(index=False))
print("")
