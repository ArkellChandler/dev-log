import sys
import os
import time

# Garante que os módulos locais sejam priorizados
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_PATH)

import data_loader
import models
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

print("--- [ STARTING_MODEL_TRAINING ] ---")

try:
    start_time = time.time()
    
    # Carregamento e Preparação
    df = data_loader.load_raw_data()
    df = data_loader.preprocess_data(df)
    
    X = df.drop('is_fraud', axis=1)
    y = df['is_fraud']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    n_amostras = len(df)
    print(f"Dados carregados: {n_amostras} amostras.")
    
    # Modelo
    model = models.get_model()
    model.fit(X_train, y_train)
    
    end_time = time.time()
    tempo_treino = end_time - start_time
    
    y_pred = model.predict(X_test)
    report_text = classification_report(y_test, y_pred)
    
    # Definição de Caminhos Absolutos para Relatórios
    REPORTS_DIR = os.path.join(os.path.dirname(BASE_PATH), "reports")
    FIGURES_DIR = os.path.join(REPORTS_DIR, "figures")
    
    # Garante que as pastas de relatórios existam
    os.makedirs(FIGURES_DIR, exist_ok=True)
    
    # Salvando o Relatório de Texto
    comparison_report = f"""
============================================================
RELATÓRIO DE PERFORMANCE E COMPARAÇÃO
============================================================
PROJETO: Fraud Detection (XGBoost)
AMOSTRAS: {n_amostras}
TEMPO DE EXECUÇÃO: {tempo_treino:.4f} segundos
ESTILO: HUD Performance Optimized

COMPARAÇÃO COM PROJETO NEURAL (Referência):
- Amostras Neurais: 100
- Épocas Neurais: 500
- Objetivo: Overfitting Control vs Decision Speed
============================================================

DETALHES DO MODELO:
{report_text}
"""
    
    report_file = os.path.join(REPORTS_DIR, "classification_report.txt")
    with open(report_file, "w") as f:
        f.write(comparison_report)
    print(f"\nRelatório de Classificação e Tempos salvo em: {report_file}")
    
    # GRÁFICO DE BARRAS HORIZONTAIS (HUD OPTIMIZED)
    plt.figure(figsize=(12, 8))
    importances = pd.Series(model.feature_importances_, index=X.columns)
    top_10 = importances.nlargest(10).sort_values()
    
    # Plotagem com Estilo Cyberpunk
    bars = top_10.plot(kind='barh', color='#00f3ff', edgecolor='#ff00ff', linewidth=1.5)
    
    # Adicionando Anotações de Valores para Legibilidade
    for i, v in enumerate(top_10):
        plt.text(v + 0.005, i, f"{v:.4f}", color='#39ff14', fontweight='bold', va='center', fontsize=10)
    
    plt.title('TOP 10 - Variáveis Decisivas para Detecção de Fraude', color='#00f3ff', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Importância Relativa (Score)', color='white', fontsize=12, labelpad=10)
    plt.grid(axis='x', linestyle='--', alpha=0.2, color='#00f3ff')
    
    # Estilização de HUD/Terminal
    plt.gca().set_facecolor('#050505')
    plt.gcf().set_facecolor('#050505')
    plt.tick_params(colors='white', labelsize=11)
    
    # Removendo bordas desnecessárias (spines)
    for spine in plt.gca().spines.values():
        spine.set_color('#00f3ff')
        spine.set_alpha(0.3)
    
    plt.tight_layout()
    chart_file = os.path.join(FIGURES_DIR, "feature_importance.png")
    plt.savefig(chart_file, dpi=300)
    print(f"Gráfico de Importância Otimizado salvo em: {chart_file}")
    
    print("--- [ TRAINING_COMPLETE ] ---")

except Exception as e:
    print(f"\n[ERRO CRÍTICO NO SISTEMA]: {e}")
    sys.exit(1)

