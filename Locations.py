import GameStrings
import PlayerStrings
import LocationStrings
import random
import Characters

class Location():
   pers_iteraction_message = False
   location_list = [MyStrings.Text.kolbas_name.value, MyStrings.Text.polazna_name.value, MyStrings.Text.god_city_name.value, MyStrings.Text.bad_trip_name.value, MyStrings.Text.molebka_name.value, MyStrings.Text.army_name.value, MyStrings.Text.drochilnya_name.value, MyStrings.Text.stage25_name.value]
   location_name = random.choice(location_list)

   # интерактивные значения изменения персонажей 
   kolya_stage25_health_down_procent = 20
   kolya_badtrip_health_up_value = 300
   kolya_badtrip_damage_up_value = 100
   mitya_stage25_health_up_procent = 20

   def __init__(self, health, damage, critical_chance, name, description, icon):
      self.health = health
      self.damage = damage
      self.critical_chance = critical_chance
      self.name = name
      self.description = description
      self.icon = icon

def location_choice(location_name):
   global loc

   if location_name == MyStrings.Text.kolbas_name.value:
      loc = Location(10, 500, 0, location_name, MyStrings.Text.kolbas_description.value, MyStrings.Text.kolbas_icon.value)
      Characters.Player.health_down_procent(Characters.player, loc.value1)
      
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         Characters.Boss.health_up(Characters.boss, loc.value2)
         Location.pers_iteraction_message = MyStrings.Text.doner_kolbas_text.value
   
   elif location_name == MyStrings.Text.polazna_name.value:
      loc = Location(20, 10, 0, location_name, MyStrings.Text.polazna_description.value, MyStrings.Text.polazna_icon.value)
      Characters.Player.health_up_procent(Characters.player, loc.value1)
      Characters.Player.damage_down_procent(Characters.player, loc.value2)

   elif location_name == MyStrings.Text.god_city_name.value:
      loc = Location(10, 10, 10, location_name, MyStrings.Text.god_city_description.value, MyStrings.Text.god_city_icon.value)
      Characters.Player.health_up_procent(Characters.player, loc.value1)
      Characters.Player.damage_up_procent(Characters.player, loc.value2)
      Characters.Player.critical_chance_up(Characters.player, loc.value3)
      
      if Characters.boss.name == MyStrings.Text.chaikovskii_name.value:
         Characters.Boss.health_up_procent(Characters.boss, loc.value1)
         Characters.Boss.damage_up_procent(Characters.boss, loc.value2)
         Characters.Boss.critical_chance_up(Characters.boss, loc.value3)
         Location.pers_iteraction_message = MyStrings.Text.chaikovskii_god_city_text.value


   # Бэд Трип
   elif location_name == LocationStrings.BadTrip.name:

      loc = Location(20, 20, 0, location_name, LocationStrings.BadTrip.description(), GameStrings.Icons.badtrip)

      # интерактив с игроком Темыч
      if Characters.player.name == PlayerStrings.Temich.name:
         Location.pers_iteraction_message = LocationStrings.BadTrip.temich_interaction

      # интерактив с игроком Коля
      elif Characters.player.name == PlayerStrings.Kolya.name:
         Characters.player.health_up(Location.kolya_badtrip_health_up_value)
         Characters.player.damage_up(Location.kolya_badtrip_damage_up_value)
         Location.pers_iteraction_message = LocationStrings.BadTrip.kolya_interaction()

      # применение эффекта локации для других игроков
      else:
         Characters.Player.health_down_procent(loc.health)
         Characters.Player.damage_down_procent(loc.damage)
         Location.pers_iteraction_message = LocationStrings.BadTrip.description()


   # Молебка   
   elif location_name == LocationStrings.Molebka.name:

      loc = Location(20, 10, 0, location_name, LocationStrings.Molebka.description(), GameStrings.Icons.molebka)

      # интерактив с игроком Тошик
      if Characters.player.name == PlayerStrings.Toshik.name:
         Characters.player.health_up_procent(loc.health)
         Characters.player.damage_up_procent(loc.damage)
         Location.pers_iteraction_message = LocationStrings.Molebka.toshik_interaction()

      # примерение эффекта локации для других игроков
      else:
         Characters.player.health_down_procent(loc.health)
         Characters.player.damage_up_procent(loc.damage)
      
   elif location_name == MyStrings.Text.army_name.value:
      loc = Location(50, 30, 0, location_name, MyStrings.Text.army_description.value, MyStrings.Text.army_icon.value)
      Characters.Player.health_down_procent(Characters.player, loc.value1)
      Characters.Player.damage_up_procent(Characters.player, loc.value2)


   # Дрочильня
   elif location_name == LocationStrings.Drochilnya.name:

      loc = Location(0, 10, 10, location_name, LocationStrings.Drochilnya.description(), GameStrings.Icons.drochilnya)

      # применение эффекта локации
      Characters.player.damage_up_procent(loc.damage)
      Characters.player.critical_chance_up(loc.critical_chance)

      # интерактив с игроком Саня
      if Characters.player.name == PlayerStrings.Sanya.name:
         Characters.player.critical_chance_up(loc.critical_chance)
         Location.pers_iteraction_message = LocationStrings.Drochilnya.sanya_interaction()


   # 25й этаж
   elif location_name == LocationStrings.Stage25.name:

      loc = Location(0, 50, 10, location_name, LocationStrings.Stage25.description(), GameStrings.Icons.stage25)

      # применение эффекта локации
      Characters.player.damage_down_procent(loc.damage)
      Characters.player.critical_chance_down(loc.critical_chance)

      # интерактив с игроком Коля
      if Characters.player.name == PlayerStrings.Kolya.name:
         Characters.player.health_down_procent(Location.kolya_stage25_health_down_procent)
         Location.pers_iteraction_message = LocationStrings.Stage25.kolya_interaction()

      # интерактив с игроком Митя
      elif Characters.player.name == PlayerStrings.Mitya.name:
         Characters.player.health_up_procent(Location.mitya_stage25_health_up_procent)
         Location.pers_iteraction_message = LocationStrings.Stage25.mitya_interaction()