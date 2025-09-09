# Síntese FM

Este projeto implementa um sintetizador de áudio usando síntese FM (Frequency Modulation) para criar diferentes timbres de instrumentos musicais.

## Estrutura do Projeto

### main.py
O arquivo principal que controla a execução do sintetizador. Para alterar a música a ser tocada, modifique a variável `NOME_ARQUIVO` no início do arquivo.

### instrumentos.py
Contém as classes que definem as características de cada instrumento. Cada classe possui parâmetros que controlam:

- Envelope da portadora (attack e decay)
- Envelope da modulante (attack e decay)
- Frequências relativas (f_port e f_mod)
- Índice máximo de modulação (mod_index_max)

Modificar estes parâmetros alterará diretamente o timbre do instrumento resultante.

### sintese.py
Implementa as funções core do sintetizador FM:

- `fm_synth`: Função principal que realiza a síntese FM, combinando a onda portadora com a modulante
- `adsr_envelope`: Gera envelopes ADSR (Attack, Decay, Sustain, Release) para instrumentos sustentados como sopros
- `exponential_decay_envelope`: Gera envelopes com decay exponencial para instrumentos percussivos
- `fm_sopro`: Implementa síntese específica para instrumentos de sopro
- `fm_corda`: Implementa síntese específica para instrumentos de corda
- `fm_batida`: Implementa síntese específica para instrumentos de percussão

A síntese FM funciona modulando a frequência de uma onda portadora usando uma onda modulante. A quantidade de modulação (índice de modulação) e a relação entre as frequências das ondas determinam o timbre resultante.

## Como Usar

1. Coloque seu arquivo de música na pasta `musicas/`
2. Altere a variável `NOME_ARQUIVO` em `main.py` para o nome do seu arquivo
3. Execute `main.py`
4. O arquivo de áudio sintetizado será salvo com o sufixo "_sintetizado.wav"

## Personalizando Instrumentos

Para modificar o timbre de um instrumento, ajuste os parâmetros na classe correspondente em `instrumentos.py`:

- Aumente/diminua o `attack` e `decay` para mudar a forma como o som inicia e termina
- Modifique a relação `f_mod/f_port` para alterar o timbre base
- Ajuste `mod_index_max` para controlar a riqueza harmônica do som
