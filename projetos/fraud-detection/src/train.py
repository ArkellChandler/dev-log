import sys
import os

# Garante que os módulos locais sejam priorizados
sys.path.insert(0, os.path.dirname(__file__))

import data_loader
import models
import matplotlib.pyplot as plt
import seaborn as sns
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

# Gerando e Salvando a Matriz de Confusão (Gráfico)
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Não Fraude', 'Fraude'], yticklabels=['Não Fraude', 'Fraude'])
plt.title('Matriz de Confusão - Detecção de Fraudes')
plt.ylabel('Real')
plt.xlabel('Predito')
plt.savefig('../reports/figures/confusion_matrix.png')
print("Gráfico de Matriz de Confusão salvo em: reports/figures/confusion_matrix.png")

print("--- [ TRAINING_COMPLETE ] ---")
