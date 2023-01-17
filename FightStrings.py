import CharactersGenerator
import FightCycle
import FightFunctions
import BossStrings
import GameStrings

class Banners():
   # баннеры с описанием эффекта
   
   def miss(pers):
      # уклонение
      # если False - сообщение об увороте для босса
      if pers == False:
         if CharactersGenerator.boss.name == BossStrings.Mel.name:
            intro = BossStrings.Mel.miss
         elif CharactersGenerator.boss.name == BossStrings.BlackStas.name:
            intro = BossStrings.BlackStas.miss
         else:
            intro = 'Босс пропустил твой урон'
         return '{0}\n{1}{2}{3}%{1}'.format(intro, GameStrings.Icons.miss, 'Уворотка', 
                                             CharactersGenerator.boss.miss_chance)

      # если True - сообщение об увороте для игрока
      elif pers == True:
         intro = CharactersGenerator.player.name + 'скользский тип'
         return '{0}\n{1}{2}{3}%{1}'.format(intro, GameStrings.Icons.miss, 'Уворотка', 
                                             CharactersGenerator.player.miss_chance)

   def stan(pers_name):
      # оглушение
      return '{0} {1}\n{2}{3}{2}'.format(pers_name, GameStrings.Text.stan, 
                                          GameStrings.Icons.stan, 'Оглушение')                                             


   def returnal(pers):
      # обратка босса
      if pers == False:
         return '{0}{1}{0}\n{2}-{3}{4}'.format(GameStrings.Icons.returnal, 
                                                GameStrings.Text.returnal_banner, 
                                                CharactersGenerator.player.icon, 
                                                FightFunctions.returnal_damage, 
                                                GameStrings.Icons.player_health)

   
   def critical_attack(pers):
      # критическая атака игрока
      if pers == True:
         return '{0}{1}{0}\n{2}-{3}{4}'.format(GameStrings.Icons.critical_chance, 
                                                GameStrings.Text.critical_banner, 
                                                CharactersGenerator.boss.icon, 
                                                FightCycle.player_attack_damage, 
                                                GameStrings.Icons.boss_health)
      # критическая атака босса                                                
      elif pers == False:
         return '{0}{1}{0}\n{2}-{3}{4}'.format(GameStrings.Icons.critical_chance, 
                                                GameStrings.Text.critical_banner, 
                                                CharactersGenerator.player.icon, 
                                                FightCycle.boss_attack_damage, 
                                                GameStrings.Icons.player_health)

   
   def lifesteal():
      # вампиризм игрока
      return '{0}{1}{0}\n{2}+{3}{4}'.format(GameStrings.Icons.lifesteal, 
                                                GameStrings.Text.lifesteal_banner, 
                                                CharactersGenerator.player.icon, 
                                                FightFunctions.lifesteal_heal, 
                                                GameStrings.Icons.player_health)
                                                

class Message_text():
   
      
   

   def boss_item_iteraction_message(x):
      return '{0}\n{1}{2}{3}'.format(x, Characters.boss.icon, GameStrings.Text.plus, Drop.item)






  
  
   def chaikovskii_ressurection_message():
      return '{0}\n{1}+{2}{3}'.format(GameStrings.Text.chaikovskii_ressurection_text, Characters.boss.icon, str(Characters.Player.ressurection), GameStrings.Text.boss_health)

   def boss_ressurection_message():
      return '{0}\n{1}+{2}{3}'.format(GameStrings.Text.ressurection_text, Characters.boss.icon, str(Characters.Player.ressurection), GameStrings.Text.boss_health)

   def char_ressurection_message():
      return '{0}\n{1}+{2}{3}'.format(GameStrings.Text.ressurection_text, Characters.player.icon, str(Characters.Player.ressurection), GameStrings.Text.player_health)

   def viv_end_skill_message():
      return '{0}\n{1}+{2}{3}'.format(GameStrings.Text.viv_end_skill_text, Characters.boss.icon, str(Characters.boss.viv_end_skill_damage_up), GameStrings.Text.damage)

   def kitty_stan_message():
      return '{0}\n{1}+{2}'.format(GameStrings.Text.kitty_stan_text, Characters.player.icon, GameStrings.Text.stan)

   def kitty_bleeding_message():
      return '{}\n{}-{}{}'.format(GameStrings.Text.kitty_bleeding_text, Characters.player.icon, str(Characters.boss.kitty_end_skill_damage), GameStrings.Text.player_health, GameStrings.Text.bleeding)
      
   def drunk_leha_boost_message():
      return '{0}\n{1}+{2}%{3} +{2}%{4}'.format(GameStrings.Text.drunk_leha_skill_text, Characters.boss.icon, str(Characters.boss.drunk_leha_end_skill_boost), GameStrings.Text.boss_health, GameStrings.Text.damage)
   
   def doc_leha_bleeding_message():
      return '{0}\n{1}-{2}{3}{4}'.format(GameStrings.Text.doc_leha_skill_text, Characters.player.icon, str(Characters.boss.doc_leha_end_skill_damage), GameStrings.Text.player_health, GameStrings.Text.bleeding)

   def mel_end_skill_message():
      return '{0}\n{1}-{2}{3}'.format(GameStrings.Text.mel_end_skill_text, Characters.player.icon, str(Characters.boss.mel_end_skill_damage), GameStrings.Text.player_health)
      
   def dron_end_skill_message():
      return '{0}\n{1}-{2}{3}'.format(GameStrings.Text.dron_skill_text, Characters.player.icon, str(Characters.boss.dron_end_skill_damage), GameStrings.Text.player_health)
      
   def glad_damage_skill_message():
      return '{0}\n{1}-{2}{3}'.format(GameStrings.Text.glad_damage_skill_text, Characters.player.icon, str(Characters.boss.glad_end_skill_damage), GameStrings.Text.player_health)
   
   def glad_health_up_skill_message():
      return '{0}\n{1}+{2}{3}'.format(GameStrings.Text.glad_health_up_skill_text, Characters.boss.icon, str(Characters.boss.glad_end_skill_health_up), GameStrings.Text.boss_health)

   def glad_critical_up_skill_message():
      return '{0}\n{1}+{2}%{3}'.format(GameStrings.Text.glad_critical_up_skill_text, Characters.boss.icon, str(Characters.boss.glad_end_skill_critical_up), GameStrings.Text.critical_chance)

   def glad_damage_down_skill_message():
      return '{0}\n{1}-{2}{3}'.format(GameStrings.Text.glad_damage_down_skill_text, Characters.player.icon, str(Characters.boss.glad_damage_down_skill), GameStrings.Text.damage)

   def glad_poison_skill_message():
      return '{0}\n{1}+{2}'.format(GameStrings.Text.glad_poison_skill_text, Characters.player.icon, GameStrings.Text.poison)

   def shiva_critical_skill_message():
      return '{0}\n{1}+{2}%{3}'.format(GameStrings.Text.shiva_critical_up_skill_text, Characters.boss.icon, str(Characters.boss.shiva_end_skill_critical_up), GameStrings.Text.critical_chance)

   def shiva_damage_up_skill_message():
      return '{0}\n{1}+{2}%{3}'.format(GameStrings.Text.shiva_damage_up_skill_text, Characters.boss.icon, str(Characters.boss.shiva_end_skill_damage_up), GameStrings.Text.damage)

   def bleeding_message(pers_icon, pers_health_icon):
      return '{0}\n{1}-{2}{3}'.format(GameStrings.Text.bleeding_text, pers_icon, str(Characters.Pers.bleeding_damage), pers_health_icon)

   def poison_message(pers_icon, pers_health_icon):
      return '{0}\n{1}-{2}%{3}'.format(GameStrings.Text.poison_text, pers_icon, str(Characters.Pers.poison_damage), pers_health_icon)

   def regeneration_message(pers_icon, pers_health_icon):
      return '{0}\n{1}+{2}{3}'.format(GameStrings.Text.regeneration_text, pers_icon, str(Characters.Pers.regeneration), pers_health_icon)

   def sanya_skill_message():
      return '{0}-{1}{2}'.format(Characters.boss.icon, str(Fight.sanya_skill_damage), GameStrings.Text.sanya_skill_effect_text)

   def temich_skill_stan_message():
      return '{0}\n{1}+{2}'.format(GameStrings.Text.temich_skill_deffect_text, Characters.player.icon, GameStrings.Text.stan)
