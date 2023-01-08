# модуль со строками относящимся к героям и игроку: имя, характеристики героя, описание способности при ее применениии

import Characters
import GameStrings
import Fight
import CharactersGenerator

class Mitya():
   name = 'Митя'

   def skill_effect():
      return '-{0}{1}\n+{2}{3}\n{4}{5}'.format(Characters.Player.mitya_health_down_skill_value, GameStrings.Icons.player_health, 
                                                Characters.Player.mitya_damage_up_skill_value, GameStrings.Icons.damage, 
                                                GameStrings.Icons.cooldown, Characters.player.cooldown)

   def description():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}\n{7}'.format(GameStrings.Icons.player_health, Characters.player.health,
                                                      GameStrings.Icons.damage, Characters.player.damage,
                                                      GameStrings.Icons.critical_chance, Characters.player.critical_chance,
                                                      'Мастер отсоса жизни',
                                                      'Любитель губительно-усиливающих эликсиров, будь с ними осторожен')
   
   def inkvisizia_interaction():
      return '{0}\n{1}%{2}'.format('Каждая конвульсия делает Митю крепче!', 
                                    Characters.Boss.inkvisizia_mitya_health_up, GameStrings.Icons.player_health)


class Sanya():
   name = 'Саня'

   def skill_effect():
      return '{0}-{1}{2}\n{3}{4}'.format(GameStrings.Icons.boss, Fight.sanya_skill_damage, 
                                          GameStrings.Icons.boss_health, GameStrings.Icons.cooldown, 
                                          Characters.player.cooldown)
   
   def sasha_interaction():
      return '{0}\n+{1}%{2}\n+{3}%{4}\n+{5}%{6}'.format('Победа над собой возвысила тебя!', 
                                                         Characters.Boss.sanya_sasha_health_up, GameStrings.Icons.player_health, 
                                                         Characters.Boss.sanya_sasha_damage_up, GameStrings.Icons.damage, 
                                                         Characters.Boss.sanya_sasha_critical_up, GameStrings.Icons.critical_chance)
   
   def description():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}\n{7}'.format(GameStrings.Icons.player_health, Characters.player.health,
                                                      GameStrings.Icons.damage, Characters.player.damage,
                                                      GameStrings.Icons.critical_chance, Characters.player.critical_chance,
                                                      'Эзотерический парикмахер',
                                                      'Мастер чистого белого неделимого броска ножницами')


class Toshik():
   name = 'Тошик'

   def skill_effect():
      return '+{0}%{1}\n{2}{3}'.format(Characters.Player.toshik_health_up_skill_procent, 
                                       GameStrings.Icons.player_health, GameStrings.Icons.cooldown, 
                                       Characters.player.cooldown)

   def passive_effect():
      return '{0}\n{1}+{2}%{3}'.format('В здоровом теле - здоровый урон', 
                                       GameStrings.Icons.damage, Characters.Player.toshik_passive_skill_procent, 
                                       GameStrings.Icons.player_health)

   def description():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}\n{7}'.format(GameStrings.Icons.player_health, Characters.player.health,
                                                      GameStrings.Icons.damage, Characters.player.damage,
                                                      GameStrings.Icons.critical_chance, Characters.player.critical_chance,
                                                      'Псайтанковый медитатор',
                                                      'Больше здоровья - больше силы')                                     
   

class Kolya():
   name = 'Коля'

   def skill_effect():
      return '{0}-{1}{2}\n{3}+{1}{2}\n{4}{5}'.format(Characters.boss.icon, Fight.kolya_hack_damage_value,
                                                      GameStrings.Icons.damage, Characters.player.icon,
                                                      GameStrings.Icons.cooldown, Characters.player.cooldown)

   def description():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}\n{7}'.format(GameStrings.Icons.player_health, Characters.player.health,
                                                      GameStrings.Icons.damage, Characters.player.damage,
                                                      GameStrings.Icons.critical_chance, Characters.player.critical_chance,
                                                      'Хипстерский программист',
                                                      'Падок на разочарование')


class Temich():
   name = 'Темыч'
   bad_skill_effect = 'Ой ой, Темыч запутался в своей суете'

   def good_skill_effect():
      return '{0}{1}{2}\n{3}{4}'.format(GameStrings.Icons.player_health, GameStrings.Icons.exchange, 
                                       GameStrings.Icons.boss_health, GameStrings.Icons.cooldown, Characters.player.cooldown)
   
   def description():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}\n{7}'.format(GameStrings.Icons.player_health, Characters.player.health,
                                                      GameStrings.Icons.damage, Characters.player.damage,
                                                      GameStrings.Icons.critical_chance, Characters.player.critical_chance,
                                                      'Нетикающий суетолог',
                                                      'Если не поймет что понес урон - значит этого не было')

class Text():
   def hero_description():
      return '{0}{1}\n{2}'.format(CharactersGenerator.player.name, CharactersGenerator.player.icon, 
                                 CharactersGenerator.player.description)