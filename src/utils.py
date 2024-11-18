import os
import subprocess
import pandas as pd
from pathlib import Path


def load_or_download_data(output_file="../data/raw/heart_disease_original_data.csv"):
    """
    Check if the data file exists; if not, run make_dataset.py to generate it.

    Args:
        output_file (str): The relative path to the output data file.

    Returns:
        pd.DataFrame: The loaded dataset as a pandas DataFrame.
    """
    # Define paths relative to the current working directory
    data_file = Path(output_file)
    script_path = Path("../src") / "data" / "make_dataset.py"

    # Check if the data file exists
    if data_file.exists():
        print(f"File found at {data_file}. Loading data...")
    else:
        print(f"File not found at {data_file}. Running {script_path} to generate it...")
        try:
            # Run the make_dataset.py script
            subprocess.run(
                ["python", str(script_path), str(data_file)],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running the script: {e}")
            raise

    # Load the dataset
    return pd.read_csv(data_file)
