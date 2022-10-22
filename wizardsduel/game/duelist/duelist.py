
import constants

class Duelist:
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

    def __init__(self):
        """Constructs a new Duelist."""
        self._spell_dict = {}
        for spell in constants.spell_list:
            self._spell_dict[spell] = 0
        self._lives_left:2
        self._rounds_won:0

    def cast_spell(self, spell):
        casted = self._spell_dict[spell] > 0
        if casted:
            self._spell_dict[spell] -= 1
        return casted

    def setup_duelist(self):
        pass

    def add_spell(self, type, uses):
        self._spell_dict[type] = uses 

    def avail_spells(self):
        spells = self._spell_dict
        result = {}

        for spell in spells:
            uses = spells[spell]
            if uses > 0:
                result[spell] = uses
        return result

    def print_spells(self, spells):
        index = 1
        uses = 0
        for spell in spells:
            uses = spells[spell]
            print(f'[ {index} ]: {spell} x{uses}')
            index += 1


    def take_damage(self):
        self._lives_left -= 1

    def get_life(self):
        return self._lives_left