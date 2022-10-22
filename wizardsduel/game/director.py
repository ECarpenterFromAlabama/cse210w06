import imp
import random
from game.terminal_service import TerminalService
from game.duelist.player import Player
from game.duelist.enemy import Enemy
from game.handle_combat import HandleCombat
from constants import DEFEAT_MSG, VIC_MSG, spell_list, RETRY_MSG


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        player (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self.level = 1
        self.terminal_service = TerminalService()
        self.combat = HandleCombat()
        self.player_wizard = Player()
        self.enemy_types = ['red', 'blue', 'white', 'black']
        self.enemy_wizards = []
        for type in self.enemy_types:
            self.enemy_wizards.append(Enemy(type))
        self.current_enemy = self.enemy_wizards[self.level-1]

        self.start_round = True
        self.player_choice = 'Fire'
        self.enemy_choice = ''

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """

        self.round_start()
        player_spells = self.player_wizard.avail_spells()
        self.terminal_service.write_text('Please choose the spell you will use:')
        self.player_wizard.print_spells(player_spells)
        self.terminal_service.write_text(f'Your current life: {self.player_wizard.get_life()}')
        self.terminal_service.write_text(f'Your opponent\'s life: {self.current_enemy.get_life()}')
        casted = False
        while(not casted):
            prompt = 'Pick the spell by typing its corresponding menu number:'
            try:
                number_choice = self.terminal_service.read_number(prompt)-1
                spells_list = list(player_spells.keys())
                self.player_choice = spells_list[number_choice]
                casted = self.player_wizard.cast_spell(self.player_choice)
            except:
                pass         
            
            if (not casted):
                self.terminal_service.write_text(RETRY_MSG)

        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        self.combat.do_combat(self.current_enemy, self.player_wizard, self.player_choice)
        

        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        if(self.player_wizard.get_life() == 0):
            self.terminal_service.write_text(DEFEAT_MSG)
            self._is_playing = False
        elif(self.current_enemy.get_life() == 0):
            self.terminal_service.write_text(VIC_MSG)
            self.level += 1
            self.player_wizard.level_up()
            self.start_round = True
            if(self.level > 4):
                self.terminal_service.write_text('Congratulations! You are the strongest wizard!')
                self._is_playing = False


    def round_start(self):
        opponent = self.enemy_types[self.level-1]
        if self.start_round:
            self.terminal_service.write_text(f'The {opponent} wizard approaches.')
            self.player_wizard.setup_duelist()
            self.current_enemy = self.enemy_wizards[self.level-1]
            self.start_round = False