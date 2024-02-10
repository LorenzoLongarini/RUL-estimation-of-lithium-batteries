import os
import pandas as pd
from src.utils import constants as cs

def make_soh(path:str='', output_path:str=''):
    # Charge csv from path and initialize capacities
    df = pd.read_csv(path)

    capacities = [value[cs.charge_cap].max() for key, value in df.groupby(cs.white_list[1])]
    initial_capacity = capacities[0]  # Assuming the initial capacity is the first value

    # Calculate SOH as a percentage of the initial capacity
    soh_values = [capacity / initial_capacity * 100 for capacity in capacities]

    # Create a DataFrame with cycles and SOH values
    soh_df = pd.DataFrame({'Cycle': df.groupby(cs.white_list[1]).apply(lambda x: x[cs.c_index].max()).values,
                           'SOH': soh_values})

    # Save the DataFrame to a CSV file
    soh_df.to_csv(output_path, index=False)

# Percorso della cartella contenente i file CSV
folder_path = "src/dataset/cleaned"

# Itera attraverso i file nella cartella
for file_name in os.listdir(folder_path):
    if file_name.startswith("charge-CS2_") or file_name.startswith("discharge-CS2_"):
        # Costruisci il percorso completo del file
        file_path = os.path.join(folder_path, file_name)

        # Crea un nome di output basato sul nome del file
        output_file_name = f"soh_{file_name}"
        output_file_path = os.path.join(folder_path, output_file_name)

        # Applica la funzione make_soh e salva il file CSV
        make_soh(file_path, output_file_path)

        print(f"File CSV creato con successo: {output_file_path}")
