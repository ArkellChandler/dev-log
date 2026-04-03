from xgboost import XGBClassifier

def get_model():
    return XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
