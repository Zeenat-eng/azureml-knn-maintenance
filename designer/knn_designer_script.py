# KNN inside Azure ML Designer (Execute Python Script)

# Dataset1 = training rows
# Dataset2 = test rows

import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


# Target column
TARGET = "machine_failure"

# Numerical columns
NUM_COLS = [
    "air_temp_k",
    "process_temp_k",
    "rpm",
    "torque_nm",
    "tool_wear_min"
]

# Categorical column
CAT_COLS = ["type"]


# Best K from our notebook
K = 1

# Best weights from our notebook
WEIGHTS = "uniform"


def azureml_main(dataframe1=None, dataframe2=None):

    # Dataset1 is training data
    train = dataframe1

    # Dataset2 is testing data
    test = dataframe2

    # Separate training features
    X_train = train[NUM_COLS + CAT_COLS]

    # Get training target
    y_train = train[TARGET].astype(int)

    # Separate testing features
    X_test = test[NUM_COLS + CAT_COLS]

    # Get testing target
    y_test = test[TARGET].astype(int)


    # Scale numerical columns and encode categorical column
    prep = ColumnTransformer([
        ("num", StandardScaler(), NUM_COLS),
        ("cat", OneHotEncoder(handle_unknown="ignore"), CAT_COLS),
    ])


    # Create KNN pipeline
    model = Pipeline([
        ("prep", prep),
        ("knn", KNeighborsClassifier(
            n_neighbors=K,
            weights=WEIGHTS
        ))
    ])


    # Train the model
    model.fit(X_train, y_train)


    # Predict test data
    pred = model.predict(X_test)

    # Get failure probabilities
    prob = model.predict_proba(X_test)[:, 1]


    # Add predictions to test dataset
    scored = test.copy()

    scored["predicted_failure"] = pred

    scored["failure_probability"] = prob.round(3)


    # Create metrics table
    metrics = pd.DataFrame({
        "metric": [
            "k",
            "accuracy",
            "precision",
            "recall",
            "f1",
            "auc"
        ],

        "value": [
            K,
            accuracy_score(y_test, pred),
            precision_score(y_test, pred, zero_division=0),
            recall_score(y_test, pred),
            f1_score(y_test, pred),
            roc_auc_score(y_test, prob)
        ],
    })


    # Print metrics in job logs
    print(metrics)


    # Return test predictions and metrics
    return scored, metrics