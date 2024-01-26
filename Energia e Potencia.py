import numpy as np
import matplotlib.pyplot as plt

def calcular_potencia(sinal):
    """
    Calcula a potência de um sinal.

    Parâmetros:
    - sinal: array, o sinal de entrada (contínuo ou discreto).

    Retorna:
    - potencia: float, potência do sinal.
    """
    potencia = np.mean(np.abs(sinal)**2)
    return potencia

def calcular_energia(sinal, tempo_amostragem=None):
    """
    Calcula a energia de um sinal.

    Parâmetros:
    - sinal: array, o sinal de entrada (contínuo ou discreto).
    - tempo_amostragem: float, intervalo de amostragem para sinais contínuos (opcional).

    Retorna:
    - energia: float, energia do sinal.
    """
    if tempo_amostragem is not None:
        energia = np.sum(np.abs(sinal)**2) * tempo_amostragem
    else:
        energia = np.sum(np.abs(sinal)**2)
    return energia

# Criar sinais de exemplo
tempo = np.linspace(0, 1, 1000)  # 1000 pontos entre 0 e 1 segundo
sinal_continuo = np.sin(2 * np.pi * 5 * tempo)  # sinal senoidal de 5 Hz
sinal_discreto = np.array([1, 2, 3, 4, 5])

# Calcular potência e energia para ambos os sinais
potencia_sinal_continuo = calcular_potencia(sinal_continuo)
energia_sinal_continuo = calcular_energia(sinal_continuo, tempo_amostragem=tempo[1])
potencia_sinal_discreto = calcular_potencia(sinal_discreto)
energia_sinal_discreto = calcular_energia(sinal_discreto)

print(potencia_sinal_continuo)
print(energia_sinal_continuo)

print(potencia_sinal_discreto)
print(energia_sinal_discreto)

# Plotar os sinais
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(tempo, sinal_continuo)
plt.title('Sinal Contínuo')
plt.xlabel('Tempo')
plt.ylabel('Amplitude')

plt.subplot(1, 2, 2)
plt.stem(sinal_discreto, linefmt='b-', markerfmt='bo', basefmt='r-')
plt.title('Sinal Discreto')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# Plotar gráficos de energia e potência
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.bar(['Potência', 'Energia'], [potencia_sinal_continuo, energia_sinal_continuo], color=['orange', 'green'])
plt.title('Sinal Contínuo')
plt.ylabel('Valor')

plt.subplot(1, 2, 2)
plt.bar(['Potência', 'Energia'], [potencia_sinal_discreto, energia_sinal_discreto], color=['orange', 'green'])
plt.title('Sinal Discreto')
plt.ylabel('Valor')

plt.tight_layout()
plt.show()
