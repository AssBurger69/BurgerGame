import CharactersGenerator
import Characters
import FightCycle
import FightFunctions
import InteractionParameters
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
      return '{0} {1}\n{2}{3}{2}'.format(pers_name, GameStrings.Text.stan_banner, 
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

   def ressurection(pers):
      # воскрешение игрока
      if pers == True:
         return '{0}{1}{0}\n{2}+{3}{4}'.format(GameStrings.Icons.ressurection, 
                                                GameStrings.Text.ressurection_banner,
                                                CharactersGenerator.player.icon,
                                                Characters.Pers.ressurection_value,
                                                GameStrings.Icons.player_health)

      # воскрешение босса
      elif pers == False:
         # особое воскрешение босса Чайковский
         if CharactersGenerator.boss.name == BossStrings.Chaikovskii.name:
            return '{0}{1}{0}\n{2}+{3}{4}'.format(GameStrings.Icons.ressurection, 
                                                   BossStrings.Chaikovskii.ressurection,
                                                   CharactersGenerator.boss.icon,
                                                   Characters.Pers.ressurection_value,
                                                   GameStrings.Icons.boss_health)

         # для всех остальных боссов                                                   
         else:
            return '{0}{1}{0}\n{2}+{3}{4}'.format(GameStrings.Icons.ressurection, 
                                                   GameStrings.Text.ressurection_banner,
                                                   CharactersGenerator.boss.icon,
                                                   Characters.Pers.ressurection_value,
                                                   GameStrings.Icons.boss_health)
   def bleeding(pers):
      # кровотечение игрока
      if pers == True:
         return '{0}{1}{0}\n{2}-{3}{4}'.format(GameStrings.Icons.bleeding, 
                                                GameStrings.Text.bleeding_banner, 
                                                CharactersGenerator.player.icon,
                                                Characters.Pers.regeneration_value,
                                                GameStrings.Icons.player_health)

      # кровотечение босса                                                
      elif pers == False:
         return '{0}{1}{0}\n{2}-{3}{4}'.format(GameStrings.Icons.bleeding, 
                                                GameStrings.Text.bleeding_banner, 
                                                CharactersGenerator.boss.icon,
                                                Characters.Pers.regeneration_value,
                                                GameStrings.Icons.boss_health)                                 

   def poison(pers):
      if pers == True:
      # отравление игрока
         return '{0}{1}{0}\n{2}-{3}%{4}'.format(GameStrings.Icons.poison,
                                                GameStrings.Text.poison_banner,
                                                CharactersGenerator.player.icon,
                                                Characters.Pers.poison_damage, 
                                                GameStrings.Icons.player_health)
      elif pers == False:                                                
         # отравление босса
         return '{0}{1}{0}\n{2}-{3}%{4}'.format(GameStrings.Icons.poison,
                                                GameStrings.Text.poison_banner,
                                                CharactersGenerator.boss.icon,
                                                Characters.Pers.poison_damage, 
                                                GameStrings.Icons.boss_health)                                             

   def regeneration(pers):
      # регенерация игрока
      if pers == True:
         return '{0}{1}{0}\n{1}+{2}{3}'.format(GameStrings.Icons.regeneration, 
                                                GameStrings.Text.regeneration_banner, 
                                                CharactersGenerator.player.icon,
                                                Characters.Pers.regeneration_value,
                                                GameStrings.Icons.player_health)

      # регенерация босса
      elif pers == False:
         return '{0}{1}{0}\n{1}+{2}{3}'.format(GameStrings.Icons.regeneration, 
                                                GameStrings.Text.regeneration_banner, 
                                                CharactersGenerator.boss.icon,
                                                Characters.Pers.regeneration_value,
                                                GameStrings.Icons.boss_health)                                                                                                 

class BossMessages():

   def viv_end_skill():
      return '{0}\n{1}+{2}{3}'.format(BossStrings.Viv.end_skill, 
                                       CharactersGenerator.boss.icon, 
                                       CharactersGenerator.boss.viv_end_skill_damage_up, 
                                       GameStrings.Icons.damage)

   def kitty_stan():
      return '{0}\n{1}+{2}'.format(BossStrings.Kitty.stan_skill, 
                                    CharactersGenerator.player.icon, 
                                    GameStrings.Icons.stan)

   def kitty_bleeding():
      return '{0}\n{1}-{2}{3}'.format(BossStrings.Kitty.bleeding_skill, 
                                       CharactersGenerator.player.icon, 
                                       CharactersGenerator.boss.kitty_end_skill_damage, 
                                       GameStrings.Icons.player_health, GameStrings.Icons.bleeding)
      
   def drunk_leha_boost():
      return '{0}\n{1}+{2}%{3} +{2}%{4}'.format(BossStrings.DrunkLeha.end_skill, 
                                                CharactersGenerator.boss.icon, 
                                                CharactersGenerator.boss.drunk_leha_end_skill_boost, 
                                                GameStrings.Icons.boss_health, 
                                                GameStrings.Icons.damage)
   
   def doc_leha_bleeding():
      return '{0}\n{1}-{2}{3}{4}'.format(BossStrings.DocLeha.end_skill, 
                                          CharactersGenerator.player.icon, 
                                          CharactersGenerator.boss.doc_leha_end_skill_damage, 
                                          GameStrings.Icons.player_health, 
                                          GameStrings.Icons.bleeding)

   def mel_end_skill():
      return '{0}\n{1}-{2}{3}'.format(BossStrings.Mel.end_skill, 
                                       CharactersGenerator.player.icon, 
                                       CharactersGenerator.boss.mel_end_skill_damage, 
                                       GameStrings.Icons.player_health)
      
   def dron_end_skill():
      return '{0}\n{1}-{2}{3}'.format(BossStrings.Dron.end_skill, 
                                       CharactersGenerator.player.icon, 
                                       CharactersGenerator.boss.dron_end_skill_damage, 
                                       GameStrings.Icons.player_health)
      
   def glad_damage_skill():
      return '{0}\n{1}-{2}{3}'.format(BossStrings.Glad.damage_skill, 
                                       CharactersGenerator.player.icon, 
                                       CharactersGenerator.boss.glad_end_skill_damage, 
                                       GameStrings.Icons.player_health)
   
   def glad_health_up_skill():
      return '{0}\n{1}+{2}{3}'.format(BossStrings.Glad.health_up_skill, 
                                       CharactersGenerator.boss.icon, 
                                       CharactersGenerator.boss.glad_end_skill_health_up, 
                                       GameStrings.Icons.boss_health)

   def glad_critical_up_skill():
      return '{0}\n{1}+{2}%{3}'.format(BossStrings.Glad.critical_up_skill, 
                                       CharactersGenerator.boss.icon, 
                                       CharactersGenerator.boss.glad_end_skill_critical_up, 
                                       GameStrings.Icons.critical_chance)

   def glad_damage_down_skill():
      return '{0}\n{1}-{2}{3}'.format(BossStrings.Glad.damage_down_skill, 
                                       CharactersGenerator.player.icon, 
                                       CharactersGenerator.boss.glad_end_skill_damage_down, 
                                       GameStrings.Icons.damage)

   def glad_poison_skill():
      return '{0}\n{1}+{2}'.format(BossStrings.Glad.poison_skill, 
                                    CharactersGenerator.player.icon, 
                                    GameStrings.Icons.poison)

   def shiva_critical_skill():
      return '{0}\n{1}+{2}%{3}'.format(BossStrings.Shiva.critical_up_skill, 
                                       CharactersGenerator.boss.icon, 
                                       CharactersGenerator.boss.shiva_end_skill_critical_up, 
                                       GameStrings.Icons.critical_chance)

   def shiva_damage_up_skill():
      return '{0}\n{1}+{2}%{3}'.format(BossStrings.Shiva.damage_up_skill, 
                                       CharactersGenerator.boss.icon, 
                                       CharactersGenerator.boss.shiva_end_skill_damage_up, 
                                       GameStrings.Icons.damage)

   def sasha_victory():
      return '{0}\n+{1}%{2}\n+{3}%{4}\n+{5}%{6}'.format(BossStrings.Sasha.victory_fight,
                                                         InteractionParameters.Boss.sanya_sasha_health_up,
                                                         InteractionParameters.Boss.sanya_sasha_damage_up,
                                                         InteractionParameters.Boss.sanya_sasha_critical_up)                                       

   def sasha_skill_message():
      return '{0}-{1}{2}'.format(Characters.boss.icon, str(Fight.sanya_skill_damage), GameStrings.Text.sanya_skill_effect_text)


   def temich_skill_stan_message():
      return '{0}\n{1}+{2}'.format(GameStrings.Text.temich_skill_deffect_text, Characters.player.icon, GameStrings.Text.stan_banner)
