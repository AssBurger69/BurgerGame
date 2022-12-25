# -*- coding: utf-8 -*-
import Characters
import MyStrings
import Locations
import Drop

class Message_text():
   def char_description_message():
      return '{0}{1}\n{2}'.format(Characters.char.name, Characters.char.icon, Characters.char.description)

   def char_stats_message():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}{7}'.format(Characters.char.name, Characters.char.icon, MyStrings.Text.char_health_icon.value, str(Characters.char.health), MyStrings.Text.damage_icon.value, str(Characters.char.damage), MyStrings.Text.critical_chance_icon.value, str(Characters.char.critical_chance))
   
   def boss_stats_message():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}{7}'.format(Characters.boss.name, Characters.boss.icon, MyStrings.Text.boss_health_icon.value, str(Characters.boss.health), MyStrings.Text.damage_icon.value, str(Characters.boss.damage), MyStrings.Text.critical_chance_icon.value, str(Characters.boss.critical_chance))
      
   def location_description_message():
      return '{0}{1}\n{2}'.format(Locations.loc.name, Locations.loc.icon, Locations.loc.description)

   def boss_item_iteraction_message(x):
      return '{0}\n{1}{2}{3}'.format(x, Characters.boss.icon, MyStrings.Text.plus.value, Drop.item.value)

   def boss_skill_meter_message(x):
      if x == MyStrings.Text.sledovatel_name.value:
         return '{0}{1} {2}%{0}'.format(MyStrings.Text.chains_icon.value, MyStrings.Text.sledovatel_skill_meter_text.value, Characters.char.busted_level)
      elif x == MyStrings.Text.dron_name.value:
         return '{0}{1} {2}%{0}'.format(MyStrings.Text.obida_icon.value, MyStrings.Text.dron_skill_meter_text.value, Characters.boss.obida_level)

   def versus_stats(x, y):
      str1 = Characters.char.icon + x + ' 🆚 ' + y + Characters.boss.icon
      str2 = '❤️' + str(Characters.char.health)
      str3 = '🖤' + str(Characters.boss.health)
      str4 = '⚔️' + str(Characters.char.damage)
      str5 = '⚔️' + str(Characters.boss.damage)
      z = len(str2) - len(str3)
      indent1 = ' ' * 8
      indent2 = ' ' * (8 + z)
      return '{0}\n{1}{2}{3}\n{4}{5}{6}'.format(str1, str2, indent1, str3, str4, indent2, str5)

   def miss_text_indent(x):
      return ' ' * 9 + str(x) + '%'

   def black_stas_returnal_message():
      return '{0}\n{1}{2}{3}{4}'.format(MyStrings.Text.black_stas_returnal_text.value, Characters.char.icon, MyStrings.Text.minus.value, str(Characters.char.damage), MyStrings.Text.char_health_icon.value)

   def stan_effect_message(x):
      return '{0} {1}\n{2}'.format(x, MyStrings.Text.stan_text.value, MyStrings.Text.stan_icon.value)