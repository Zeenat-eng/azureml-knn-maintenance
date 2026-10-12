# Automated ML Results (KNN Only)

- Job name: knn-automl-zeenat-v2
- Best scaler and model: RobustScaler + KNN
- Best K: 47
- Weights: uniform
- Distance metric: Manhattan
- Weighted AUC: 0.939713
- Test recall (failure class): 0.03321
- Test F1 (failure class): 0.06429

AutoML selected a RobustScaler + KNN pipeline. Although the AUC is high, the failure-class recall is very low, so the model misses many actual failures.
