# -*- coding: utf-8 -*-

class Message_text():
   
      
   

   def boss_item_iteraction_message(x):
      return '{0}\n{1}{2}{3}'.format(x, Characters.boss.icon, MyStrings.Text.plus.value, Drop.item.value)




   def miss_message(x):
      return '{0}{1}{2}%'.format(MyStrings.Text.miss_text.value, ' ' * 9, str(x))

   def black_stas_returnal_message():
      return '{0}\n{1}{2}{3}{4}'.format(MyStrings.Text.black_stas_returnal_text.value, Characters.player.icon, MyStrings.Text.minus.value, str(Characters.player.damage), MyStrings.Text.player_health.value)

   def stan_effect_message(pers):
      return '{0} {1}\n{2}'.format(pers, MyStrings.Text.stan_text.value, MyStrings.Text.stan.value)

   def player_critical_attack_message():
      return '{0}{1}{0}\n{2}{3}{4}'.format(MyStrings.Text.critical_chance.value, MyStrings.Text.critical_text.value, Characters.boss.icon, MyStrings.Text.minus.value, Fight.player_attack_damage, MyStrings.Text.boss_health.value)

   def player_attack_message():
      return '{0}{1}{2}{3}'.format(Characters.boss.icon, MyStrings.Text.minus.value, Fight.player_attack_damage, MyStrings.Text.boss_health.value)

   def lifesteal_message():
      indent = ' ' * 11 + str(Characters.player.lifesteal) + '%\n'
      return '{0}{1}{0}\n{2}{3}{4}{5}{6}'.format(MyStrings.Text.lifesteal.value, MyStrings.Text.lifesteal_text.value, indent, Characters.player.icon, MyStrings.Text.plus.value, Fight.player_attack_damage * Characters.player.lifesteal // 100, MyStrings.Text.player_health.value)

   def returnal_message():   
      indent = ' ' * 10 + str(Characters.boss.returnal_value) + '%\n'
      return '{0}{1}{0}\n{2}{3}{4}{5}{6}'.format(MyStrings.Text.returnal.value, MyStrings.Text.returnal_text.value, indent, Characters.player.icon, MyStrings.Text.minus.value, Fight.player_attack_damage * Characters.boss.returnal_value // 100, MyStrings.Text.player_health.value)

   def boss_critical_attack_message():
      return '{0}{1}{0}\n{2}{3}{4}'.format(MyStrings.Text.critical_chance.value, MyStrings.Text.critical_text.value, Characters.player.icon, MyStrings.Text.minus.value, Fight.boss_attack_damage, MyStrings.Text.player_health.value)

   def boss_attack_message():
      return '{0}{1}{2}{3}'.format(Characters.player.icon, MyStrings.Text.minus.value, Fight.boss_attack_damage, MyStrings.Text.player_health.value)

   def chaikovskii_ressurection_message():
      return '{0}\n{1}+{2}{3}'.format(MyStrings.Text.chaikovskii_ressurection_text.value, Characters.boss.icon, str(Characters.Player.ressurection_value), MyStrings.Text.boss_health.value)

   def boss_ressurection_message():
      return '{0}\n{1}+{2}{3}'.format(MyStrings.Text.ressurection_text.value, Characters.boss.icon, str(Characters.Player.ressurection_value), MyStrings.Text.boss_health.value)

   def char_ressurection_message():
      return '{0}\n{1}+{2}{3}'.format(MyStrings.Text.ressurection_text.value, Characters.player.icon, str(Characters.Player.ressurection_value), MyStrings.Text.player_health.value)

   def viv_end_skill_message():
      return '{0}\n{1}+{2}{3}'.format(MyStrings.Text.viv_end_skill_text.value, Characters.boss.icon, str(Characters.boss.viv_end_skill_damage_up), MyStrings.Text.damage.value)

   def kitty_stan_message():
      return '{0}\n{1}+{2}'.format(MyStrings.Text.kitty_stan_text.value, Characters.player.icon, MyStrings.Text.stan.value)

   def kitty_bleeding_message():
      return '{}\n{}-{}{}'.format(MyStrings.Text.kitty_bleeding_text.value, Characters.player.icon, str(Characters.boss.kitty_end_skill_damage), MyStrings.Text.player_health.value, MyStrings.Text.bleeding.value)
      
   def drunk_leha_boost_message():
      return '{0}\n{1}+{2}%{3} +{2}%{4}'.format(MyStrings.Text.drunk_leha_skill_text.value, Characters.boss.icon, str(Characters.boss.drunk_leha_end_skill_boost), MyStrings.Text.boss_health.value, MyStrings.Text.damage.value)
   
   def doc_leha_bleeding_message():
      return '{0}\n{1}-{2}{3}{4}'.format(MyStrings.Text.doc_leha_skill_text.value, Characters.player.icon, str(Characters.boss.doc_leha_end_skill_damage), MyStrings.Text.player_health.value, MyStrings.Text.bleeding.value)

   def mel_end_skill_message():
      return '{0}\n{1}-{2}{3}'.format(MyStrings.Text.mel_end_skill_text.value, Characters.player.icon, str(Characters.boss.mel_end_skill_damage), MyStrings.Text.player_health.value)
      
   def dron_end_skill_message():
      return '{0}\n{1}-{2}{3}'.format(MyStrings.Text.dron_skill_text.value, Characters.player.icon, str(Characters.boss.dron_end_skill_damage), MyStrings.Text.player_health.value)
      
   def glad_damage_skill_message():
      return '{0}\n{1}-{2}{3}'.format(MyStrings.Text.glad_damage_skill_text.value, Characters.player.icon, str(Characters.boss.glad_end_skill_damage), MyStrings.Text.player_health.value)
   
   def glad_health_up_skill_message():
      return '{0}\n{1}+{2}{3}'.format(MyStrings.Text.glad_health_up_skill_text.value, Characters.boss.icon, str(Characters.boss.glad_end_skill_health_up), MyStrings.Text.boss_health.value)

   def glad_critical_up_skill_message():
      return '{0}\n{1}+{2}%{3}'.format(MyStrings.Text.glad_critical_up_skill_text.value, Characters.boss.icon, str(Characters.boss.glad_end_skill_critical_up), MyStrings.Text.critical_chance.value)

   def glad_damage_down_skill_message():
      return '{0}\n{1}-{2}{3}'.format(MyStrings.Text.glad_damage_down_skill_text.value, Characters.player.icon, str(Characters.boss.glad_damage_down_skill_value), MyStrings.Text.damage.value)

   def glad_poison_skill_message():
      return '{0}\n{1}+{2}'.format(MyStrings.Text.glad_poison_skill_text.value, Characters.player.icon, MyStrings.Text.poison.value)

   def shiva_critical_skill_message():
      return '{0}\n{1}+{2}%{3}'.format(MyStrings.Text.shiva_critical_up_skill_text.value, Characters.boss.icon, str(Characters.boss.shiva_end_skill_critical_up), MyStrings.Text.critical_chance.value)

   def shiva_damage_up_skill_message():
      return '{0}\n{1}+{2}%{3}'.format(MyStrings.Text.shiva_damage_up_skill_text.value, Characters.boss.icon, str(Characters.boss.shiva_end_skill_damage_up), MyStrings.Text.damage.value)

   def bleeding_message(pers_icon, pers_health_icon):
      return '{0}\n{1}-{2}{3}'.format(MyStrings.Text.bleeding_text.value, pers_icon, str(Characters.Pers.bleeding_damage), pers_health_icon)

   def poison_message(pers_icon, pers_health_icon):
      return '{0}\n{1}-{2}%{3}'.format(MyStrings.Text.poison_text.value, pers_icon, str(Characters.Pers.poison_damage), pers_health_icon)

   def regeneration_message(pers_icon, pers_health_icon):
      return '{0}\n{1}+{2}{3}'.format(MyStrings.Text.regeneration_text.value, pers_icon, str(Characters.Pers.regeneration_value), pers_health_icon)

   def sanya_skill_message():
      return '{0}-{1}{2}'.format(Characters.boss.icon, str(Fight.sanya_skill_damage), MyStrings.Text.sanya_skill_effect_text.value)

   def temich_skill_stan_message():
      return '{0}\n{1}+{2}'.format(MyStrings.Text.temich_skill_deffect_text.value, Characters.player.icon, MyStrings.Text.stan.value)
