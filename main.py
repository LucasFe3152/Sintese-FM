from sintese import *
import sounddevice as sd

freq_nota = 440.0
duracao = 1.0
f_amostragem = 44100

t = np.linspace(0, duracao, int(f_amostragem * duracao), endpoint=False)

for i in range (0, 800, 50):
    sinal_fm = fm_corda(i, duracao, f_amostragem)

    print(f'Frequência: {i}Hz')
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