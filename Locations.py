import MyStrings
import random
import Characters

class Location():
   pers_iteraction_message = False
   location_list = [MyStrings.Text.kolbas_name.value, MyStrings.Text.polazna_name.value, MyStrings.Text.god_city_name.value, MyStrings.Text.bad_trip_name.value, MyStrings.Text.molebka_name.value, MyStrings.Text.army_name.value, MyStrings.Text.drochilnya_name.value, MyStrings.Text.stage25_name.value]
   location_name = random.choice(location_list)

   def __init__(self, value1, value2, value3, name, description, icon):
      self.value1 = value1
      self.value2 = value2
      self.value3 = value3
      self.name = name
      self.description = description
      self.icon = icon

def location_choice(x):
   global loc

   if x == MyStrings.Text.kolbas_name.value:
      loc = Location(10, 500, 0, x, MyStrings.Text.kolbas_description.value, MyStrings.Text.kolbas_icon.value)
      Characters.Char.health_down_procent(Characters.char, loc.value1)
      
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         Characters.Boss.health_up(Characters.boss, loc.value2)
         Location.pers_iteraction_message = MyStrings.Text.doner_kolbas_text.value
   
   elif x == MyStrings.Text.polazna_name.value:
      loc = Location(20, 10, 0, x, MyStrings.Text.polazna_description.value, MyStrings.Text.polazna_icon.value)
      Characters.Char.health_up_procent(Characters.char, loc.value1)
      Characters.Char.damage_down_procent(Characters.char, loc.value2)

   elif x == MyStrings.Text.god_city_name.value:
      loc = Location(10, 10, 10, x, MyStrings.Text.god_city_description.value, MyStrings.Text.god_city_icon.value)
      Characters.Char.health_up_procent(Characters.char, loc.value1)
      Characters.Char.damage_up_procent(Characters.char, loc.value2)
      Characters.Char.critical_chance_up(Characters.char, loc.value3)
      
      if Characters.boss.name == MyStrings.Text.chaikovskii_name.value:
         Characters.Boss.health_up_procent(Characters.boss, loc.value1)
         Characters.Boss.damage_up_procent(Characters.boss, loc.value2)
         Characters.Boss.critical_chance_up(Characters.boss, loc.value3)
         Location.pers_iteraction_message = MyStrings.Text.chaikovskii_god_city_text.value

   elif x == MyStrings.Text.bad_trip_name.value:
      loc = Location(20, 20, 0, x, MyStrings.Text.bad_trip_description.value, MyStrings.Text.bad_trip_icon.value)
      if Characters.char.name != MyStrings.Text.kolya_name.value and Characters.char.name != MyStrings.Text.temich_name.value:
         Characters.Char.health_down_procent(Characters.char, loc.value1)
         Characters.Char.damage_down_procent(Characters.char, loc.value2)
         Location.pers_iteraction_message = MyStrings.Text.bad_trip_effect_text.value

      elif Characters.char.name == MyStrings.Text.temich_name.value:
         Location.pers_iteraction_message = MyStrings.Text.temich_bad_trip_text.value

      elif Characters.char.name == MyStrings.Text.kolya_name.value:
         Characters.Char.health_up(Characters.char, 300)
         Characters.Char.damage_up(Characters.char, 100)
         Location.pers_iteraction_message = MyStrings.Text.kolya_bad_trip_text.value
      
   elif x == MyStrings.Text.molebka_name.value:
      loc = Location(20, 10, 0, x, MyStrings.Text.molebka_description.value, MyStrings.Text.molebka_icon.value)
      if Characters.char.name != MyStrings.Text.toshik_name.value:
         Characters.Char.health_down_procent(Characters.char, loc.value1)
         Characters.Char.damage_up_procent(Characters.char, loc.value2)
         Location.pers_iteraction_message = MyStrings.Text.molebka_effect_text.value

      elif Characters.char.name == MyStrings.Text.toshik_name.value:
         Characters.Char.health_up_procent(Characters.char, loc.value1)
         Characters.Char.damage_up_procent(Characters.char, loc.value2)
         Location.pers_iteraction_message = MyStrings.Text.toshik_molebka_text.value
      
   elif x == MyStrings.Text.army_name.value:
      loc = Location(50, 30, 0, x, MyStrings.Text.army_description.value, MyStrings.Text.army_icon.value)
      Characters.Char.health_down_procent(Characters.char, loc.value1)
      Characters.Char.damage_up_procent(Characters.char, loc.value2)

   elif x == MyStrings.Text.drochilnya_name.value:
      loc = Location(10, 0, 10, x, MyStrings.Text.drochilnya_description.value, MyStrings.Text.drochilnya_icon.value)
      Characters.Char.damage_up_procent(Characters.char, loc.value1)
      Characters.Char.critical_chance_up(Characters.char, loc.value3)
      if Characters.char.name == MyStrings.Text.sanya_name.value:
         Characters.Char.critical_chance_up(Characters.char, loc.value3)
         Location.pers_iteraction_message = MyStrings.Text.sanya_drochilnya_text.value

   elif x == MyStrings.Text.stage25_name.value:
      loc = Location(50, 10, 0, x, MyStrings.Text.stage25_description.value, MyStrings.Text.stage25_icon.value)
      Characters.Char.damage_down_procent(Characters.char, loc.value1)
      Characters.Char.critical_chance_down(Characters.char, loc.value2)
      if Characters.char.name == MyStrings.Text.kolya_name.value:
         Characters.Char.health_down_procent(Characters.char, 20)
         Location.pers_iteraction_message = MyStrings.Text.kolya_stage25_text.value
      elif Characters.char.name == MyStrings.Text.mitya_name.value:
         Characters.Char.health_up_procent(Characters.char, 20)
         Location.pers_iteraction_message = MyStrings.Text.mitya_stage25_text.value