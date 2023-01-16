# модуль со всеми параметрами и атрибутами классов Бафф и Итем
# параметры эффектов применяющихся на игрока при входе в магазин
import random
import DropStrings
import CharactersGenerator
import GameStrings

class Buff():
   # параметр увеличения здоровья игрока при посещении магазина Братишкино логово
   bratishki_health_up_value = 200
   description = False

   # создание класса Бафф - предмета увеличивающего характеристики игрока моментально
   def __init__(self, health, damage, critical_chance, miss_chance, lifesteal):
      self.health = health
      self.damage = damage
      self.critical_chance = critical_chance
      self.miss_chance = miss_chance
      self.lifesteal = lifesteal


class Item():
   # параметр увеличения атаки игрока при посещении магазина Серого Стаса
   stas_damage_up_value = 50

   # обнуление интерактивных сообщений при взаимодействии игрока/боссов с определенными предметами
   boss_iteraction_message = False
   player_iteraction_message = False

   # создание класса Итем - предмета с активацией только во время боя
   def __init__(self, value, description):
      self.value = value
      self.description = description


def shop_enter(shop_name):
   global buff_choice
   global item_choice

   # подбор трех случайных баффов или итемов на выбор игроку
   buff_choice = [random.choice(DropStrings.Buffs.buff_list), random.choice(DropStrings.Buffs.buff_list), 
                  random.choice(DropStrings.Buffs.buff_list)]

   item_choice = [random.choice(DropStrings.Items.item_list), random.choice(DropStrings.Items.item_list), 
                  random.choice(DropStrings.Items.item_list)]

   # применение параметров усиливающих характеристики игрока в зависимости от выбора магазина (здоровье или урон)
   if shop_name == GameStrings.ButtonText.stas_shop_name:
      CharactersGenerator.player.damage_up(Item.stas_damage_up_value)
      
   elif shop_name == GameStrings.ButtonText.bratishki_shop_name:
      CharactersGenerator.player.health_up(Buff.bratishki_health_up_value)