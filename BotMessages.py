# -*- coding: utf-8 -*-
import Characters
import MyStrings

class Message_text():
   def char_description_message():
      return '{0}{1}\n{2}'.format(Characters.char.name, Characters.char.icon, Characters.char.description)

   def char_stats_message():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}{7}'.format(Characters.char.name, Characters.char.icon, MyStrings.Text.health_icon.value, str(Characters.char.health), MyStrings.Text.damage_icon.value, str(Characters.char.damage), MyStrings.Text.critical_chance_icon.value, str(Characters.char.critical_chance))
   
   def boss_stats_message():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}{7}'.format(Characters.boss.name, Characters.boss.icon, MyStrings.Text.health_icon.value, str(Characters.boss.health), MyStrings.Text.damage_icon.value, str(Characters.boss.damage), MyStrings.Text.critical_chance_icon.value, str(Characters.boss.critical_chance))
      