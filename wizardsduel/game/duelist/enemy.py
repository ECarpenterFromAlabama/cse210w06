from game.duelist.duelist import Duelist

class Enemy(Duelist):
    
    def __init__(self, type):
        super().__init__()
        self.setup_duelist(type)

    def setup_duelist(self, type):
        self._lives_left = 2
        if type == 'red':
            self.add_spell('Fire', 4)
            self.add_spell('Ice', 1)
            self.add_spell('Lightning', 2)      
            for spell in self._spell_dict:
                print(f'{spell} x {self._spell_dict[spell]}')  
        
        elif type == 'blue':
            self.add_spell('Fire', 1)
            self.add_spell('Ice', 2)
            self.add_spell('Lightning', 4)
            self.add_spell('Shield', 1)

        elif type == 'white':
            self.add_spell('Fire', 1)
            self.add_spell('Ice', 4)
            self.add_spell('Lightning', 3)
            self.add_spell('Shield', 1)

        elif type == 'black':
            self.add_spell('Fire', 3)
            self.add_spell('Ice', 3)
            self.add_spell('Lightning', 3)
            self.add_spell('Shield', 1)
            self.add_spell('Overkill', 1)


            