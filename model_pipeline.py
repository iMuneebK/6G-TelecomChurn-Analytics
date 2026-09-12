from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class ChurnModel:
    def __init__(self):
        self.model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model.fit(X_train, y_train)
        preds = self.model.predict(X_test)
        return classification_report(y_test, preds)

    def predict(self, X):
        return self.model.predict_proba(X)[:, 1]\n