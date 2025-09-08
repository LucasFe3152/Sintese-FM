from sintese import *
import sounddevice as sd

freq_nota = 220.0
duracao = 3.0
f_amostragem = 44100

t = np.linspace(0, duracao, int(f_amostragem * duracao), endpoint=False)

sinal_fm = fm_sopro(freq_nota, duracao, f_amostragem)

print("Reproduzindo som FM...")
sd.play(sinal_fm, f_amostragem)
sd.wait()

plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
plt.plot(t[:5000], sinal_fm[:5000])
plt.title('Sinal de Síntese FM')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.show()