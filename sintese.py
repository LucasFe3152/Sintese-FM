import numpy as np
import matplotlib.pyplot as plt
from instrumentos import *

def fm_synth(f_port, f_mod, env_port, env_mod, duracao, f_amostragem=44100):
    t = np.linspace(0, duracao, int(f_amostragem * duracao), endpoint=False)
    if isinstance(env_port, (int, float)):
        env_port = np.ones_like(t) * env_port
    if isinstance(env_mod, (int, float)):
        env_mod = np.ones_like(t) * env_mod
    
    modulante = env_mod * np.sin(2 * np.pi * f_mod * t)
    portadora = env_port * np.sin(2 * np.pi * f_port * t + modulante)
    portadora = portadora / np.max(np.abs(portadora))
    return portadora

def adsr_envelope(attack, decay, sustain_level, release, duracao, f_amostragem):
    total_samples = int(duracao * f_amostragem)
    t = np.linspace(0, duracao, total_samples, endpoint=False)
    
    attack_samples = int(attack * total_samples)
    decay_samples = int(decay * total_samples)
    release_samples = int(release * total_samples)
    sustain_samples = total_samples - attack_samples - decay_samples - release_samples
    
    envelope = np.zeros(total_samples)
    envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
    envelope[attack_samples:attack_samples+decay_samples] = np.linspace(1, sustain_level, decay_samples)
    envelope[attack_samples+decay_samples:attack_samples+decay_samples+sustain_samples] = sustain_level
    envelope[attack_samples+decay_samples+sustain_samples:] = np.linspace(sustain_level, 0, release_samples)
    
    return envelope

def exponential_decay_envelope(attack, decay_time, duracao, f_amostragem):
    total_samples = int(duracao * f_amostragem)
    t = np.linspace(0, duracao, total_samples, endpoint=False)
    
    attack_samples = int(attack * f_amostragem)
    envelope = np.zeros(total_samples)
    
    envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
    
    decay_start = attack_samples
    decay = np.exp(-(t[decay_start:] - t[decay_start]) / decay_time)
    envelope[decay_start:] = decay
    
    return envelope

def fm_sopro(frequencia, duracao, f_amostragem):
    tromp = Trompete(frequencia)
    env_port = adsr_envelope(tromp.portadora['attack'], tromp.portadora['decay'], 
                                tromp.portadora['sustain_level'], tromp.portadora['release'], duracao, f_amostragem)

    env_mod = adsr_envelope(tromp.modulante['attack'], tromp.modulante['decay'], 
                               tromp.modulante['sustain_level'], tromp.modulante['release'], duracao, f_amostragem)
    
    mod_index_max = 5.0 
    env_mod = env_mod * mod_index_max

    sopro_fm = fm_synth(tromp.f_port, tromp.f_mod, env_port, env_mod, duracao, f_amostragem)

    return sopro_fm

def fm_corda(frequencia, duracao, f_amostragem):
    corda = Corda(frequencia)
    mod_index_max = 8.0

    env_port = exponential_decay_envelope(corda.portadora['attack'], corda.portadora['decay'], duracao=duracao, f_amostragem=f_amostragem)

    env_mod = exponential_decay_envelope(corda.modulante['attack'], corda.modulante['decay'], duracao=duracao, f_amostragem=f_amostragem) * mod_index_max

    corda_fm = fm_synth(corda.f_port, corda.f_mod, env_port, env_mod, duracao, f_amostragem)
    
    return corda_fm

def fm_batida(frequencia, duracao, f_amostragem):
    batida = Caixa(frequencia)

    env_port = exponential_decay_envelope(batida.portadora['attack'], batida.portadora['decay'], duracao=duracao, f_amostragem=f_amostragem)

    env_mod = exponential_decay_envelope(batida.modulante['attack'], batida.modulante['decay'], duracao=duracao, f_amostragem=f_amostragem) * batida.mod_index_max

    batida_fm = fm_synth(batida.f_port, batida.f_mod, env_port, env_mod, duracao, f_amostragem)
    
    return batida_fm

