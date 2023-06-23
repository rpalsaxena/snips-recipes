# Evaluation metrics

## RMSE: 

```
from sklearn.metrics import mean_squared_error

rmse = mean_squared_error(randomf_pred, y, squared = False)
rmse
```
It can also be coded this way:
```
randomf_pred = rf.predict(X)
rmse_randomf = np.sqrt(((randomf_pred - y)**2).mean())
print(rmse_randomf)
```
