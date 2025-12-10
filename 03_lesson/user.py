class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def name(self):
        return self.first_name
    
    def fam(self):
        return self.last_name
    
    def name_fam(self):
        return f"{self.first_name} {self.last_name}"


