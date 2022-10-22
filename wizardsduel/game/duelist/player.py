from game.duelist.duelist import Duelist

class Player(Duelist):
    
    def __init__(self) -> None:
        super().__init__()
        self.player_level = 1
    
    def level_up(self):
        self.player_level +=1
    
    def setup_duelist(self):
        self._lives_left = 2
        level = self.player_level
        if level == 1:
            self.add_spell('Fire', 2)
            self.add_spell('Ice', 2)
            self.add_spell('Lightning', 2)
        elif level == 2:
            self.add_spell('Fire', 3)
            self.add_spell('Ice', 2)
            self.add_spell('Lightning', 2)
            self.add_spell('Shield', 1)
        elif level == 3:
            self.add_spell('Fire', 3)
            self.add_spell('Ice', 2)
            self.add_spell('Lightning', 3)
            self.add_spell('Shield', 1)
        elif level == 4:
            self.add_spell('Fire', 3)
            self.add_spell('Ice', 3)
            self.add_spell('Lightning', 3)
            self.add_spell('Shield', 1)
            self.add_spell('Overkill', 1)
