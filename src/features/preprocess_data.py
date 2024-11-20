import pandas as pd
from sklearn.model_selection import train_test_split

# from sklearn.preprocessing import LabelEncoder
from utils import load_or_download_data


class DataProcessor:
    def __init__(self, dataset, numerical_cols, categorical_cols, target_col):
        self.numerical_cols = numerical_cols
        self.categorical_cols = categorical_cols
        self.target_col = target_col
        self.data = dataset

    def clean_data(self):
        self.data.dropna(inplace=True)
        return self

    def preprocess_data(self):
        # Convert target variable
        self.data[self.target_col] = self.data[self.target_col].apply(
            lambda x: 1 if x > 0 else 0
        )

        # Encode categorical variables
        for col in self.categorical_cols:
            self.data[col] = self.data[col].astype("category")
            # self.data[col] = LabelEncoder().fit_transform(self.data[col])
        return self

    def split_data(self, test_size=0.2, val_size=0.25, random_state=42):
        df_full_train, df_val = train_test_split(
            self.data, test_size=test_size, random_state=random_state
        )
        df_train, df_test = train_test_split(
            df_full_train, test_size=val_size, random_state=random_state
        )

        X_train = df_train.drop(columns=[self.target_col])
        y_train = df_train[self.target_col]

        X_val = df_val.drop(columns=[self.target_col])
        y_val = df_val[self.target_col]

        X_test = df_test.drop(columns=[self.target_col])
        y_test = df_test[self.target_col]
        # Output the shapes of the splits to verify
        print(
            f"Train set: {X_train.shape}, Validation set: {X_val.shape}, Test set: {X_test.shape}"
        )

        return X_train, y_train, X_test, y_test, X_val, y_val


def main():
    # Initialize DataProcessor
    heart_df = load_or_download_data()
    numerical_cols = ["age", "trestbps", "chol", "thalach", "oldpeak"]
    target_col = "num"
    categorical_cols = [
        col for col in heart_df.columns if col not in numerical_cols + [target_col]
    ]

    data_processor = DataProcessor(
        heart_df,
        numerical_cols=numerical_cols,
        categorical_cols=categorical_cols,
        target_col=target_col,
    )

    # Split the data
    X_train, y_train, X_val, y_val, X_test, y_test = (
        data_processor.clean_data().preprocess_data().split_data()
    )

    return X_train, y_train, X_test, y_test, X_val, y_val
