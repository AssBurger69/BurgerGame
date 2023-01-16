# модуль со всеми строками и функциями вывода сообщений, 
# использующих динамические характеристики касательно игрока 
# и его взаимодействия с локациями и боссами

import Characters
import Locations
import InteractionParameters
import GameStrings
import FightCycle
import CharactersGenerator

class Mitya():
   name = 'Митя'

   # сообщение способоности героя
   def skill_effect():
      return '-{0}{1}\n+{2}{3}\n{4}{5}'.format(Characters.Player.mitya_health_down_skill_value, 
                                                GameStrings.Icons.player_health, 
                                                Characters.Player.mitya_damage_up_skill_value, 
                                                GameStrings.Icons.damage, 
                                                GameStrings.Icons.cooldown, 
                                                CharactersGenerator.player.cooldown)

   #  описание героя
   def description():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}\n{7}'.format(GameStrings.Icons.player_health, 
                                                      CharactersGenerator.player.health,
                                                      GameStrings.Icons.damage, 
                                                      CharactersGenerator.player.damage,
                                                      GameStrings.Icons.critical_chance, 
                                                      CharactersGenerator.player.critical_chance,
                                                      'Мастер отсоса жизни',
                                                      'Любитель губительно-усиливающих эликсиров, будь с ними осторожен')

   # интерактив с локацией 25й этаж
   def stage25_interaction():
      return '{0}\n+{1}%{2}'.format('Митя тут, как рыба в воде', 
                                    InteractionParameters.Player.mitya_stage25_health_up_procent, 
                                    GameStrings.Icons.player_health) 

   # интерактив и боссом Инквизиция
   def inkvisizia_interaction():
      return '{0}\n{1}%{2}'.format('Каждая конвульсия делает Митю крепче!', 
                                    InteractionParameters.Boss.inkvisizia_mitya_health_up, 
                                    GameStrings.Icons.player_health)                                                                                          


class Sanya():
   name = 'Саня'

   # сообщение способоности героя
   def skill_effect():
      return '{0}-{1}{2}\n{3}{4}'.format(GameStrings.Icons.boss, FightCycle.sanya_skill_damage, 
                                          GameStrings.Icons.boss_health, GameStrings.Icons.cooldown, 
                                          CharactersGenerator.player.cooldown)

   # описание героя
   def description():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}\n{7}'.format(GameStrings.Icons.player_health, 
                                                      CharactersGenerator.player.health,
                                                      GameStrings.Icons.damage, 
                                                      CharactersGenerator.player.damage,
                                                      GameStrings.Icons.critical_chance, 
                                                      CharactersGenerator.player.critical_chance,
                                                      'Эзотерический парикмахер',
                                                      'Мастер чистого белого неделимого броска ножницами')
   
   # интерактив с локацией Дрочильня
   def drochilnya_interaction():
      return '{0}\n+{1}{2}'.format('Да, Саша?', Locations.loc.critical_chance, 
                                    GameStrings.Icons.critical_chance)    
   
   # интерактив с боссом Саша Шлякин
   def sasha_interaction():
      return '{0}\n+{1}%{2}\n+{3}%{4}\n+{5}%{6}'.format('Победа над собой возвысила тебя!', 
                                                         InteractionParameters.Boss.sanya_sasha_health_up, 
                                                         GameStrings.Icons.player_health, 
                                                         InteractionParameters.Boss.sanya_sasha_damage_up, 
                                                         GameStrings.Icons.damage, 
                                                         InteractionParameters.Boss.sanya_sasha_critical_up, 
                                                         GameStrings.Icons.critical_chance)                                                                                      


class Toshik():
   name = 'Тошик'
   
   # описание способности героя
   def skill_effect():
      return '+{0}%{1}\n{2}{3}'.format(Characters.Player.toshik_health_up_skill_procent, 
                                       GameStrings.Icons.player_health, GameStrings.Icons.cooldown, 
                                       CharactersGenerator.player.cooldown)
   
   # описание пассивной способности героя
   def passive_effect():
      return '{0}\n{1}+{2}%{3}'.format('В здоровом теле - здоровый урон', 
                                       GameStrings.Icons.damage, 
                                       Characters.Player.toshik_passive_skill_procent, 
                                       GameStrings.Icons.player_health)
   
   # описание героя
   def description():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}\n{7}'.format(GameStrings.Icons.player_health, 
                                                      CharactersGenerator.player.health,
                                                      GameStrings.Icons.damage, 
                                                      CharactersGenerator.player.damage,
                                                      GameStrings.Icons.critical_chance, 
                                                      CharactersGenerator.player.critical_chance,
                                                      'Псайтанковый медитатор',
                                                      'Больше здоровья - больше силы')    
   
   # интерактив с локацией Молебка
   def molebka_interaction():
      return '{0}\n+{1}%{2}\n+{3}%{4}'.format('Но Тошика так просто не измотаешь', 
                                             Locations.loc.health, GameStrings.Icons.player_health, 
                                             Locations.loc.damage, GameStrings.Icons.damage)                                                                        
   

class Kolya():
   name = 'Коля'
   
   # описание способности героя
   def skill_effect():
      return '{0}-{1}{2}\n{3}+{1}{2}\n{4}{5}'.format(CharactersGenerator.boss.icon, 
                                                      FightCycle.kolya_hack_damage_value,
                                                      GameStrings.Icons.damage, 
                                                      CharactersGenerator.player.icon,
                                                      GameStrings.Icons.cooldown, 
                                                      CharactersGenerator.player.cooldown)
   
   # описание героя
   def description():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}\n{7}'.format(GameStrings.Icons.player_health, 
                                                      CharactersGenerator.player.health,
                                                      GameStrings.Icons.damage, 
                                                      CharactersGenerator.player.damage,
                                                      GameStrings.Icons.critical_chance, 
                                                      CharactersGenerator.player.critical_chance,
                                                      'Хипстерский программист',
                                                      'Падок на разочарование')
   
   # интерактив с локацией Бэд Трип
   def badtrip_interaction():
      return '{0}\n+{1}{2}\n+{3}{4}'.format('Коля любит бэд трипы', 
                                             InteractionParameters.Player.kolya_badtrip_health_up_value, 
                                             GameStrings.Icons.player_health, 
                                             InteractionParameters.Player.kolya_badtrip_damage_up_value, 
                                             GameStrings.Icons.damage)    
   
   # интерактив с локацией 25 этаж
   def stage25_interaction():
      return '{0}\n-{1}%{2}'.format('Коле здесь явно не место', 
                                    InteractionParameters.Player.kolya_stage25_health_down_procent, 
                                    GameStrings.Icons.player_health)                                                                                                 


class Temich():
   name = 'Темыч'

   # описание неудачной способности героя
   bad_skill_effect = 'Ой ой, Темыч запутался в своей суете'
   
   # описание успешной способности героя
   def good_skill_effect():
      return '{0}{1}{2}\n{3}{4}'.format(GameStrings.Icons.player_health, GameStrings.Icons.exchange, 
                                          GameStrings.Icons.boss_health, GameStrings.Icons.cooldown, 
                                          CharactersGenerator.player.cooldown)

   # описание героя
   def description():
      return '{0}{1}\n{2}{3}\n{4}{5}\n{6}\n{7}'.format(GameStrings.Icons.player_health, 
                                                      CharactersGenerator.player.health,
                                                      GameStrings.Icons.damage, 
                                                      CharactersGenerator.player.damage,
                                                      GameStrings.Icons.critical_chance, 
                                                      CharactersGenerator.player.critical_chance,
                                                      'Нетикающий суетолог',
                                                      'Если не поймет что понес урон - значит этого не было')

class Text():
   def hero_description():
      return '{0}{1}\n{2}'.format(CharactersGenerator.player.name, 
                                 CharactersGenerator.player.icon, 
                                 CharactersGenerator.player.description)