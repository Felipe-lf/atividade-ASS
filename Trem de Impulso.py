import numpy as np
import matplotlib.pyplot as plt

def impulse_train(period, duration, total_duration):
    """
    Gera um trem de impulsos.

    Parameters:
    - period: Período do trem de impulsos.
    - duration: Duração de cada impulso.
    - total_duration: Duração total do sinal.

    Returns:
    - time: Eixo do tempo.
    - signal: Sinal do trem de impulsos.
    """
    time = np.arange(0, total_duration, duration)
    signal = np.zeros_like(time)

    for t in time:
        signal[int(t/duration)] = 1

    return time, signal

# Entrada do usuário para o período do trem de impulsos
period = 30
duration = 1
total_duration = 10

# Gera o trem de impulsos
time, signal = impulse_train(period, duration, total_duration)

# Plota o sinal
plt.stem(time, signal)
plt.title('Trem de Impulsos')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.show()
