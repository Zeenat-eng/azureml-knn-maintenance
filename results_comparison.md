# Model Comparison

| Metric | Notebook | AutoML | Designer |
|---|---:|---:|---|
| Best K | 1 | 47 | 1 (configured) |
| Weights | uniform | uniform | uniform |
| Scaler | StandardScaler | RobustScaler | StandardScaler |
| Test recall (failure) | 0.353 | 0.03321 | Pending actual job output |
| Test F1 (failure) | 0.397 | 0.06429 | Pending actual job output |
| Test AUC | 0.669 | 0.939713 (weighted) | Pending actual job output |
| Code written | Yes | No, AutoML configuration | Yes |
| Setup style | Notebook | Automated search | Visual pipeline |
| Managed endpoint | Yes, model registered | Depends on selected model registration | Classic Designer component is not directly deployable as a managed endpoint |

## Reflection

1. The Notebook approach achieved the highest verified failure recall among the two approaches with available test metrics: 0.353 versus AutoML's 0.03321. AutoML's AUC is weighted, so it should not be treated as directly comparable to the Notebook's binary test AUC without confirming the same calculation.
2. The difference in failure recall is substantial. AutoML's low recall means it misses many actual failures despite its high weighted AUC.
3. For a real factory, I would prioritize failure recall and F1, validate performance on representative data, and monitor false alarms. I would compare models on the same test split before selecting a production model.
4. The dataset is imbalanced: failures are approximately 3.4% of records. Accuracy alone can be misleading. Useful improvements include collecting more failure examples, using suitable resampling or class-aware methods, and tuning the decision threshold based on validation results.
