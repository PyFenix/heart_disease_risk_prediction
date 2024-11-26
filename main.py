from src.utils import load_or_download_data
from src.features.preprocess_data import DataProcessor
from src.models.train_model import ModelTrainer
from src.models.train_model import HyperparameterTuner
from src.models.model_params import models, model_param_grids
import logging

"""
main.py

This script orchestrates the machine learning pipeline for heart disease prediction.
It performs the following steps:
1. Downloads and loads the dataset.
2. Preprocesses the data.
3. Trains multiple machine learning models.
4. Tunes hyperparameters for the models.
5. Selects and saves the best-performing model.

Models used:
- Logistic Regression
- Support Vector Classifier
- XGBoost Classifier
- Decision Tree Classifier
"""

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """
    Main function to execute the machine learning pipeline.
    """

    # Step 1: Download data
    logger.info("Downloading data...")
    heart_df = load_or_download_data()
    logger.info("Data downloaded successfully.")

    # Step 2: Preprocess data
    # Define the numerical columns
    numerical_cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

    # Define the categorical columns by excluding numerical ones
    categorical_cols = [col for col in heart_df.columns if col not in numerical_cols]

    logger.info("Categorical Columns:", categorical_cols)
    logger.info("Numerical Columns:", numerical_cols)
    logger.info("Preprocessing data...")
    data_processor = DataProcessor(
        heart_df,
        numerical_cols,
        categorical_cols,
        'num'
        )
    X_train, y_train, X_val, y_val, X_test, y_test = (
        data_processor.clean_data().preprocess_data().split_data()
        )
    logger.info("Data preprocessed successfully.")

    # Step 3: Train model
    logger.info("Training model...")

    ModelTrainer(models).train_models(X_train=X_train, y_train=y_train).evaluate_models(X_test=X_test, y_test=y_test)
    logger.info("Model trained successfully.")

    # Step 4: Tune hyperparameters
    logger.info("Tuning hyperparameters...")

    model_tuner = HyperparameterTuner(model_param_grids)
    # best_models = model_tuner.tune_models(X_train=X_train, y_train=y_train)
    # Selecting the best performing model
    best_model = model_tuner.get_best_models()
    logger.info("Hyperparameters tuned successfully.")
    logger.info(f"The best performing model after tuning is {best_model.best_model[0]}")

    # Step 5: Save the best model
    logger.info("Saving the best model...")
    model_tuner.save_best_model_to_pickle(filepath="/models/trained_model")
    logger.info("Model saved successfully.")

if __name__ == '__main__':
    main()
