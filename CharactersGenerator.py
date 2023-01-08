# модуль создания игрока и боссов, функции выбора босса от количества побед игрока, способности боссов перед боем с игроком
import GameStrings
import PlayerStrings
import Characters

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
   global boss

   if boss_name == MyStrings.Text.palich_name.value:
      boss = Characters.Boss(boss_name, 800, 200, 0, 0, 0, 0, MyStrings.Text.palich_description.value)
      
   elif boss_name == MyStrings.Text.chaikovskii_name.value:
      boss = Characters.Boss(boss_name, 600, 250, 0, 0, 0, 0, MyStrings.Text.chaikovskii_description.value)
      boss.resurrection = True

   elif boss_name == MyStrings.Text.viv_name.value:
      boss = Characters.Boss(boss_name, 900, 100, 0, 0, 0, 0, MyStrings.Text.viv_description.value)

   elif boss_name == MyStrings.Text.sasha_name.value:
      boss = Characters.Boss(boss_name, 1000, 200, 20, 0, 0, 0, MyStrings.Text.sasha_description.value)

   elif boss_name == MyStrings.Text.tvar_name.value:
      boss = Characters.Boss(boss_name, 800, 50, 0, 0, 0, 0, MyStrings.Text.tvar_description.value)
      boss.returnal_value = 50

   elif boss_name == MyStrings.Text.randomich_name.value:
      boss = Characters.Boss(boss_name, random.randint(100, 1001), random.randint(10, 301), random.randint(0, 51), random.randint(0, 51), 0, random.randint(0, 301), MyStrings.Text.randomich_description.value)
      boss.returnal_value = random.randint(0, 51)

   elif boss_name == MyStrings.Text.kitty_name.value:
      boss = Characters.Boss(boss_name, 1000, 200, 0, 0, 0, 0, MyStrings.Text.kitty_description.value)
      boss.end_skill_chance = 50

   elif boss_name == MyStrings.Text.inkvisizia_name.value:
      boss = Boss(boss_name, 500, 500, 50, 0, 0, 0, MyStrings.Text.inkvisizia_description.value)

   elif boss_name == MyStrings.Text.doc_leha_name.value:
      boss = Boss(boss_name, 1500, 300, 0, 0, 0, 0, MyStrings.Text.doc_leha_description.value)
      boss.end_skill_chance = 36

   elif boss_name == MyStrings.Text.drunk_leha_name.value:
      boss = Boss(boss_name, 1200, 100, 0, 0, 0, 0, MyStrings.Text.doc_leha_description.value)

   elif boss_name == MyStrings.Text.mel_name.value:
      boss = Boss(boss_name, 50, 0, 0, 90, 0, 0, MyStrings.Text.mel_description.value)

   elif boss_name == MyStrings.Text.redhead_name.value:
      boss = Boss(boss_name, 2000, 100, 0, 0, 0, 300, MyStrings.Text.redhead_description.value)

   elif boss_name == MyStrings.Text.sledovatel_name.value:
      boss = Boss(boss_name, 1500, 100, 0, 50, 0, 0, MyStrings.Text.redhead_description.value)
      boss.sledovatel_busted_level = 10

   elif boss_name == MyStrings.Text.doner_name.value:
      boss = Boss(boss_name, 1800, 350, 0, 0, 0, 0, MyStrings.Text.doner_description.value)

   elif boss_name == MyStrings.Text.black_stas_name.value:
      boss = Boss(boss_name, 1500, 300, 0, 0, 0, 0, MyStrings.Text.black_stas_description.value)

   elif boss_name == MyStrings.Text.dron_name.value:
      boss = Boss(boss_name, 2000, 100, 0, 0, 0, 0, MyStrings.Text.dron_description.value)
      boss.dron_obida_level = 5

   elif boss_name == MyStrings.Text.glad_name.value:
      boss = Boss(boss_name, 3000, 200, 0, 0, 0, 0, MyStrings.Text.glad_description.value)

   elif boss_name == MyStrings.Text.shiva_name.value:
      boss = Boss(boss_name, 2000, 500, 0, 30, 0, 0, MyStrings.Text.shiva_description.value)

   elif boss_name == MyStrings.Text.makar_name.value:
      boss = Boss(boss_name, player.health, player.damage, player.critical_chance, player.miss_chance, player.lifesteal, player.regeneration ,MyStrings.Text.makar_description.value)

   elif boss_name == MyStrings.Text.gomozeki_name.value:
      boss = Boss(boss_name, 2000, 300, 20, 0, 0, 200, MyStrings.Text.gomozeki_description.value)

class BossList():
   list_easy = ['Палыч', 'Чайковский', 'Вив', 'Саша Шлякин', 'Качаловская Тварь', 'Рандом Рандомыч', 'Котенок-тролль']
   list_medium = ['Инквизиция', 'Доктор Леха', 'Пьяный Леха', 'Мел', 'Рыжий', 'Следователь']
   list_hard = ['Донер Кебаб', 'Черный Стас', 'Дрон', 'Валера Гладиатор', 'Великая Шива']

def boss_difficult_choice(x):
   global boss_name

   if x < 3:
      boss_name = random.choice(BossList.list_easy)
      BossList.list_easy.remove(boss_name)
   elif x < 6 and x >= 3:
      boss_name = random.choice(BossList.list_medium)
      BossList.list_medium.remove(boss_name)
   elif x < 9 and x >= 6:
      boss_name = random.choice(BossList.list_hard)
      BossList.list_hard.remove(boss_name)
   elif x == 9:
      boss_name = [MyStrings.Text.makar_name.value]

def boss_prelude_skill_activation(boss_name):
   global prelude_skill_message
   
   prelude_skill_message = False

   if boss_name == MyStrings.Text.palich_name.value:
      player.silence = True
      prelude_skill_message = MyStrings.Text.palich_prelude_text.value

   elif boss_name == MyStrings.Text.redhead_name.value:
      player.poison = True
      prelude_skill_message = MyStrings.Text.redhead_prelude_text.value

   elif boss_name == MyStrings.Text.sledovatel_name.value:
      drugs = MyStrings.Text.marki_name.value, MyStrings.Text.madam_name.value, MyStrings.Text.marki_name.value
      cross_check = [x for x in drugs if x in player.all_items]
      if player.damage > 500:
         player.health_down_procent(50)
         prelude_skill_message = MyStrings.Text.sledovatel_damage_prelude_text.value
      elif player.mitya_elexir_count > 0 or len(cross_check) > 0:
         player.police_level += 50
         prelude_skill_message = MyStrings.Text.sledovatel_drugcheck_text.value
      elif player.damage > 500 and player.mitya_elexir_count > 0 or len(cross_check) > 0:
         player.health_down_procent(50)
         player.police_level += 50
         prelude_skill_message = MyStrings.Text.sledovatel_damage_prelude_text.value + '\n' + MyStrings.Text.sledovatel_drugcheck_text.value

   elif boss_name == MyStrings.Text.dron_name.value:
      obida_level = 0
      obida_level += len(player.all_items) * 5
      prelude_skill_message = MyStrings.Text.dron_bratishki_text.value
      if MyStrings.Text.dron_meat_name.value in player.all_items:
         obida_level += 10
         prelude_skill_message += '\n' + MyStrings.Text.dron_dron_meat_text.value

   elif boss_name == MyStrings.Text.doner_name.value and MyStrings.Text.everlast_name.value in player.all_items:
      boss.health_up_procent(10)
      boss.damage_up_procent(10)
      prelude_skill_message = MyStrings.Text.doner_everlast_text.value

   elif boss_name == MyStrings.Text.black_stas_name.value and player.name == MyStrings.Text.mitya_name.value:
      boss.damage_up(player.mitya_elexir_count * 200)
      prelude_skill_message = MyStrings.Text.black_stas_mitya_text.value