# -*- coding: utf-8 -*-
import Characters
import MyStrings
import Locations
import Drop

class Message_text():
   def char_description_message():
      return '{0}{1}\n{2}'.format(Characters.char.name, Characters.char.icon, Characters.char.description)

   def char_stats_message():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}{7}'.format(Characters.char.name, Characters.char.icon, MyStrings.Text.health_icon.value, str(Characters.char.health), MyStrings.Text.damage_icon.value, str(Characters.char.damage), MyStrings.Text.critical_chance_icon.value, str(Characters.char.critical_chance))
   
   def boss_stats_message():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}{7}'.format(Characters.boss.name, Characters.boss.icon, MyStrings.Text.health_icon.value, str(Characters.boss.health), MyStrings.Text.damage_icon.value, str(Characters.boss.damage), MyStrings.Text.critical_chance_icon.value, str(Characters.boss.critical_chance))
      
   def location_description_message():
      return '{0}{1}\n{2}'.format(Locations.loc.name, Locations.loc.icon, Locations.loc.description)

   def boss_item_iteraction_message(x):
      return '{0}\n{1}{2}{3}'.format(x, Characters.boss.icon, MyStrings.Text.plus.value, Drop.item.value)

   def default_item_text(description, pers_icon, symbol, value, stats_icon):
      return '{0}{1}{2}{3}{4}'.format(description, pers_icon, symbol, value, stats_icon)