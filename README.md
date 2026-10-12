# Predictive Maintenance with KNN on Azure Machine Learning

**Student Name:** Zeenat Riaz  
**Roll Number:** C2C

## 1. Problem Statement

This project predicts machine failure using sensor readings from the AI4I 2020 Predictive Maintenance dataset. The dataset contains 10,000 records, and approximately 3.4% represent machine failures.

## 2. Dataset and Preprocessing

* Cleaned dataset: `data/ai4i_clean.csv`
* Target variable: `machine_failure`
* Features include machine type, air temperature, process temperature, rotational speed, torque, and tool wear.
* Identifier columns and failure-mode columns were removed to avoid data leakage.

## 3. Approaches

### Approach 1: Notebook
* File: `notebooks/01_knn_notebook.ipynb`
* Algorithm: K-Nearest Neighbors (KNN)
* Scaler: StandardScaler
* Best K: 1
* Distance metric: Manhattan
* Weights: uniform
* Test failure recall: 0.353
* Test failure F1-score: 0.397
* Test AUC: 0.669
* Model tracking and registration: MLflow and Azure Machine Learning

### Approach 2: Automated ML
* Results: `automl/automl_results.md`
* Best scaler and model: RobustScaler + KNN
* Best K: 47
* Distance metric: Manhattan
* Weights: uniform
* Reported weighted AUC: 0.939713
* Test failure recall: 0.03321
* Test failure F1-score: 0.06429

The AutoML weighted AUC and Notebook test AUC may use different averaging methods, so they should not be compared directly without checking their definitions.

### Approach 3: Designer
* Script: `designer/knn_designer_script.py`
* Algorithm: KNN
* Configured K: 1
* Scaler: StandardScaler
* Weights: uniform
* Results: See the completed Azure ML Designer job output.

## 4. Model Comparison

See `results_comparison.md` for the comparison table and reflection questions.

The Notebook achieved higher verified failure-class recall than AutoML. However, the approaches should be evaluated on the same test data and metrics before selecting a production model.

## 5. Deployment

The Notebook model was registered in Azure Machine Learning and tested using a managed online endpoint.

* Endpoint name: `knn-maint-zeenat1`
* Deployment VM: `Standard_F2s_v2`
* Sample request: `deployment/sample-request.json`
* Test script: `deployment/test_endpoint.py`

The endpoint has been deleted after testing to avoid ongoing cloud costs.

## 6. Repository Structure

* `data/` — cleaned dataset
* `notebooks/` — data preparation, model training, and deployment notebooks
* `automl/` — AutoML results
* `designer/` — Designer Python script
* `deployment/` — endpoint testing files
* `screenshots/` — evidence screenshots to be added

## 7. Reflection

1. **Best verified failure recall:** The Notebook approach achieved 0.353 recall, compared with AutoML's 0.03321. Designer results must be checked before making a final three-way ranking.
2. **Difference between approaches:** The recall difference between Notebook and AutoML is substantial. AutoML's low failure recall means it misses many actual failures.
3. **Real factory recommendation:** I would compare all approaches on the same test split, prioritize failure recall and F1-score, investigate false alarms, and monitor the model after deployment.
4. **Class imbalance:** Approximately 3.4% of records represent failures. Accuracy alone can be misleading. Possible improvements include resampling, class-aware methods, collecting more failure examples, and tuning the decision threshold using validation data.

## 8. What I Learned

This project helped me practise KNN classification, data preprocessing, feature scaling, and evaluation on an imbalanced dataset. I also explored experiment tracking and model registration with Azure Machine Learning, Automated ML, and Designer. Finally, I learned how to test a managed online endpoint and compare models using failure-class metrics.
