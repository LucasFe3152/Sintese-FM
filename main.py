from sintese import *

freq_nota = 440.0
duracao = 3.0
f_amostragem = 44100

t = np.linspace(0, duracao, int(f_amostragem * duracao), endpoint=False)

instrumento = Trompete(freq_nota)

env_port = create_adsr_envelope(instrumento.portadora['attack'], instrumento.portadora['decay'], 
                                instrumento.portadora['sustain_level'], instrumento.portadora['release'], duracao, f_amostragem)

env_mod = create_adsr_envelope(instrumento.modulante['attack'], instrumento.modulante['decay'], 
                               instrumento.modulante['sustain_level'], instrumento.modulante['release'], duracao, f_amostragem)

mod_index_max = 5.0 
env_mod = env_mod * mod_index_max

sinal_fm = fm_synth(instrumento.f_port, instrumento.f_mod, env_port, env_mod, duracao, f_amostragem)

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

plt.subplot(3, 1, 2)
plt.plot(t, env_port)
plt.title('Envelope da Portadora (ADSR)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, env_mod)
plt.title('Envelope da modulante (ADSR)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.show()