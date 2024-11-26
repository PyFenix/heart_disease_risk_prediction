from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier

# Define the models in a dictionary
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Support Vector Classifier': SVC(),
    'XGBoost Classifier': XGBClassifier(eval_metric="logloss", enable_categorical=True),
    'Decision Tree': DecisionTreeClassifier()
}

model_param_grids = {
        "Logistic Regression": {
            "model": LogisticRegression(),
            "params": {
                "penalty": ["l1", "l2"],
                "C": [0.01, 0.1, 1, 5, 10],
                "solver": ["liblinear"],# "saga"],
            },
        },
        "Support Vector Classifier": {
            "model": SVC(),
            "params": {
                "C": [0.01, 0.1, 1, 10],
                "kernel": ["linear", "rbf", "poly", "sigmoid"],
                "gamma": ["scale", "auto"],
            },
        },
        "XGBoost Classifier": {
        "model": XGBClassifier(eval_metric="logloss", enable_categorical=True),
        "params": {
            "learning_rate": [0.02, 0.05, 0.1],  # Smaller learning rates for better generalization
            "n_estimators": [50, 100],    # Number of boosting rounds
            "max_depth": [3, 5, 10],      # Limit depth to control model complexity
            "min_child_weight": [1, 3],   # Minimum sum of instance weights in a child
            "gamma": [0, 0.1, 0.3],       # Minimum loss reduction to make a split
            "subsample": [0.8, 1.0],      # Fraction of samples for each tree
            "colsample_bytree": [0.8, 1.0],  # Fraction of features for each tree
            "reg_alpha": [0, 0.1, 1.0],   # L1 regularization
            "reg_lambda": [1.0, 2.0],     # L2 regularization
            },
        },
        "Decision Tree": {
            "model": DecisionTreeClassifier(),
            "params": {
                "criterion": ["gini", "entropy"],
                "max_depth": [5, 10, 20],
                "min_samples_split": [2, 5, 10],
                "min_samples_leaf": [1, 2, 5],
            },
        },
    }
