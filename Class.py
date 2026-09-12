class Ferarri():
    def __init__(self):
        self.tyre= "rubber"
        self.frame= "carbon fiber"
        self.glass_tint= "50%"
        self.engine= "V12"
        self.lefttyre= self.tyre
    def print_car_details(self):
        print(self.tyre)
        

f712 = Ferarri()
print (f712.lefttyre)
f712.print_car_details()