from sintese import *
from scipy.io import wavfile
import sounddevice as sd

A1 = 55

INTERVALOS = {
    'A': 0,
    'B': 2,
    'C': 3,
    'D': 5,
    'E': 7,
    'F': 8,
    'G': 10
}

ACIDENTES = {
    'n': 0,
    's': 1,
    'b': -1
}

F_AMOSTRAGEM = 44100
NOME_ARQUIVO = "metal.txt"


with open(f'musicas/{NOME_ARQUIVO}', "r", encoding="utf-8") as arquivo:
            conteudo_total = arquivo.read()

# musica = input()
musica = conteudo_total

musica = musica.split(',')
config = musica[:2]
duracao_padrao = float(config[0][1:])  # Convertendo para float
instrumento = config[1]
sons = musica[2:]
duracao = 0.0
som_final = []

def get_freq(nota, acidente, oitava):
    return A1 * (2 ** ((12 * oitava-1 + INTERVALOS[nota] + acidente)/12))

def get_intensidade(intensidade):
    if intensidade == 'F':
        return 1
    else:
        return 0.5
    
def get_som(freq, duracao, intensidade, instrumento):
    if instrumento == 'Ic':
        return intensidade * fm_corda(freq, duracao, F_AMOSTRAGEM)
    elif instrumento == 'Is':
        return intensidade * fm_sopro(freq, duracao, F_AMOSTRAGEM)
    else:
        return intensidade * fm_batida(freq, duracao_padrao, F_AMOSTRAGEM)


for som in sons:
    nota = som[0]
    acidente = ACIDENTES[som[1]]
    oitava = som[2]
    if instrumento == 'Ip':
        duracao = int(duracao_padrao)
    else:
        duracao = float(duracao_padrao) / float(som[3])
    intensidade = get_intensidade(som[4])

    freq = get_freq(nota, acidente, int(oitava))
    sinal = get_som(freq, duracao, intensidade, instrumento)
    som_final.append(sinal)
    sd.play(sinal, F_AMOSTRAGEM)
    sd.wait()


def aplicar_efeitos_finais(musica, efeitos=['reverb', 'tubescreamer', 'pantera']):
    resultado = musica.copy()
    
    for efeito in efeitos:
        if efeito == 'reverb':
            delay_samples = [int(0.05 * F_AMOSTRAGEM), int(0.1 * F_AMOSTRAGEM), int(0.15 * F_AMOSTRAGEM)]
            decays = [0.6, 0.4, 0.2]
            
            reverb_total = np.zeros_like(resultado)
            for delay, decay in zip(delay_samples, decays):
                if len(resultado) > delay:
                    reverb = np.zeros_like(resultado)
                    reverb[delay:] = resultado[:-delay] * decay
                    reverb_total += reverb
            
            resultado = resultado + reverb_total * 0.5
        
        elif efeito == 'tubescreamer':
            from scipy import signal
            sos_boost = signal.butter(2, [400, 1500], btype='band', fs=F_AMOSTRAGEM, output='sos')
            mid_boosted = signal.sosfilt(sos_boost, resultado)
            
            drive = 25
            clipped = np.tanh(mid_boosted * drive) * 0.8

            sos_tone = signal.butter(2, 3000, btype='low', fs=F_AMOSTRAGEM, output='sos')
            final_signal = signal.sosfilt(sos_tone, clipped)
            
            resultado = resultado * 0.4 + final_signal * 0.6

        elif efeito == 'pantera':
            from scipy import signal

            sos_hp = signal.butter(2, 80, btype='high', fs=F_AMOSTRAGEM, output='sos')
            clean = signal.sosfilt(sos_hp, resultado)

            sos_mid = signal.butter(2, [500, 2000], btype='band', fs=F_AMOSTRAGEM, output='sos')
            mid_content = signal.sosfilt(sos_mid, clean)
            scooped = clean - mid_content * 0.8

            drive = 20
            distorted = np.tanh(scooped * drive) * 0.99

            sos_presence = signal.butter(1, [4000, 6000], btype='band', fs=F_AMOSTRAGEM, output='sos')
            presence = signal.sosfilt(sos_presence, distorted)

            final_signal = distorted + presence * 0.3

            resultado = final_signal
    
    return resultado

musica_final = np.concatenate(som_final)
musica_com_efeitos = aplicar_efeitos_finais(musica_final, ['pantera'])
wavfile.write(f'{NOME_ARQUIVO[:-4]}_sintetizado.wav', F_AMOSTRAGEM, musica_com_efeitos.astype(np.float32))
