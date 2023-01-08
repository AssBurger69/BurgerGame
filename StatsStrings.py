import CharactersGenerator
import GameStrings

def player_stats_message():
   return '{0}{1}\n{2}{3}\n{4}{5}\n{6}{7}'.format(CharactersGenerator.player.name, CharactersGenerator.player.icon, 
                                                   GameStrings.Icons.player_health, CharactersGenerator.player.health, 
                                                   GameStrings.Icons.damage, CharactersGenerator.player.damage, 
                                                   GameStrings.Icons.critical_chance, CharactersGenerator.player.critical_chance)
   
def boss_stats_message():
   return '{0}{1}\n{2}{3}\n{4}{5}\n{6}{7}'.format(CharactersGenerator.boss.name, CharactersGenerator.boss.icon, 
                                                   GameStrings.Icons.boss_health, CharactersGenerator.boss.health, 
                                                   GameStrings.Icons.damage, CharactersGenerator.boss.damage, 
                                                   GameStrings.Icons.critical_chance, CharactersGenerator.boss.critical_chance)
