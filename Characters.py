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