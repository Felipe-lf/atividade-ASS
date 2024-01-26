import numpy as np
import matplotlib.pyplot as plt

def degrau_unitario(t, a=0):
    """
    Gera um degrau unitário deslocado temporalmente para tempo contínuo.

    Parâmetros:
    - t: array, vetor de tempo.
    - a: float, valor do deslocamento temporal (padrão é 0).

    Retorna:
    - sinal: array, sinal de degrau unitário deslocado.
    """
    sinal = np.zeros_like(t)
    sinal[t >= a] = 1
    return sinal

def degrau_unitario_discreto(n, k=0):
    """
    Gera um degrau unitário discreto deslocado temporalmente.

    Parâmetros:
    - n: array, vetor de índices de tempo discreto.
    - k: int, valor do deslocamento temporal (padrão é 0).

    Retorna:
    - sinal: array, sinal de degrau unitário discreto deslocado.
    """
    sinal = np.zeros_like(n)
    sinal[n >= k] = 1
    return sinal

# Exemplo de uso para tempo contínuo
tempo = np.linspace(-1, 5, 1000)  # Vetor de tempo de -1 a 5 segundos
deslocamento_temporal = 2

# Gerar degrau unitário deslocado para tempo contínuo
degrau_deslocado = degrau_unitario(tempo, a=deslocamento_temporal)

# Plotar o degrau unitário deslocado para tempo contínuo
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(tempo, degrau_deslocado, label=f'Degrau Deslocado (a={deslocamento_temporal})')
plt.title('Degrau Unitário Deslocado (Tempo Contínuo)')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Exemplo de uso para tempo discreto
indices_temporais = np.arange(-5, 10)  # Vetor de índices de tempo discreto
deslocamento_temporal_discreto = 2

# Gerar degrau unitário discreto deslocado
degrau_deslocado_discreto = degrau_unitario_discreto(indices_temporais, k=deslocamento_temporal_discreto)

# Plotar o degrau unitário discreto deslocado
plt.subplot(1, 2, 2)
plt.stem(indices_temporais, degrau_deslocado_discreto, basefmt='b-', markerfmt='bo', linefmt='r-')
plt.title('Degrau Unitário Discreto Deslocado')
plt.xlabel('Índices Temporais')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
