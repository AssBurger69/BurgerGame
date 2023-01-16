# модуль со всеми строками касательно локаций и взаимодействия персонажей с ними

import Locations
import GameStrings


class Stage25():
   name = '25й этаж'

   def description():
      return '{0}{1}\n{2}\n-{3}%{4}\n-{5}%{6}'.format(Locations.loc.name, Locations.loc.icon,
                                                      'Святое место, где настоящие убийцы смотрят в пол', 
                                                      Locations.loc.damage, GameStrings.Icons.damage, 
                                                      Locations.loc.critical_chance, 
                                                      GameStrings.Icons.critical_chance)                                  


class BadTrip():
   name = 'Бэд Трип'
   temich_interaction = 'Темыч так и не понял что был в бэде, а значит этого не было!'

   def description():
      return '{0}{1}\n{2}\n-{3}%{4}\n-{5}%{6}'.format(Locations.loc.name, Locations.loc.icon,
                                                      'Тебя занесло в Бэд Трип! Вот незадача!',
                                                      Locations.loc.health, GameStrings.Icons.player_health,
                                                      Locations.loc.damage, GameStrings.Icons.damage)


class Drochilnya():
   name = 'Дрочильня'

   def description():
      return '{0}{1}\n{2}\n+{3}%{4}'.format(Locations.loc.name, Locations.loc.icon,
                                                      'Тренировка в тесном мужском кругу лишней не бывает, да?',
                                                      Locations.loc.damage, Locations.loc.critical_chance)


class Molebka():
   name = 'Молебка'

   def description():
      return '{0}{1}\n{2}\n-{3}%{4}\n+{5}%{6}'.format(Locations.loc.name, Locations.loc.icon,
                                                      'Медитативный псайденс измотал тебя, но в итоге ты стал сильнее',
                                                      Locations.loc.health, GameStrings.Icons.player_health, 
                                                      Locations.loc.damage, GameStrings.Icons.damage)


class GodCity():
   name = 'Город Богов'

   def description():
      return '{0}{1}\n{2}\n+{3}%{4}\n+{5}%{6}\n+{7}%{8}'.format(Locations.loc.name, Locations.loc.icon,
                                                               'Прогулка по нему разносторонне возвышает тебя',
                                                               Locations.loc.health, GameStrings.Icons.player_health,
                                                               Locations.loc.damage, GameStrings.Icons.damage,
                                                               Locations.loc.critical_chance, 
                                                               GameStrings.Icons.critical_chance)    


class Kolbas():
   name = 'Хата Колбаса'

   def description():
      return '{0}{1}\n{2}\n-{3}%{4}'.format(Locations.loc.name, Locations.loc.icon,
                                             'Нахождение здесь насыщает тебя благовонием помойки!', 
                                             Locations.loc.health, GameStrings.Icons.player_health)                                 


class Polazna():
   name = 'Полазна'

   def description():
      return '{0}{1}\n{2}\n+{3}%{4}\n-{5}%{6}'.format(Locations.loc.name, Locations.loc.icon,
                                                      'Ебанув текилы ты стал крепче, но закусив шигой - немощнее', 
                                                      Locations.loc.health, GameStrings.Icons.player_health,
                                                      Locations.loc.damage, GameStrings.Icons.damage)


class Army():
   name = 'Армия'

   def description():
      return '{0}{1}\n{2}\n-{3}%{4}\n+{5}%{6}'.format(Locations.loc.name, Locations.loc.icon,
                                                      'Армия забрала год твоей жизни, но ты неплохо так подкачался',
                                                      Locations.loc.health, GameStrings.Icons.player_health,
                                                      Locations.loc.damage, GameStrings.Icons.damage)  
                                                                                                                                      
                                           