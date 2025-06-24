import numpy as np
import matplotlib.pyplot as plt
import time
import winsound  # Para Windows (alternativa: simpleaudio para multiplataforma)

f0 = 261.63  # Dó central

# Ciclo das quintas em semitons
semitons_ciclo = [(7 * i) % 12 for i in range(12)]
notas = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Db', 'Ab', 'Eb', 'Bb', 'F']

# Ângulos corrigidos - sentido horário com C no topo
angulos = [np.pi/2 - 2 * np.pi * i/12 for i in range(12)]

# Números complexos
pontos_complexos = [np.exp(1j * theta) for theta in angulos]
x = [z.real for z in pontos_complexos]
y = [z.imag for z in pontos_complexos]

# Plot
plt.figure(figsize=(8, 8))
plt.plot(x, y, 'o-', color='green')

circle = plt.Circle((0, 0), 1, color='lightgray', fill=False, linestyle='--')
plt.gca().add_artist(circle)

for xi, yi, nota in zip(x, y, notas):
    plt.text(xi * 1.1, yi * 1.1, nota, ha='center', va='center', fontsize=12, weight='bold')

plt.title('Ciclo das Quintas – 12-TET (Começando em Dó)', fontsize=14)
plt.axis('equal')
plt.grid(True)

#Reprodução das notas
for i, semitom in enumerate(semitons_ciclo):
    frequencia = f0 * (2 ** (semitom / 12))
    nota = notas[i]
    print(f"Tocando nota {nota} ({frequencia:.2f} Hz)")
    
    winsound.Beep(int(frequencia), 1000)  # 1000ms = 1 segundo
    
    # Pequena pausa entre notas
    time.sleep(0.2)

# Mostrar o gráfico 
plt.show()

print("Ciclo das quintas concluído!")