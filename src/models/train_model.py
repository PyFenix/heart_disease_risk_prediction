from sklearn.model_selection import GridSearchCV
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
import pickle


class ModelTrainer:
    def __init__(self, models):
        self.models = models  # Dictionary of models
        self.trained_models = {}

    def train_models(self, X_train, y_train):
        for model_name, model in self.models.items():
            print(f"Training {model_name}...")
            model.fit(X_train, y_train)
            self.trained_models[model_name] = model
        print("*" * 12)
        print("All models trained! Next step is performance evaluation.")
        print("*" * 12)
        print("*" * 12)
        return self

    def evaluate_models(self, X_test, y_test):
        for model_name, model in self.trained_models.items():
            print(f"Evaluating {model_name}...")
            predicted = model.predict(X_test)

            # Compute metrics
            conf = confusion_matrix(y_test, predicted)
            accuracy = accuracy_score(y_test, predicted) * 100
            precision = precision_score(y_test, predicted) * 100
            recall = recall_score(y_test, predicted) * 100
            f1 = f1_score(y_test, predicted) * 100

            # Print results
            print("*" * 12)
            print(f"Confusion Matrix for {model_name}: \n{conf}")
            print(f"Accuracy of {model_name}: {accuracy:.2f}%")
            print(f"Precision of {model_name}: {precision:.2f}%")
            print(f"Recall of {model_name}: {recall:.2f}%")
            print(f"F1 Score of {model_name}: {f1:.2f}%")
            print("\n" + "=" * 60 + "\n")


class HyperparameterTuner:
    def __init__(self, param_grids, scoring="recall", cv=5, n_jobs=-1):
        self.param_grids = param_grids  # Dictionary with model name as key
        self.best_models = {}
        self.scoring = scoring
        self.cv = cv
        self.n_jobs = n_jobs

    def tune_models(self, X_train, y_train):
        for model_name, model_info in self.param_grids.items():
            print(f"Tuning hyperparameters for {model_name}...")
            grid_search = GridSearchCV(
                estimator=model_info["model"],
                param_grid=model_info["params"],
                scoring=self.scoring,
                cv=self.cv,
                verbose=1,
                error_score="raise",
                n_jobs=self.n_jobs,
            )
            grid_search.fit(X_train, y_train)

            # Store the best model and parameters
            self.best_models[model_name] = {
                "best_estimator": grid_search.best_estimator_,
                "best_params": grid_search.best_params_,
                "best_score": grid_search.best_score_,
            }
            print(f"Best Parameters for {model_name}: {grid_search.best_params_}")
            print(
                f"Best {self.scoring.capitalize()} Score for {model_name}: {grid_search.best_score_:.3f}\n"
            )
        return self.best_models

    def get_best_models(self):
        # Extract the best-performing model
        self.best_model = max(
            self.best_models.items(), key=lambda x: x[1]["best_score"]
        )

        # Display the best model's information
        best_model_name, best_model_info = self.best_model
        print(f"Best Model: {best_model_name}")
        print(f"Best Estimator: {best_model_info['best_estimator']}")
        print(f"Best Params: {best_model_info['best_params']}")
        print(f"Best Score: {best_model_info['best_score']}")
        return self

    def save_best_model_to_pickle(self, filepath="models/trained_model.pkl"):
        if not self.best_model:
            raise ValueError("No best model found. Run `get_best_models()` first.")

            # Ensure file has .pkl extension
        if not filepath.endswith(".pkl"):
            filepath += ".pkl"

        # Extract the best estimator
        best_model_info = self.best_model[
            1
        ]  # [0] is the model name, [1] is the details
        best_estimator = best_model_info["best_estimator"]

        # Save to pickle
        with open(filepath, "wb") as f:
            pickle.dump(best_estimator, f)
        print(f"Best model saved to {filepath}")
