class Virus(object):
    def __init__(self,name, morality_rate, reproduction_rate):
        self.name = name
        self.morality_rate = morality_rate
        self.reproduction_rate = reproduction_rate
    
    def get_name(self):
    	return self.name
        
    def get_sickness_percentage(self):
    	return self.morality_rate

    def get_reproduction_rate(self):
    	return self.reproduction_rate