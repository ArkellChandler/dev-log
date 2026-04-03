import pandas as pd
from sklearn.datasets import make_classification

def load_raw_data():
    """Gera dados sintéticos para detecção de fraudes (1% de fraude)."""
    X, y = make_classification(n_samples=1000, n_features=20, n_clusters_per_class=1, weights=[0.99], flip_y=0, random_state=42)
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(20)])
    df['is_fraud'] = y
    return df

def preprocess_data(df):
    """Limpeza básica e preparação."""
    return df.dropna()
