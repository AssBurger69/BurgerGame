# модуль со всеми параметрами, атрибутами и методами классов Персонаж, Игрок и Босс
import GameStrings

class Pers():
   # базовые игровые параметры
   poison_damage = 10
   bleeding_damage = 100
   win_rate = 0
   wanted_level = False
   ressurection_value = 800
   regeneration_value = 100

   # создание класса персонажа с характеристиками общими для игрока и босса
   def __init__(self, name, health, damage, critical_chance, miss_chance, lifesteal, regeneration, description):
      self.name = name
      self.health = health
      self.damage = damage
      self.critical_chance = critical_chance
      self.miss_chance = miss_chance
      self.lifesteal = lifesteal
      self.regeneration = regeneration
      self.description = description

   # функции изменения характеристик персонажей
   def health_down(self, value):
      self.health -= value
   def health_down_procent(self, value):
      self.health -= self.health * value // 100

   def health_up(self, value):
      self.health += value
   def health_up_procent(self, value):
      self.health += self.health * value // 100

   def damage_down(self, value):
      self.damage -= value
   def damage_down_procent(self, value):
      self.damage -= self.damage * value // 100

   def damage_up(self, value):
      self.damage += value
   def damage_up_procent(self, value):
      self.damage += self.damage * value // 100

   def critical_chance_down(self, value):
      self.critical_chance -= value

   def critical_chance_up(self, value):
      self.critical_chance += value

   def miss_chance_down(self, value):
      self.miss_chance -= value
   def miss_chance_down_procent(self, value):
      self.miss_chance -= self.miss_chance * value // 100

   def miss_chance_up(self, value):
      self.miss_chance += value
   def miss_chance_up_procent(self, value):
      self.miss_chance += self.miss_chance * value // 100

   def lifesteal_down(self, value):
      self.lifesteal -= value
   def lifesteal_down_procent(self, value):
      self.lifesteal -= self.lifesteal * value // 100

   def lifesteal_up(self, value):
      self.lifesteal += value
   def lifesteal_up_procent(self, value):
      self.lifesteal += self.lifesteal * value // 100

   def regeneration_down(self, value):
      self.regeneration -= value

   def regeneration_up(self, value):
      self.regeneration += value

class Player(Pers):
   # стандартное значение слота игрока - Пусто
   item = GameStrings.Text.empty_text
   # список, заполняющийся всеми предметами игрока по ходу игры
   all_items = []
   # стандартные параметры игрока
   stan_timer = 0
   cooldown = 0
   police_level = 0
   mitya_elexir_count = 0
   poison = False
   bleeding = False
   silence = False
   immunity = False
   # параметры способностей героев
   mitya_health_down_skill_value = 100
   mitya_damage_up_skill_value = 200
   toshik_health_up_skill_procent = 20
   toshik_passive_skill_procent = 5
   kolya_skill_procent = 50
   temich_skill_chance = 21
   # добавление дополнительных характеристик игрока - иконка и имя
   def __init__(self, name, health, damage, critical_chance, miss_chance, 
                  lifesteal, regeneration, description, skill_name, icon):
      super().__init__(name, health, damage, critical_chance, miss_chance, 
                        lifesteal, regeneration, description)
      self.skill_name = skill_name
      self.icon = icon

class Boss(Pers):
   # стандартные параметры боссов
   end_skill_chance = 0
   returnal_value = 0
   stan_timer = 0
   mel_blazer_level = 0
   sledovatel_busted_level = 0
   dron_obida_level = 0
   resurrection = False
   bleeding = False
   poison = False
   icon = GameStrings.Icons.boss
   # уникальные параметры при взаимодействии боссов и игрока
   inkvisizia_mitya_health_up = 50
   sanya_sasha_health_up = 20
   sanya_sasha_damage_up = 20
   sanya_sasha_critical_up = 10
   # параметры способностей боссов в конце раунда
   viv_end_skill_damage_up = 100
   kitty_end_skill_damage = 200
   drunk_leha_end_skill_boost = 50
   doc_leha_end_skill_damage = 500
   mel_end_skill_damage = 500
   dron_end_skill_damage = 2000
   glad_end_skill_damage = 500
   glad_end_skill_health_up = 500
   glad_end_skill_critical_up = 25
   glad_end_skill_damage_down = 250
   shiva_end_skill_critical_up = 20
   shiva_end_skill_damage_up = 100
   # копирование в подкласс босса характеристик класса персонаж
   def __init__(self, name, health, damage, critical_chance, miss_chance, lifesteal,regeneration ,description):
      super().__init__(name, health, damage, critical_chance, miss_chance, lifesteal, regeneration, description)