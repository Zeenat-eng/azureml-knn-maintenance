
import os
import json
import pandas as pd
import mlflow.pyfunc

def init():
    global model
    model_dir = os.path.join(
        os.environ["AZUREML_MODEL_DIR"], "model"
    )
    model = mlflow.pyfunc.load_model(model_dir)

def run(raw_data):
    data = json.loads(raw_data)
    input_data = data["input_data"]
    df = pd.DataFrame(
        input_data["data"],
        columns=input_data["columns"]
    )
    predictions = model.predict(df)
    return {"predictions": predictions.tolist()}
