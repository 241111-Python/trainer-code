class Pokemon:
    def __init__(self, ID, Name, Type_1, Type_2, Total, HP, Attack, Defense, Sp_Atk, Sp_Def, Speed, Generation, Legendary):
        self.ID = ID
        self.Name = Name
        self.Type_1 = Type_1
        self.Type_2 = Type_2
        self.Total = Total
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.Sp_Atk = Sp_Atk
        self.Sp_Def  = Sp_Def
        self.Speed = Speed
        self.Generation = Generation
        self.Legendary = Legendary

    # def __init__(self, *x):
    #     self.x = x

    def __str__(self):
        return f'{self.Name}: #{self.ID} - {self.Type_1}'

    # def __str__(self):
    #     return f'{self.x}'

# (1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False)


import csv
path = './../SourceData/pokemon.csv'
pokelist = []
with open(path, "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        entry = Pokemon(*row)
        # print(*row)
        pokelist.append(entry)

for i in pokelist:
    print(i)