# -*- coding: utf-8 -*-
import click
import logging
import pandas as pd
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from ucimlrepo import fetch_ucirepo


@click.command()
# @click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path())
def main(output_filepath):
    """Fetches the heart disease dataset from UCI repository
    and saves it to the specified output filepath.
    """
    logger = logging.getLogger(__name__)
    logger.info("Fetching heart disease dataset from UCI repository")

    # Fetch dataset
    heart_disease = fetch_ucirepo(id=45)

    # Data (as pandas dataframes)
    X = heart_disease.data.features
    y = heart_disease.data.targets

    # Optional: Log metadata and variable information
    logger.info("Dataset metadata:\n{}".format(heart_disease.metadata))
    logger.info("Variable information:\n{}".format(heart_disease.variables))

    # Combine features and targets into one DataFrame
    df = pd.concat([X, y], axis=1)

    # Ensure the output directory exists
    output_path = Path(output_filepath)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the DataFrame to the specified output filepath
    df.to_csv(output_filepath, index=False)
    logger.info("Dataset saved to {}".format(output_filepath))


if __name__ == "__main__":
    # Setup logging format and level
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # Find and load environment variables from the .env file
    load_dotenv(find_dotenv())

    # Execute the main function with command-line arguments
    main()
