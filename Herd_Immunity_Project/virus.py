class Virus(object):
    def __init__(self, virus_name, repo_rate, morality_rate):
        self.name = virus_name
        self.repo_rate = repo_rate
        self.morality_rate = morality_rate

    def get_repo_rate(self):
        return self.repo_rate

    def get_morality_rate(self):
        return self.morality_rate
    
    def get_virus_name(self):
        return self.name
