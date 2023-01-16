# модуль со всеми параметрами и атрибутами класса Локаций
# создание объектов локаций, 
# применение их общих и интерактивных эффектов

import GameStrings
import PlayerStrings
import LocationStrings
import BossStrings
import random
import CharactersGenerator
import InteractionParameters

class Location():
   # переменная для вывода интерактивного сообщение при его наличии
   pers_iteraction_message = False

   # список всех имен локаций для их случайного подбора
   location_list = [LocationStrings.Kolbas.name, LocationStrings.Polazna.name,
                     LocationStrings.GodCity.name, LocationStrings.BadTrip.name,
                     LocationStrings.Molebka.name, LocationStrings.Army.name,
                     LocationStrings.Drochilnya.name, LocationStrings.Stage25.name]

   location_name = random.choice(location_list)

   description = False

   # создание класса Локация
   def __init__(self, health, damage, critical_chance, name, icon):
      self.health = health
      self.damage = damage
      self.critical_chance = critical_chance
      self.name = name
      self.icon = icon

def location_choice(location_name):
   # создание экземпляра локации с данными значениями:
   # Влияние на здоровье, влияние на урон, влияние на критический шанс
   # имя локации и иконка
   global loc

   # Хата Колбаса
   if location_name == LocationStrings.Kolbas.name:

      loc = Location(10, 0, 0, location_name, 
                     GameStrings.Icons.kolbas)
      Location.description = LocationStrings.Kolbas.description()                     

      # применение эффекта локации
      CharactersGenerator.player.health_down_procent(loc.health)
      
      # интерактив с боссом Донер Кебаб
      if CharactersGenerator.boss.name == BossStrings.Doner.name:
         CharactersGenerator.boss.health_up(InteractionParameters.Boss.doner_kolbas)
         Location.pers_iteraction_message = BossStrings.Doner.kolbas_interaction()
   


   # Полазна
   elif location_name == LocationStrings.Polazna.name:

      loc = Location(20, 10, 0, location_name, 
                     GameStrings.Icons.polazna)
      Location.description = LocationStrings.Polazna.description()                     

      # применение эффекта локации
      CharactersGenerator.player.health_up_procent(loc.health)
      CharactersGenerator.player.damage_down_procent(loc.damage)


   # Город Богов
   elif location_name == LocationStrings.GodCity.name:

      loc = Location(10, 10, 10, location_name, 
                     GameStrings.Icons.god_city)
      Location.description = LocationStrings.GodCity.description()                     

      # применение эффекта локации 
      CharactersGenerator.player.health_up_procent(CharactersGenerator.player, loc.health)
      CharactersGenerator.player.damage_up_procent(CharactersGenerator.player, loc.damage)
      CharactersGenerator.player.critical_chance_up(CharactersGenerator.player, loc.critical_chance)
      
      # интерактив с боссом Чайковский
      if CharactersGenerator.boss.name == BossStrings.Chaikovskii.name:
         CharactersGenerator.boss.health_up_procent(CharactersGenerator.boss, loc.health)
         CharactersGenerator.boss.damage_up_procent(CharactersGenerator.boss, loc.damage)
         CharactersGenerator.boss.critical_chance_up(CharactersGenerator.boss, loc.critical_chance)
         Location.pers_iteraction_message = BossStrings.Chaikovskii.god_city_interaction()


   # Бэд трип
   elif location_name == LocationStrings.BadTrip.name:

      loc = Location(20, 20, 0, location_name, 
                     GameStrings.Icons.badtrip)
      Location.description = LocationStrings.BadTrip.description()                     

      # интерактив с игроком Темыч
      if CharactersGenerator.player.name == PlayerStrings.Temich.name:
         Location.pers_iteraction_message = LocationStrings.BadTrip.temich_interaction

      # интерактив с игроком Коля
      elif CharactersGenerator.player.name == PlayerStrings.Kolya.name:
         CharactersGenerator.player.health_up(InteractionParameters.Player.kolya_badtrip_health_up_value)
         CharactersGenerator.player.damage_up(InteractionParameters.Player.kolya_badtrip_damage_up_value)
         Location.pers_iteraction_message = PlayerStrings.Kolya.badtrip_interaction()

      # применение эффекта локации для других игроков
      else:
         CharactersGenerator.player.health_down_procent(loc.health)
         CharactersGenerator.player.damage_down_procent(loc.damage)
         Location.pers_iteraction_message = LocationStrings.BadTrip.description()


   # Молебка   
   elif location_name == LocationStrings.Molebka.name:

      loc = Location(20, 10, 0, location_name, 
                     GameStrings.Icons.molebka)
      Location.description = LocationStrings.Molebka.description()                     

      # интерактив с игроком Тошик
      if CharactersGenerator.player.name == PlayerStrings.Toshik.name:
         CharactersGenerator.player.health_up_procent(loc.health)
         CharactersGenerator.player.damage_up_procent(loc.damage)
         Location.pers_iteraction_message = PlayerStrings.Toshik.molebka_interaction()

      # примерение эффекта локации для других игроков
      else:
         CharactersGenerator.player.health_down_procent(loc.health)
         CharactersGenerator.player.damage_up_procent(loc.damage)
   

   # Армия
   elif location_name == LocationStrings.Army.name:

      loc = Location(50, 30, 0, location_name, 
                     GameStrings.Icons.army)
      Location.description = LocationStrings.Army.description()                     

      # применение эффекта локации                     
      CharactersGenerator.player.health_down_procent(loc.health)
      CharactersGenerator.player.damage_up_procent(loc.damage)


   # Дрочильня
   elif location_name == LocationStrings.Drochilnya.name:

      loc = Location(0, 10, 10, location_name, 
                     GameStrings.Icons.drochilnya)
      Location.description = LocationStrings.Drochilnya.description()                     

      # применение эффекта локации
      CharactersGenerator.player.damage_up_procent(loc.damage)
      CharactersGenerator.player.critical_chance_up(loc.critical_chance)

      # интерактив с игроком Саня
      if CharactersGenerator.player.name == PlayerStrings.Sanya.name:
         CharactersGenerator.player.critical_chance_up(loc.critical_chance)
         Location.pers_iteraction_message = PlayerStrings.Sanya.drochilnya_interaction()


   # 25й этаж
   elif location_name == LocationStrings.Stage25.name:

      loc = Location(0, 50, 10, location_name, 
                     GameStrings.Icons.stage25)
      Location.description = LocationStrings.Stage25.description()                     

      # применение эффекта локации
      CharactersGenerator.player.damage_down_procent(loc.damage)
      CharactersGenerator.player.critical_chance_down(loc.critical_chance)

      # интерактив с игроком Коля
      if CharactersGenerator.player.name == PlayerStrings.Kolya.name:
         CharactersGenerator.player.health_down_procent(InteractionParameters.Player.kolya_stage25_health_down_procent)
         Location.pers_iteraction_message = PlayerStrings.Kolya.stage25_interaction()

      # интерактив с игроком Митя
      elif CharactersGenerator.player.name == PlayerStrings.Mitya.name:
         CharactersGenerator.player.health_up_procent(InteractionParameters.Player.mitya_stage25_health_up_procent)
         Location.pers_iteraction_message = PlayerStrings.Mitya.stage25_interaction()