import MyStrings
import random

class Pers():
   poison_dmg = 10
   win_rate = 0
   wanted_level = False

   def __init__(self, name, health, damage, critical_chance, miss_chance, lifesteal, regeneration, description):
      self.name = name
      self.health = health
      self.damage = damage
      self.critical_chance = critical_chance
      self.miss_chance = miss_chance
      self.lifesteal = lifesteal
      self.regeneration = regeneration
      self.description = description

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
      print(self.damage)

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

class Char(Pers):
   item = 'Пусто'
   all_items = []
   stan_timer = 0
   cooldown = 0
   busted_level = 0
   elex_count = 0
   sueta_count = 0
   poison = False
   bleeding = False
   silence = False
   immunity = False

   def __init__(self, name, health, damage, critical_chance, miss_chance, lifesteal, regeneration, description, skill_name, icon):
      super().__init__(name, health, damage, critical_chance, miss_chance, lifesteal, regeneration, description)
      self.skill_name = skill_name
      self.icon = icon

class Boss(Pers):
   endskill_value = 0
   returnal_value = 0
   regen = 0
   stan_timer = 0
   blazer_level = 0
   busted_level = 0
   obida_level = 0
   resurrection = False
   bleeding = False
   poison = False
   icon = MyStrings.Text.boss_icon.value
   
   def __init__(self, name, health, damage, critical_chance, miss_chance, lifesteal,regeneration ,description):
      super().__init__(name, health, damage, critical_chance, miss_chance, lifesteal, regeneration, description)
   
class BossList():
   list_easy = ['Палыч', 'Чайковский', 'Вив', 'Саша Шлякин', 'Качаловская Тварь', 'Рандом Рандомыч', 'Котенок-тролль']
   list_medium = ['Инквизиция', 'Доктор Леха', 'Пьяный Леха', 'Мел', 'Рыжий', 'Следователь']
   list_hard = ['Донер Кебаб', 'Черный Стас', 'Дрон', 'Валера Гладиатор', 'Великая Шива']

def char_get_stats(x):
   global char

   if x == MyStrings.Text.mitya_name.value:
      char = Char(MyStrings.Text.mitya_name.value, 800, 100, 0, 0, 20, 0, MyStrings.Text.mitya_description_text.value, MyStrings.Text.mitya_skill_button_text.value, MyStrings.Text.mitya_icon.value)
      
   elif x == MyStrings.Text.sanya_name.value:
      char = Char(MyStrings.Text.sanya_name.value, 1000, 200, 30, 0, 0, 0, MyStrings.Text.sanya_description_text.value, MyStrings.Text.sanya_skill_button_text.value, MyStrings.Text.sanya_icon.value)
      
   elif x == MyStrings.Text.toshik_name.value:
      char = Char(MyStrings.Text.toshik_name.value, 1500, 100, 0, 0, 0, 0, MyStrings.Text.temich_description_text.value, MyStrings.Text.toshik_skill_button_text.value, MyStrings.Text.toshik_icon.value)
      
   elif x == MyStrings.Text.kolya_name.value:
      char = Char(MyStrings.Text.kolya_name.value, 1200, 100, 0, 0, 0, 0, MyStrings.Text.kolya_description_text.value, MyStrings.Text.kolya_skill_button_text.value, MyStrings.Text.kolya_icon.value)
      
   elif x == MyStrings.Text.temich_name.value:
      char = Char(MyStrings.Text.temich_name.value, 800, 150, 0, 15, 0, 0, MyStrings.Text.temich_description_text.value, MyStrings.Text.temich_skill_button_text.value, MyStrings.Text.temich_icon.value)

def boss_get_stats(x):
   global boss

   if x == MyStrings.Text.palich_name.value:
      boss = Boss(x, 800, 200, 0, 0, 0, 0, MyStrings.Text.palich_description.value)
      
   elif x == MyStrings.Text.chaikovskii_name.value:
      boss = Boss(x, 600, 250, 0, 0, 0, 0, MyStrings.Text.chaikovskii_description.value)
      boss.resurrection = True

   elif x == MyStrings.Text.viv_name.value:
      boss = Boss(x, 900, 100, 0, 0, 0, 0, MyStrings.Text.viv_description.value)

   elif x == MyStrings.Text.sasha_name.value:
      boss = Boss(x, 1000, 200, 20, 0, 0, 0, MyStrings.Text.sasha_description.value)

   elif x == MyStrings.Text.tvar_name.value:
      boss = Boss(x, 800, 50, 0, 0, 0, 0, MyStrings.Text.tvar_description.value)
      boss.returnal_value = 50

   elif x == MyStrings.Text.randomich_name.value:
      boss = Boss(x, random.randint(100, 1001), random.randint(10, 301), random.randint(0, 51), random.randint(0, 51), 0, random.randint(0, 301), MyStrings.Text.randomich_description.value)
      boss.returnal_value = random.randint(0, 51)

   elif x == MyStrings.Text.kitty_name.value:
      boss = Boss(x, 1000, 200, 0, 0, 0, 0, MyStrings.Text.kitty_description.value)
      boss.endskill_value = 50

   elif x == MyStrings.Text.inkvisizia_name.value:
      boss = Boss(x, 500, 500, 50, 0, 0, 0, MyStrings.Text.inkvisizia_description.value)

   elif x == MyStrings.Text.doc_leha_name.value:
      boss = Boss(x, 1500, 300, 0, 0, 0, 0, MyStrings.Text.doc_leha_description.value)
      boss.endskill_value = 36

   elif x == MyStrings.Text.drunk_leha_name.value:
      boss = Boss(x, 1200, 100, 0, 0, 0, 0, MyStrings.Text.doc_leha_description.value)

   elif x == MyStrings.Text.mel_name.value:
      boss = Boss(x, 50, 0, 0, 90, 0, 0, MyStrings.Text.mel_description.value)

   elif x == MyStrings.Text.redhead_name.value:
      boss = Boss(x, 2000, 100, 0, 0, 0, 300, MyStrings.Text.redhead_description.value)

   elif x == MyStrings.Text.sledovatel_name.value:
      boss = Boss(x, 1500, 100, 0, 50, 0, 0, MyStrings.Text.redhead_description.value)
      boss.busted_level = 10

   elif x == MyStrings.Text.doner_name.value:
      boss = Boss(x, 1800, 350, 0, 0, 0, 0, MyStrings.Text.doner_description.value)

   elif x == MyStrings.Text.black_stas_name.value:
      boss = Boss(x, 1500, 300, 0, 0, 0, 0, MyStrings.Text.black_stas_description.value)

   elif x == MyStrings.Text.dron_name.value:
      boss = Boss(x, 2000, 100, 0, 0, 0, 0, MyStrings.Text.dron_description.value)
      boss.obida_level = 5

   elif x == MyStrings.Text.glad_name.value:
      boss = Boss(x, 3000, 200, 0, 0, 0, 0, MyStrings.Text.glad_description.value)

   elif x == MyStrings.Text.shiva_name.value:
      boss = Boss(x, 2000, 500, 0, 30, 0, 0, MyStrings.Text.shiva_description.value)

   elif x == MyStrings.Text.makar_name.value:
      boss = Boss(x, char.health, char.damage, char.critical_chance, char.miss_chance, char.lifesteal, char.regeneration ,MyStrings.Text.makar_description.value)

   elif x == MyStrings.Text.gomozeki_name.value:
      boss = Boss(x, 2000, 300, 20, 0, 0, 200, MyStrings.Text.gomozeki_description.value)

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

def boss_prelude_skill_activation(x):
   global prelude_skill_message
   
   prelude_skill_message = False

   if x == MyStrings.Text.palich_name.value:
      char.silence = True
      prelude_skill_message = MyStrings.Text.palich_prelude_text.value

   elif boss.name == MyStrings.Text.redhead_name.value:
      char.poison = True
      prelude_skill_message = MyStrings.Text.redhead_prelude_text.value

   elif boss.name == MyStrings.Text.sledovatel_name.value:
      drugs = MyStrings.Text.marki_name.value, MyStrings.Text.madam_name.value, MyStrings.Text.marki_name.value
      cross_check = [x for x in drugs if x in char.all_items]
      if char.damage > 500:
         char.health_down_procent(50)
         prelude_skill_message = MyStrings.Text.sledovatel_damage_prelude_text.value
      elif char.elex_count > 0 or len(cross_check) > 0:
         char.busted_level += 50
         prelude_skill_message = MyStrings.Text.sledovatel_drugcheck_text.value
      elif char.damage > 500 and char.elex_count > 0 or len(cross_check) > 0:
         char.health_down_procent(50)
         char.busted_level += 50
         prelude_skill_message = MyStrings.Text.sledovatel_damage_prelude_text.value + '\n' + MyStrings.Text.sledovatel_drugcheck_text.value

   elif boss.name == MyStrings.Text.dron_name.value:
      obida_level = 0
      obida_level += len(char.all_items) * 5
      prelude_skill_message = MyStrings.Text.dron_bratishki_text.value
      if MyStrings.Text.dron_meat_name.value in char.all_items:
         obida_level += 10
         prelude_skill_message += '\n' + MyStrings.Text.dron_dron_meat_text.value

   elif boss.name == MyStrings.Text.doner_name.value and MyStrings.Text.everlast_name.value in char.all_items:
      boss.health_up_procent(10)
      boss.damage_up_procent(10)
      prelude_skill_message = MyStrings.Text.doner_everlast_text.value

   elif boss.name == MyStrings.Text.black_stas_name.value and char.name == MyStrings.Text.mitya_name.value:
      boss.damage_up(char.elex_count * 200)
      prelude_skill_message = MyStrings.Text.black_stas_mitya_text.value
