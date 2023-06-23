
### Feature importance snippet

This takes in the model and check feature importance for model rf. Plots the horizontal bar chart
```
feat_importances = pd.Series(rf.feature_importances_, index = X.columns)
feat_importances.sort_values(ascending=True).plot(kind='barh')
```

![](https://lh3.googleusercontent.com/drive-viewer/AFGJ81p9lPc9peRDj4yduJvf86b7lbMYpJoyijvFDAioNq1y3SJz3dkPQom648HaowB48xw5dljYq3NLj5tmdN1CNGkiqyvT=s2560)
