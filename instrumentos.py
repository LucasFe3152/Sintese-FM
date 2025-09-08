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

class Bumbo:
    def __init__(self, freq_nota):
        self.portadora = {
            'attack': 0.002,
            'decay': 0.08,
        }
        self.modulante = {
           'attack': 0.001,
            'decay': 0.03,
        }
         
        self.f_port = freq_nota
        self.f_mod = freq_nota * 11.0 / 8.0

        self.mod_index_max = 12.0

class Caixa:
    def __init__(self, freq_nota):
        self.portadora = {
            'attack': 0.001,
            'decay': 0.05,
        }
        self.modulante = {
           'attack': 0.0005,
            'decay': 0.02,
        }
         
        self.f_port = freq_nota
        self.f_mod = freq_nota * 1.28

        self.mod_index_max = 15.0

class Chimbal:
    def __init__(self, freq_nota):
        self.portadora = {
            'attack': 0.001,
            'decay': 0.15,
        }
        self.modulante = {
           'attack': 0.0005,
            'decay': 0.08,
        }
         
        self.f_port = freq_nota
        self.f_mod = freq_nota * 1.37

        self.mod_index_max = 20.0

class Sino:
    def __init__(self, freq_nota):
        self.portadora = {
            'attack': 0.005,
            'decay': 0.4,
        }
        self.modulante = {
           'attack': 0.002,
            'decay': 0.3,
        }
         
        self.f_port = freq_nota
        self.f_mod = freq_nota * 1.545

        self.mod_index_max = 8.0