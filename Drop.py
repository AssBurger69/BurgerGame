import random

class Loot():
   def __init__(self, dscr):
      self.dscr = dscr
      self.buff_list = ['Сочник со сгухой', 'Гитара', 'Костюм Эверласт', 'Сыграть в шахматы', 'Дубайский шаурмец', 'Мясо Андрея',
                  'Башкерме взрывай', 'Почтовые марки', 'Поиграть на варгане', 'Благословение Шивы', '5 пицц', 'Пика точеная', 
                  'Лимонная голодовочка', 'Огромный дилдак', 'Благословение Макара', 'Черный чупа чупс']
      self.item_list = ['Жигули', 'Лезвия бритвы', 'Потный носок', 'Шига', 'Святая минералочка', 'Золотые Ролексы', 'Сидр',
                  '2.5-литровка Колы', 'Блевотный харчок', 'Мадам', 'Рампаг', 'Вакцина', 'Балабаха Багбира', 'Травмат Володи']

class Buff(Loot):
   def __init__(self, value_1, dscr):
      super().__init__(dscr)
      self.value_1 = value_1

class SuperBuff(Buff):
   def __init__(self, value_1, value_2, dscr):
      super().__init__(value_1, dscr)
      self.value_2 = value_2

class UltraBuff(SuperBuff):
   def __init__(self, value_1, value_2, value_3, dscr):
      super().__init__(value_1, value_2, dscr)
      self.value_3 = value_3

class Item(Loot):
   def __init__(self, dscr):
      super().__init__(dscr)
      