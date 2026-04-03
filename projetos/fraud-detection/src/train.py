import sys
import os

# Garante que os módulos locais sejam priorizados
sys.path.insert(0, os.path.dirname(__file__))

import data_loader
import models
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

print("--- [ STARTING_MODEL_TRAINING ] ---")
df = data_loader.load_raw_data()
df = data_loader.preprocess_data(df)

X = df.drop('is_fraud', axis=1)
y = df['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Dados carregados: {len(df)} amostras.")
model = models.get_model()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)

# Salvando o Relatório de Texto
with open("../reports/classification_report.txt", "w") as f:
    f.write(report)
print("\nRelatório de Classificação salvo em: reports/classification_report.txt")

# GERANDO GRÁFICO DE BARRAS HORIZONTAIS (FEATURE IMPORTANCE)
plt.figure(figsize=(10, 8))
importances = pd.Series(model.feature_importances_, index=X.columns)
importances.nlargest(10).sort_values().plot(kind='barh', color='#00f3ff', edgecolor='#ff00ff')

plt.title('TOP 10 - Variáveis Decisivas para Detecção de Fraude', color='white', fontsize=14)
plt.xlabel('Importância Relativa', color='white')
plt.grid(axis='x', linestyle='--', alpha=0.3)

# Estilização HUD/Cyberpunk para o gráfico
plt.gca().set_facecolor('#050505')
plt.gcf().set_facecolor('#050505')
plt.tick_params(colors='white')

plt.tight_layout()
plt.savefig('../reports/figures/feature_importance.png')
print("Gráfico de Importância (Barras Horizontais) salvo em: reports/figures/feature_importance.png")

print("--- [ TRAINING_COMPLETE ] ---")
