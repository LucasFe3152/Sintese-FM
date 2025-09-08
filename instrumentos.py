class Trompete:
    def __init__(self, freq_nota):
        self.portadora = {
            'attack': 0.05,
            'decay': 0.1,
            'sustain_level': 0.7,
            'release': 0.3
        }
        self.modulante = {
           'attack': 0.03,
            'decay': 0.2,
            'sustain_level': 0.6,
            'release': 0.2 
        }
         
        self.f_port = freq_nota
        self.f_mod = freq_nota * 1.0
        
class Corda:
    def __init__(self, freq_nota):
        self.portadora = {
            'attack': 0.01,
            'decay': 0.3,
        }
        self.modulante = {
           'attack': 0.005,
            'decay': 0.1,
        }
         
        self.f_port = freq_nota
        self.f_mod = freq_nota * 1.0
        