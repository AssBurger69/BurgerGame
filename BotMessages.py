# -*- coding: utf-8 -*-
import Characters
import MyStrings
import Locations
import Drop
import Fight

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

   def boss_skill_meter_message(boss_name):
      if boss_name == MyStrings.Text.sledovatel_name.value:
         return '{0}{1} {2}%{0}'.format(MyStrings.Text.chains_icon.value, MyStrings.Text.sledovatel_skill_meter_text.value, Characters.char.busted_level)
      elif boss_name == MyStrings.Text.dron_name.value:
         return '{0}{1} {2}%{0}'.format(MyStrings.Text.obida_icon.value, MyStrings.Text.dron_skill_meter_text.value, Characters.boss.dron_obida_level)

   def versus_stats(char_name, boss_name):
      str1 = Characters.char.icon + char_name + ' 🆚 ' + boss_name + Characters.boss.icon
      str2 = '❤️' + str(Characters.char.health)
      str3 = '🖤' + str(Characters.boss.health)
      str4 = '⚔️' + str(Characters.char.damage)
      str5 = '⚔️' + str(Characters.boss.damage)
      z = len(str2) - len(str3)
      indent1 = ' ' * 8
      indent2 = ' ' * (8 + z)
      return '{0}\n{1}{2}{3}\n{4}{5}{6}'.format(str1, str2, indent1, str3, str4, indent2, str5)

   def miss_message(x):
      return '{0}{1}{2}%'.format(MyStrings.Text.miss_text.value, ' ' * 9, str(x))

   def black_stas_returnal_message():
      return '{0}\n{1}{2}{3}{4}'.format(MyStrings.Text.black_stas_returnal_text.value, Characters.char.icon, MyStrings.Text.minus.value, str(Characters.char.damage), MyStrings.Text.char_health_icon.value)

   def stan_effect_message(pers):
      return '{0} {1}\n{2}'.format(pers, MyStrings.Text.stan_text.value, MyStrings.Text.stan_icon.value)

   def char_critical_attack_message():
      return '{0}{1}{0}\n{2}{3}{4}'.format(MyStrings.Text.critical_chance_icon.value, MyStrings.Text.critical_text.value, Characters.boss.icon, MyStrings.Text.minus.value, Fight.char_attack_damage, MyStrings.Text.boss_health_icon.value)

   def char_attack_message():
      return '{0}{1}{2}{3}'.format(Characters.boss.icon, MyStrings.Text.minus.value, Fight.char_attack_damage, MyStrings.Text.boss_health_icon.value)

   def lifesteal_message():
      indent = ' ' * 11 + str(Characters.char.lifesteal) + '%\n'
      return '{0}{1}{0}\n{2}{3}{4}{5}{6}'.format(MyStrings.Text.lifesteal_icon.value, MyStrings.Text.lifesteal_text.value, indent, Characters.char.icon, MyStrings.Text.plus.value, Fight.char_attack_damage * Characters.char.lifesteal // 100, MyStrings.Text.char_health_icon.value)

   def returnal_message():   
      indent = ' ' * 10 + str(Characters.boss.returnal_value) + '%\n'
      return '{0}{1}{0}\n{2}{3}{4}{5}{6}'.format(MyStrings.Text.returnal_icon.value, MyStrings.Text.returnal_text.value, indent, Characters.char.icon, MyStrings.Text.minus.value, Fight.char_attack_damage * Characters.boss.returnal_value // 100, MyStrings.Text.char_health_icon.value)

   def boss_critical_attack_message():
      return '{0}{1}{0}\n{2}{3}{4}'.format(MyStrings.Text.critical_chance_icon.value, MyStrings.Text.critical_text.value, Characters.char.icon, MyStrings.Text.minus.value, Fight.boss_attack_damage, MyStrings.Text.char_health_icon.value)

   def boss_attack_message():
      return '{0}{1}{2}{3}'.format(Characters.char.icon, MyStrings.Text.minus.value, Fight.boss_attack_damage, MyStrings.Text.char_health_icon.value)

   def chaikovskii_ressurection_message():
      return '{0}\n{1}+{2}{3}'.format(MyStrings.Text.chaikovskii_ressurection_text.value, Characters.boss.icon, str(Characters.Char.ressurection_value), MyStrings.Text.boss_health_icon.value)

   def boss_ressurection_message():
      return '{0}\n{1}+{2}{3}'.format(MyStrings.Text.ressurection_text.value, Characters.boss.icon, str(Characters.Char.ressurection_value), MyStrings.Text.boss_health_icon.value)

   def char_ressurection_message():
      return '{0}\n{1}+{2}{3}'.format(MyStrings.Text.ressurection_text.value, Characters.char.icon, str(Characters.Char.ressurection_value), MyStrings.Text.char_health_icon.value)

   def viv_end_skill_message():
      return '{0}\n{1}+{2}{3}'.format(MyStrings.Text.viv_end_skill_text.value, Characters.boss.icon, str(Characters.boss.viv_damage_up_skill_value), MyStrings.Text.damage_icon.value)

   def kitty_stan_message():
      return '{0}\n{1}+{2}'.format(MyStrings.Text.kitty_stan_text.value, Characters.char.icon, MyStrings.Text.stan_icon.value)

   def kitty_bleeding_message():
      return '{}\n{}-{}{}'.format(MyStrings.Text.kitty_bleeding_text.value, Characters.char.icon, str(Characters.boss.kity_end_skill_damage), MyStrings.Text.char_health_icon.value, MyStrings.Text.bleeding_icon.value)
      
   def drunk_leha_boost_message():
      return '{0}\n{1}+{2}%{3} +{2}%{4}'.format(MyStrings.Text.drunk_leha_skill_text.value, Characters.boss.icon, str(Characters.boss.drunk_leha_boost_skill_value), MyStrings.Text.boss_health_icon.value, MyStrings.Text.damage_icon.value)
   
   def doc_leha_bleeding_message():
      return '{0}\n{1}-{2}{3}{4}'.format(MyStrings.Text.doc_leha_skill_text.value, Characters.char.icon, str(Characters.boss.doc_leha_end_skill_damage), MyStrings.Text.char_health_icon.value, MyStrings.Text.bleeding_icon.value)

   def mel_end_skill_message():
      return '{0}\n{1}-{2}{3}'.format(MyStrings.Text.mel_end_skill_text.value, Characters.char.icon, str(Characters.boss.mel_end_skill_damage), MyStrings.Text.char_health_icon.value)
      
   def dron_end_skill_message():
      return '{0}\n{1}-{2}{3}'.format(MyStrings.Text.dron_skill_text.value, Characters.char.icon, str(Characters.boss.dron_end_skill_damage), MyStrings.Text.char_health_icon.value)
      
   def glad_damage_skill_message():
      return '{0}\n{1}-{2}{3}'.format(MyStrings.Text.glad_damage_skill_text.value, Characters.char.icon, str(Characters.boss.glad_end_skill_damage), MyStrings.Text.char_health_icon.value)
   
   def glad_health_up_skill_message():
      return '{0}\n{1}+{2}{3}'.format(MyStrings.Text.glad_health_up_skill_text.value, Characters.boss.icon, str(Characters.boss.glad_health_up_skill_value), MyStrings.Text.boss_health_icon.value)

   def glad_critical_up_skill_message():
      return '{0}\n{1}+{2}%{3}'.format(MyStrings.Text.glad_critical_up_skill_text.value, Characters.boss.icon, str(Characters.boss.glad_critical_up_skill_value), MyStrings.Text.critical_chance_icon.value)

   def glad_damage_down_skill_message():
      return '{0}\n{1}-{2}{3}'.format(MyStrings.Text.glad_damage_down_skill_text.value, Characters.char.icon, str(Characters.boss.glad_damage_down_skill_value), MyStrings.Text.damage_icon.value)

   def glad_poison_skill_message():
      return '{0}\n{1}+{2}'.format(MyStrings.Text.glad_poison_skill_text.value, Characters.char.icon, MyStrings.Text.poison_icon.value)

   def shiva_critical_skill_message():
      return '{0}\n{1}+{2}%{3}'.format(MyStrings.Text.shiva_critical_up_skill_text.value, Characters.boss.icon, str(Characters.boss.shiva_critical_up_skill_value), MyStrings.Text.critical_chance_icon.value)

   def shiva_damage_up_skill_message():
      return '{0}\n{1}+{2}%{3}'.format(MyStrings.Text.shiva_damage_up_skill_text.value, Characters.boss.icon, str(Characters.boss.shiva_damage_up_skill_value), MyStrings.Text.damage_icon.value)

   def bleeding_message(pers_icon, pers_health_icon):
      return '{0}\n{1}-{2}{3}'.format(MyStrings.Text.bleeding_text.value, pers_icon, str(Characters.Pers.bleeding_damage), pers_health_icon)

   def poison_message(pers_icon, pers_health_icon):
      return '{0}\n{1}-{2}%{3}'.format(MyStrings.Text.poison_text.value, pers_icon, str(Characters.Pers.poison_damage), pers_health_icon)

   def regeneration_message(pers_icon, pers_health_icon):
      return '{0}\n{1}+{2}{3}'.format(MyStrings.Text.regeneration_text.value, pers_icon, str(Characters.Pers.regeneration_value), pers_health_icon)

   def sanya_skill_message():
      return '{0}-{1}{2}'.format(Characters.boss.icon, str(Fight.sanya_skill_damage), MyStrings.Text.sanya_skill_effect_text.value)

   def kolya_skill_message():
      return '{0}-{1}{2}\n{3}+{1}{2}\n{4}'.format(Characters.boss.icon, str(Fight.kolya_hack_damage_value), MyStrings.Text.damage_icon.value, Characters.char.icon, MyStrings.Text.kolya_skill_effect_text.value)

   def temich_skill_stan_message():
      return '{0}\n{1}+{2}'.format(MyStrings.Text.temich_skill_deffect_text.value, Characters.char.icon, MyStrings.Text.stan_icon.value)
