from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
import xgboost as xgb

def train_XgboostClassifier(X, y, params):
    # Train XGB Classifier
    for i in params:
        model = xgb.XGBClassifier(n_estimators=i[0], max_depth=i[1], eta=i[2], subsample=0.7, colsample_bytree=0.8)
        cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=10, random_state=1)
        # evaluate model
        scores = cross_val_score(model, X, y, scoring='f1', cv=cv, n_jobs=-1)
        print(i)
        print('F1: %.3f (%.3f)' % (scores.mean(), scores.std()))
