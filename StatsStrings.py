import CharactersGenerator
import FightCycle
import GameStrings

def player_stats():
   # текущие характеристики игрока
   return '''{0}{1}\n{2}{3}\n
               {4}{5}\n{6}{7}'''.format(CharactersGenerator.player.name, CharactersGenerator.player.icon, 
                                       GameStrings.Icons.player_health, CharactersGenerator.player.health, 
                                       GameStrings.Icons.damage, CharactersGenerator.player.damage, 
                                       GameStrings.Icons.critical_chance, CharactersGenerator.player.critical_chance)
   

def boss_stats():
   # текущие характеристики босса
   return '''{0}{1}\n{2}{3}\n
               {4}{5}\n{6}{7}'''.format(CharactersGenerator.boss.name, CharactersGenerator.boss.icon, 
                                       GameStrings.Icons.boss_health, CharactersGenerator.boss.health, 
                                       GameStrings.Icons.damage, CharactersGenerator.boss.damage, 
                                       GameStrings.Icons.critical_chance, CharactersGenerator.boss.critical_chance)


def versus_stats(player_name, boss_name):
   # текущие характеристики игрока и босса,
   # в одном сообщении в бою
   str1 = CharactersGenerator.player.icon + player_name + \
         ' 🆚 ' + boss_name + CharactersGenerator.boss.icon
   str2 = '❤️' + str(CharactersGenerator.player.health)
   str3 = '🖤' + str(CharactersGenerator.boss.health)
   str4 = '⚔️' + str(CharactersGenerator.player.damage)
   str5 = '⚔️' + str(CharactersGenerator.boss.damage)
   z = len(str2) - len(str3)
   indent1 = ' ' * 8
   indent2 = ' ' * (8 + z)
   return '{0}\n{1}{2}{3}\n{4}{5}{6}'.format(str1, str2, indent1, str3, str4, indent2, str5)    


def attack(pers):
   if pers == True:
      # игрок наносит урон боссу
      return '{0}-{1}{2}'.format(CharactersGenerator.boss.icon, 
                                 FightCycle.player_attack_damage, 
                                 GameStrings.Icons.boss_health)

   elif pers == False:
      # босс наносит урон игроку
      return '{0}-{1}{2}'.format(CharactersGenerator.player.icon, 
                              FightCycle.boss_attack_damage, 
                              GameStrings.Icons.player_health)
