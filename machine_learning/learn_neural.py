import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import LambdaCallback
from tensorflow.keras.optimizers import Adam
import time

# --- 1. PROVOCANDO OVERFITTING: REDUZIR DATASET (Apenas 100 amostras) ---
X, y = make_moons(n_samples=100, noise=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# --- 2. PROVOCANDO OVERFITTING: REDE MUITO GRANDE (Sem Dropout) ---
model = Sequential([
    Dense(1024, input_shape=(2,), activation='relu'), # Camada Oculta 1 (Bazuca 1)
    Dense(1024, activation='relu'),                  # Camada Oculta 2 (Bazuca 2)
    Dense(512, activation='relu'),                   # Camada Oculta 3 (Bazuca 3)
    # Dense(1, activation='linear') # Se usar linear em vez de sigmoid, causa overfitting mais rapido ainda
    Dense(1, activation='sigmoid')                  # Saída Binária
])

model.compile(optimizer=Adam(learning_rate=0.005), # Taxa de aprendizado alta
              loss='binary_crossentropy',
              metrics=['accuracy'])

# --- 3. CONFIGURAÇÃO INICIAL DO GRÁFICO ---
plt.ion() # Modo interativo ligado
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

def plot_live_updates(epoch, logs):
    """
    Callback para desenhar a fronteira de decisão e a perda a cada época sem fechar a janela.
    """
    if epoch % 10 != 0: return 

    axs[0].cla() # Limpa apenas o eixo 1
    axs[1].cla() # Limpa apenas o eixo 2

    # --- Gráfico 1: Fronteira de Decisão ---
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.05), # Aumentado passo para velocidade
                         np.arange(y_min, y_max, 0.05))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()], verbose=0)
    Z = Z.reshape(xx.shape)

    axs[0].contourf(xx, yy, Z, alpha=0.3, cmap='RdBu')
    axs[0].scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='RdBu', edgecolors='k', s=50, label='Treino')
    axs[0].scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='Reds', edgecolors='k', marker='X', s=50, label='Teste')
    axs[0].set_title(f'Época {epoch+1}: Fronteira de Decisão')
    axs[0].legend()

    # --- Gráfico 2: Curva de Perda ---
    axs[1].plot(train_losses, label='Treino (Loss)', color='blue')
    axs[1].plot(val_losses, label='Validação (Loss)', color='red', linestyle='--')
    axs[1].set_title('Curva de Aprendizado')
    axs[1].set_xlabel('Época')
    axs[1].set_ylabel('Erro (Loss)')
    axs[1].set_ylim(0, max(max(train_losses, default=1), max(val_losses, default=1)) * 1.1)
    axs[1].legend()
    axs[1].grid(True)

    plt.pause(0.01)

# Listas para guardar o histórico de perda
train_losses = []
val_losses = []

# Callback customizado
live_plot_callback = LambdaCallback(on_epoch_end=lambda epoch, logs: [
    train_losses.append(logs['loss']),
    val_losses.append(logs['val_loss']),
    plot_live_updates(epoch, logs)
])

# --- 4. TREINAMENTO AGRESSIVO (500 Épocas) ---
print("Iniciando treinamento AGRESSIVO para provocar OVERFITTING...")
history = model.fit(X_train, y_train,
                    epochs=500,
                    batch_size=10,
                    validation_data=(X_test, y_test),
                    callbacks=[live_plot_callback],
                    verbose=0)

print("\nTreinamento concluído!")
plt.ioff() # Desliga modo interativo para travar a janela aberta no final
plt.show()
