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
   # вампиризм, регенерация, описание героя, название способности, иконка
   global player
   # Митя
   if hero_name == PlayerStrings.Mitya.name:
      player = Characters.Player(hero_name, 800, 100, 0, 0, 20, 0, 
                                 PlayerStrings.Mitya.description(), GameStrings.ButtonText.mitya_skill,
                                 GameStrings.Icons.mitya)
   # Саня 
   elif hero_name == PlayerStrings.Sanya.name:
      player = Characters.Player(hero_name, 1000, 200, 30, 0, 0, 0, 
                                 PlayerStrings.Sanya.description(), GameStrings.ButtonText.sanya_skill, 
                                 GameStrings.Icons.sanya)
   # Тошик   
   elif hero_name == PlayerStrings.Toshik.name:
      player = Characters.Player(hero_name, 1500, 100, 0, 0, 0, 0, 
                                 PlayerStrings.Toshik.description(), GameStrings.ButtonText.toshik_skill, 
                                 GameStrings.Icons.toshik)
   # Коля   
   elif hero_name == PlayerStrings.Kolya.name:
      player = Characters.Player(hero_name, 1200, 100, 0, 0, 0, 0, 
                                 PlayerStrings.Kolya.description(), GameStrings.ButtonText.kolya_skill, 
                                 GameStrings.Icons.kolya)
   # Темыч   
   elif hero_name == PlayerStrings.Temich.name:
      player = Characters.Player(hero_name, 800, 150, 0, 15, 0, 0, 
                                 PlayerStrings.Temich.description(), GameStrings.ButtonText.temich_skill, 
                                 GameStrings.Icons.temich)


def boss_get_stats(boss_name):
   # создание экземпляра босса с данными характеристиками:
   # имя, здоровье, урон, шанс критической атаки, шанс уклонения, 
   # вампиризм, регенерация, описание босса
   global boss
   
   # Палыч
   if boss_name == BossStrings.palich.name:
      boss = Characters.Boss(boss_name, 800, 200, 0, 0, 0, 0, 
                              BossStrings.palich.description)
   
   # Чайковский    
   elif boss_name == BossStrings.chaikovskii.name:
      boss = Characters.Boss(boss_name, 600, 250, 0, 0, 0, 0, 
                              BossStrings.chaikovskii.description)
      boss.resurrection = True
   
   # Вив
   elif boss_name == BossStrings.viv.name:
      boss = Characters.Boss(boss_name, 900, 100, 0, 0, 0, 0, 
                              BossStrings.viv.description)
   
   # Саша Шлякин
   elif boss_name == BossStrings.sasha.name:
      boss = Characters.Boss(boss_name, 1000, 200, 20, 0, 0, 0, 
                              BossStrings.sasha.description)
   
   # Качаловская Тварь
   elif boss_name == BossStrings.tvar.name:
      boss = Characters.Boss(boss_name, 800, 50, 0, 0, 0, 0, 
                              BossStrings.tvar.description)
      boss.returnal_value = 50
   
   # Рандом Рандомыч
   elif boss_name == BossStrings.randomich.name:
      boss = Characters.Boss(boss_name, random.randint(100, 1001), random.randint(10, 301), 
                              random.randint(0, 51), random.randint(0, 51), 0, 
                              random.randint(0, 301), BossStrings.randomich.description)
      boss.returnal_value = random.randint(0, 51)
   
   # Котенок-Тролль
   elif boss_name == BossStrings.kitty.name:
      boss = Characters.Boss(boss_name, 1000, 200, 0, 0, 0, 0, 
                              BossStrings.kitty.description)
      boss.end_skill_chance = 50
   
   # Инквизиция
   elif boss_name == BossStrings.inkvisizia.name:
      boss = Characters.Boss(boss_name, 500, 500, 50, 0, 0, 0, 
                              BossStrings.inkvisizia.description)
   
   # Доктор Леха
   elif boss_name == BossStrings.doc_leha.name:
      boss = Characters.Boss(boss_name, 1500, 300, 0, 0, 0, 0, 
                              BossStrings.doc_leha.description)
      boss.end_skill_chance = 36
   
   # Пьяный Леха
   elif boss_name == BossStrings.drunk_leha.name:
      boss = Characters.Boss(boss_name, 1200, 100, 0, 0, 0, 0, 
                              BossStrings.doc_leha.description)
   
   # Мел
   elif boss_name == BossStrings.mel.name:
      boss = Characters.Boss(boss_name, 50, 0, 0, 90, 0, 0, 
                              BossStrings.mel.description)
   
   # Рыжий
   elif boss_name == BossStrings.redhead.name:
      boss = Characters.Boss(boss_name, 2000, 100, 0, 0, 0, 300, 
                              BossStrings.redhead.description)
   
   # Следователь
   elif boss_name == BossStrings.sledovatel.name:
      boss = Characters.Boss(boss_name, 1500, 100, 0, 50, 0, 0, 
                              BossStrings.redhead.description)
      boss.sledovatel_busted_level = 10
   
   # Донер Кебаб
   elif boss_name == BossStrings.doner.name:
      boss = Characters.Boss(boss_name, 1800, 350, 0, 0, 0, 0, 
                              BossStrings.doner.description)
   
   # Черный Стас
   elif boss_name == BossStrings.black_stas.name:
      boss = Characters.Boss(boss_name, 1500, 300, 0, 0, 0, 0, 
                              BossStrings.black_stas.description)
   
   # Дрон
   elif boss_name == BossStrings.dron.name:
      boss = Characters.Boss(boss_name, 2000, 100, 0, 0, 0, 0, 
                              BossStrings.dron.description)
      boss.dron_obida_level = 5
   
   # Валера Гладиатор
   elif boss_name == BossStrings.glad.name:
      boss = Characters.Boss(boss_name, 3000, 200, 0, 0, 0, 0, 
                              BossStrings.glad.description)
   
   # Великая Шива
   elif boss_name == BossStrings.shiva.name:
      boss = Characters.Boss(boss_name, 2000, 500, 0, 30, 0, 0, 
                              BossStrings.shiva.description)
   
   # Король Макар
   elif boss_name == BossStrings.makar.name:
      boss = Characters.Boss(boss_name, player.health, player.damage, 
                              player.critical_chance, player.miss_chance, 
                              player.lifesteal, player.regeneration,
                              BossStrings.makar.description)
   
   # Гомогомозеки
   elif boss_name == BossStrings.gomozeki.name:
      boss = Characters.Boss(boss_name, 2000, 300, 20, 0, 0, 200, 
                              BossStrings.gomozeki.description)