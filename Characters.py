import MyStrings
class Pers():
   def __init__(self, name, hp, dmg, crit, miss, vamp):
      self.name = name
      self.hp = hp
      self.dmg = dmg
      self.crit = crit
      self.miss = miss
      self.vamp = vamp
   def hp_debaff(self, value):
      self.hp -= value
   def hp_baff(self, value):
      self.hp += value
   def dmg_debaff(self, value):
      self.dmg -= value
   def dmg_baff(self, value):
      self.dmg += value
   def crit_baff(self, value):
      self.crit += value
   def crit_debaff(self, value):
      self.crit -= value

class Char(Pers):
   def __init__(self, name, hp, dmg, crit, miss, vamp, description, skill_name, icon):
      super().__init__(name, hp, dmg, crit, miss, vamp)
      self.item = 'Пусто'
      self.all_items = []
      self.stan_timer = 0
      self.cooldown = 0
      self.regen = 0
      self.busted_level = 0
      self.elex_count = 0
      self.sueta_count = 0
      self.poison = False
      self.bleeding = False
      self.silence = False
      self.immunity = False
      self.description = description
      self.skill_name = skill_name
      self.icon = icon

class Boss(Pers):
   def __init__(self, name, hp, dmg, crit, miss, vamp, dscr):
      super().__init__(name, hp, dmg, crit, miss, vamp)
      self.endskill_value = 0
      self.returnal_value = 0
      self.regen = 0
      self.stan_timer = 0
      self.blazer_level = 0
      self.busted_level = 0
      self.obida_level = 0
      self.resurrection = False
      self.bleeding = False
      self.poison = False
      self.dscr = dscr
      self.icon = '👿'
   
class BossList():
   def __init__(self, aboba):
      self.list_easy = ['Палыч', 'Чайковский', 'Вив', 'Саша Шлякин', 'Качаловская Тварь', 'Рандом Рандомыч', 'Котенок-тролль']
      self.list_medium = ['Инквизиция', 'Доктор Леха', 'Пьяный Леха', 'Мел', 'Рыжий', 'Следователь']
      self.list_hard = ['Донер Кебаб', 'Черный Стас', 'Дрон', 'Валера Гладиатор', 'Великая Шива']
      self.aboba = aboba



def Char_get_stats(x):
   global char

   if x == MyStrings.Text.mitya_name.value:
      char = Char(MyStrings.Text.mitya_name.value, 800, 100, 0, 0, 20, MyStrings.Text.mitya_description_text.value, MyStrings.Text.mitya_skill_button_text.value, MyStrings.Text.mitya_icon.value)
      
   elif x == MyStrings.Text.sanya_name.value:
      char = Char(MyStrings.Text.sanya_name.value, 1000, 200, 30, 0, 0, MyStrings.Text.sanya_description_text.value, MyStrings.Text.sanya_skill_button_text.value, MyStrings.Text.sanya_icon.value)
      
   elif x == MyStrings.Text.toshik_name.value:
      char = Char(MyStrings.Text.toshik_name.value, 1500, 100, 0, 0, 0, MyStrings.Text.temich_description_text.value, MyStrings.Text.toshik_skill_button_text.value, MyStrings.Text.toshik_icon.value)
      
   elif x == MyStrings.Text.kolya_name.value:
      char = Char(MyStrings.Text.kolya_name.value, 1200, 100, 0, 0, 0, MyStrings.Text.kolya_description_text.value, MyStrings.Text.kolya_skill_button_text.value, MyStrings.Text.kolya_icon.value)
      
   elif x == MyStrings.Text.temich_name.value:
      char = Char(MyStrings.Text.temich_name.value, 800, 150, 0, 15, 0, MyStrings.Text.temich_description_text.value, MyStrings.Text.temich_skill_button_text.value, MyStrings.Text.temich_icon.value)

class Message_text():
   def char_stats_message():
      return char.name + char.icon + '\n' + char.description