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
NOME_ARQUIVO = "beatit.txt"


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

musica_final = np.concatenate(som_final)
wavfile.write(f'{NOME_ARQUIVO[:-4]}_sintetizado.wav', F_AMOSTRAGEM, musica_final.astype(np.float32))