# модуль создания объектов игрока и боссов, 
# функции выбора босса от количества побед игрока, 
# способности боссов перед боем с игроком

import GameStrings
import PlayerStrings
import BossStrings
import Characters
import random

def player_get_stats(hero_name):
   # создание экземпляра игрока с данными характеристиками:
   # имя, здоровье, урон, шанс критической атаки, шанс уклонения, 
   # вампиризм, регенерация, название способности, иконка
   global player

   # Митя
   if hero_name == PlayerStrings.Mitya.name:
      player = Characters.Player(hero_name, 800, 100, 0, 0, 20, 0, 
                                 GameStrings.ButtonText.mitya_skill,
                                 GameStrings.Icons.mitya)
      player.description = PlayerStrings.Mitya.description()

   # Саня 
   elif hero_name == PlayerStrings.Sanya.name:
      player = Characters.Player(hero_name, 1000, 200, 30, 0, 0, 0, 
                                 GameStrings.ButtonText.sanya_skill, 
                                 GameStrings.Icons.sanya)
      player.description = PlayerStrings.Sanya.description()
                                 
   # Тошик   
   elif hero_name == PlayerStrings.Toshik.name:
      player = Characters.Player(hero_name, 1500, 100, 0, 0, 0, 0, 
                                 GameStrings.ButtonText.toshik_skill, 
                                 GameStrings.Icons.toshik)
      player.description = PlayerStrings.Toshik.description()
                                 
   # Коля   
   elif hero_name == PlayerStrings.Kolya.name:
      player = Characters.Player(hero_name, 1200, 100, 0, 0, 0, 0, 
                                 GameStrings.ButtonText.kolya_skill, 
                                 GameStrings.Icons.kolya)
      player.description = PlayerStrings.Kolya.description()
                                 
   # Темыч   
   elif hero_name == PlayerStrings.Temich.name:
      player = Characters.Player(hero_name, 800, 150, 0, 15, 0, 0, 
                                 GameStrings.ButtonText.temich_skill, 
                                 GameStrings.Icons.temich)
      player.description = PlayerStrings.Temich.description()
                                 


def boss_get_stats(boss_name):
   # создание экземпляра босса с данными характеристиками:
   # имя, здоровье, урон, шанс критической атаки, шанс уклонения, 
   # вампиризм, регенерация, описание босса
   global boss
   
   # Палыч
   if boss_name == BossStrings.Palich.name:
      boss = Characters.Boss(boss_name, 800, 200, 0, 0, 0, 0, 
                              BossStrings.Palich.description)
   
   # Чайковский    
   elif boss_name == BossStrings.Chaikovskii.name:
      boss = Characters.Boss(boss_name, 600, 250, 0, 0, 0, 0, 
                              BossStrings.Chaikovskii.description)
      boss.resurrection = True
   
   # Вив
   elif boss_name == BossStrings.Viv.name:
      boss = Characters.Boss(boss_name, 900, 100, 0, 0, 0, 0, 
                              BossStrings.Viv.description)
   
   # Саша Шлякин
   elif boss_name == BossStrings.Sasha.name:
      boss = Characters.Boss(boss_name, 1000, 200, 20, 0, 0, 0, 
                              BossStrings.Sasha.description)
   
   # Качаловская Тварь
   elif boss_name == BossStrings.Tvar.name:
      boss = Characters.Boss(boss_name, 800, 50, 0, 0, 0, 0, 
                              BossStrings.Tvar.description)
      boss.returnal_value = 50
   
   # Рандом Рандомыч
   elif boss_name == BossStrings.Randomich.name:
      boss = Characters.Boss(boss_name, random.randint(100, 1001), random.randint(10, 301), 
                              random.randint(0, 51), random.randint(0, 51), 0, 
                              random.randint(0, 301), BossStrings.Randomich.description)
      boss.returnal_value = random.randint(0, 51)
   
   # Котенок-Тролль
   elif boss_name == BossStrings.Kitty.name:
      boss = Characters.Boss(boss_name, 1000, 200, 0, 0, 0, 0, 
                              BossStrings.Kitty.description)
      boss.end_skill_chance = 50
   
   # Инквизиция
   elif boss_name == BossStrings.Inkvisizia.name:
      boss = Characters.Boss(boss_name, 500, 500, 50, 0, 0, 0, 
                              BossStrings.Inkvisizia.description)
   
   # Доктор Леха
   elif boss_name == BossStrings.DocLeha.name:
      boss = Characters.Boss(boss_name, 1500, 300, 0, 0, 0, 0, 
                              BossStrings.DocLeha.description)
      boss.end_skill_chance = 36
   
   # Пьяный Леха
   elif boss_name == BossStrings.DrunkLeha.name:
      boss = Characters.Boss(boss_name, 1200, 100, 0, 0, 0, 0, 
                              BossStrings.DocLeha.description)
   
   # Мел
   elif boss_name == BossStrings.Mel.name:
      boss = Characters.Boss(boss_name, 50, 0, 0, 90, 0, 0, 
                              BossStrings.Mel.description)
   
   # Рыжий
   elif boss_name == BossStrings.Redhead.name:
      boss = Characters.Boss(boss_name, 2000, 100, 0, 0, 0, 300, 
                              BossStrings.Redhead.description)
   
   # Следователь
   elif boss_name == BossStrings.Sledovatel.name:
      boss = Characters.Boss(boss_name, 1500, 100, 0, 50, 0, 0, 
                              BossStrings.Sledovatel.description)
      boss.skill_meter_level = 10
   
   # Донер Кебаб
   elif boss_name == BossStrings.Doner.name:
      boss = Characters.Boss(boss_name, 1800, 350, 0, 0, 0, 0, 
                              BossStrings.Doner.description)
   
   # Черный Стас
   elif boss_name == BossStrings.BlackStas.name:
      boss = Characters.Boss(boss_name, 1500, 300, 0, 30, 0, 0, 
                              BossStrings.BlackStas.description)
   
   # Дрон
   elif boss_name == BossStrings.Dron.name:
      boss = Characters.Boss(boss_name, 2000, 100, 0, 0, 0, 0, 
                              BossStrings.Dron.description)
      boss.skill_meter_level = 5
   
   # Валера Гладиатор
   elif boss_name == BossStrings.Glad.name:
      boss = Characters.Boss(boss_name, 3000, 200, 0, 0, 0, 0, 
                              BossStrings.Glad.description)
   
   # Великая Шива
   elif boss_name == BossStrings.Shiva.name:
      boss = Characters.Boss(boss_name, 2000, 500, 0, 30, 0, 0, 
                              BossStrings.Shiva.description)
   
   # Король Макар
   elif boss_name == BossStrings.Makar.name:
      boss = Characters.Boss(boss_name, player.health, player.damage, 
                              player.critical_chance, player.miss_chance, 
                              player.lifesteal, player.regeneration,
                              BossStrings.Makar.description)
   
   # Гомогомозеки
   elif boss_name == BossStrings.Gomozeki.name:
      boss = Characters.Boss(boss_name, 2000, 300, 20, 0, 0, 200, 
                              BossStrings.Gomozeki.description)