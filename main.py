from sintese import *
import sounddevice as sd

freq_nota = 440.0
duracao = 0.5
f_amostragem = 44100

t = np.linspace(0, duracao, int(f_amostragem * duracao), endpoint=False)

i = 1
while True:
    sinal_fm = fm_batida(i, duracao, f_amostragem)
    print(f'Frequência: {i}Hz')
    sd.play(sinal_fm, f_amostragem)
    sd.wait()
    i += 10
    if (i > 300):
        break

plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
plt.plot(t[:5000], sinal_fm[:5000])
plt.title('Sinal de Síntese FM')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.show()