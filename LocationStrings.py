import Locations
import GameStrings

class Stage25():
   name = '25й этаж'

   def description():
      return '{0}\n-{1}%{2}\n-{3}%{4}'.format('Святое место, где настоящие убийцы смотрят в пол', 
                                                Locations.loc.damage, GameStrings.Icons.damage, 
                                                Locations.loc.critical_chance, GameStrings.Icons.critical_chance)

   def mitya_interaction():
      return '{0}\n+{1}%{2}'.format('Митя тут, как рыба в воде', 
                                    Locations.Location.mitya_stage25_health_up_procent, GameStrings.Icons.player_health)

   def kolya_interaction():
      return '{0}\n-{1}%{2}'.format('Коле здесь явно не место', 
                                    Locations.Location.kolya_stage25_health_down_procent, GameStrings.Icons.player_health)                                    


class BadTrip():
   name = 'Бэд Трип'
   temich_interaction = 'Темыч так и не понял что был в бэде, а значит этого не было!'

   def description():
      return '{0}\n-{1}%{2}\n-{3}%{4}'.format('Тебя занесло в Бэд Трип! Вот незадача!',
                                             Locations.loc.health, GameStrings.Icons.player_health,
                                             Locations.loc.damage, GameStrings.Icons.damage)

   def kolya_interaction():
      return '{0}\n+{1}{2}\n+{3}{4}'.format('Коля любит бэд трипы', 
                                             Locations.Location.kolya_badtrip_health_up_value, GameStrings.Icons.player_health, 
                                             Locations.Location.kolya_badtrip_damage_up_value, GameStrings.Icons.damage)


class Drochilnya():
   name = 'Дрочильня'

   def description():
      return '{0}\n+{1}%{2}\n+{3}%{4}'.format('Тренировка в тесном мужском кругу лишней не бывает, да?',
                                             Locations.loc.damage, Locations.loc.critical_chance)

   def sanya_interaction():
      return '{0}\n+{1}{2}'.format('Да, Саша?', Locations.loc.critical_chance, GameStrings.Icons.critical_chance)


class Molebka():
   name = 'Молебка'

   def description():
      return '{0}\n-{1}%{2}\n+{3}%{4}'.format('Медитативный псайденс измотал тебя, но в итоге ты стал сильнее',
                                             Locations.loc.health, GameStrings.Icons.player_health, 
                                             Locations.loc.damage, GameStrings.Icons.damage)

   def toshik_interaction():
      return '{0}\n+{1}%{2}\n+{3}%{4}'.format('Но Тошика так просто не измотаешь', 
                                             Locations.loc.health, GameStrings.Icons.player_health, 
                                             Locations.loc.damage, GameStrings.Icons.damage)
                                           