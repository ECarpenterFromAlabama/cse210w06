from game.duelist.enemy import Enemy
from game.duelist.player import Player
from constants import spell_list
import random

from game.terminal_service import TerminalService

class HandleCombat:

    def __init__(self):
        self.terminal = TerminalService()

    def get_enemy_spell(self, duelist):
        select_spell = random.choice(spell_list)
        casted = duelist.cast_spell(select_spell)
        while(not casted):
            select_spell = random.choice(spell_list)
            casted = duelist.cast_spell(select_spell)
        return select_spell
    
    def compare_combat(self, enemy_spell, player_spell):
        """
        There are three results, player win(1), enemy win(2) and tie(0).
        """
        player_win = -1
        enemy_victory = \
            enemy_spell is 'Overkill' and player_spell is not 'Shield' or \
            enemy_spell is 'Fire' and player_spell is 'Ice' or \
            enemy_spell is 'Ice' and player_spell is 'Lightning' or \
            enemy_spell is 'Lightning' and player_spell is 'Fire'
        tie = \
            player_spell is 'Shield' or \
            enemy_spell is 'Shield' or \
            enemy_spell == player_spell

        if enemy_victory:
            player_win = 2
        elif tie:
            player_win = 0
        else:
            player_win = 1

        return player_win

    def do_combat(self, enemy, player, player_spell):
        enemy_spell = self.get_enemy_spell(enemy)
        self.terminal.write_text('|==============| COMBAT |==============|')
        self.terminal.write_text(f'You cast {player_spell} and your enemy invoked {enemy_spell}')
        decision = self.compare_combat(enemy_spell, player_spell)
        if decision == 0:
            self.terminal.write_text('What a fight! Your power is equal!\nTie!\n')
        elif decision == 1:
            enemy.take_damage()
            self.terminal.write_text('The enemy couldn\'t avoid the attack!\nPlayer win!\n')
        else:
            player.take_damage()
            self.terminal.write_text('You tried hard but were overpowered!\nEnemy win!\n')


