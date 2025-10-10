class Animals:
    def __init__(self , tiger , lion , camel , cheetah , cow , panther):
    # ATTRIBUTES/PROPERTIES
        self.tiger = tiger
        self.lion = lion
        self.camel = camel
        self.cheetah = cheetah
        self.cow = cow
        self.panther = panther
    
    def carnivorse(self):
        print(f'WILD_ANIMAL_ARE_{self.tiger}_{self.lion}_{self.cheetah}_{self.panther}')     

    
    def herbivorse(self):
        print(f'PET_ANIMALS_ARE__{self.cow}__{self.camel}')

obj:Animals = Animals('ALL_TIGERS' , 'ALL_LIONS' , 'ALL_CAMELS' , 'ALL_CHEETAH' , 'ALL_COWS/BUFFALOS' , 'ALL_PNTHERS__BUT_COLOR_IS__BLACK') 
obj.carnivorse()
obj.herbivorse()       
