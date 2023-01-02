import random
import MyStrings
import Characters
import BotMessages

class Loot():
   buff_list = ['Сочник со сгухой', 'Гитара', 'Костюм Эверласт', 'Сыграть в шахматы', 'Дубайский шаурмец', 'Мясо Андрея',
                  'Башкерме взрывай', 'Почтовые марки', 'Поиграть на варгане', 'Благословение Шивы', '5 пицц', 'Пика точеная', 
                  'Лимонная голодовочка', 'Огромный дилдак', 'Благословение Макара', 'Черный чупа чупс']
   item_list = ['Жигули', 'Лезвия бритвы', 'Потный носок', 'Шига', 'Святая минералочка', 'Золотые Ролексы', 'Сидр',
                  '2.5-литровка Колы', 'Блевотный харчок', 'Мадам', 'Рампаг', 'Вакцина', 'Балабаха Багбира', 'Травмат Володи']

class Buff():
   def __init__(self, health, damage, critical_chance, miss_chance, lifesteal, description):
      self.health = health
      self.damage = damage
      self.critical_chance = critical_chance
      self.miss_chance = miss_chance
      self.lifesteal = lifesteal
      self.description = description

class Item():
   boss_iteraction_message = False
   char_iteraction_message = False
   def __init__(self, value, description):
      self.value = value
      self.description = description

def shop_enter(x):
   global buff_choice
   global item_choice

   buff_choice = [random.choice(Loot.buff_list), random.choice(Loot.buff_list), random.choice(Loot.buff_list)]
   item_choice = [random.choice(Loot.item_list), random.choice(Loot.item_list), random.choice(Loot.item_list)]
   if x == MyStrings.Text.stas_shop_name.value:
      Characters.char.damage_up(50)
   elif x == MyStrings.Text.bratishki_shop_name.value:
      Characters.char.health_up(200)

def stas_enter(x):
   Characters.char.item = x
   Loot.item_list.remove(x)

def bratishki_enter(x):
   global buff
   Loot.buff_list.remove(x)
   
   if x == MyStrings.Text.sochnik_name.value:
      buff = Buff(20, 0, 0, 0, 0, MyStrings.Text.sochnik_description.value)
      Characters.Char.health_up_procent(Characters.char, buff.health)
   
   elif x == MyStrings.Text.dubai_name.value:
      buff = Buff(30, 0, 0, 0, 0, MyStrings.Text.dubai_description.value)
      Characters.Char.health_up_procent(Characters.char, buff.health)

   elif x == MyStrings.Text.dron_meat_name.value:
      buff = Buff(40, 0, 0, 0, 0, MyStrings.Text.dron_meat_description.value)
      Characters.Char.health_up_procent(Characters.char, buff.health)

   elif x == MyStrings.Text.pizza5_name.value:
      buff = Buff(50, 0, 0, 0, 0, MyStrings.Text.pizza5_description.value)
      Characters.Char.health_up_procent(Characters.char, buff.health)

   elif x == MyStrings.Text.guitar_name.value:
      buff = Buff(0, 15, 0, 0, 0, MyStrings.Text.guitar__description.value)
      Characters.Char.damage_up_procent(Characters.char, buff.damage)

   elif x == MyStrings.Text.bashkerme_name.value:
      buff = Buff(0, 25, 0, 0, 0, MyStrings.Text.bashkerme_description.value)
      Characters.Char.damage_up_procent(Characters.char, buff.damage)

   elif x == MyStrings.Text.pika_name.value:
      buff = Buff(0, 30, 0, 0, 0, MyStrings.Text.pika_description.value)
      Characters.Char.damage_up_procent(Characters.char, buff.damage)

   elif x == MyStrings.Text.dildo_name.value:
      buff = Buff(0, 50, 0, 0, 0, MyStrings.Text.dildo_description.value)
      Characters.Char.damage_up_procent(Characters.char, buff.damage)
   
   elif x == MyStrings.Text.everlast_name.value:
      buff = Buff(10, 10, 0, 0, 0, MyStrings.Text.everlast_description.value)
      Characters.Char.health_up_procent(Characters.char, buff.health)
      Characters.Char.damage_up_procent(Characters.char, buff.damage)

   elif x == MyStrings.Text.marki_name.value:
      buff = Buff(20, 20, 0, 0, 0, MyStrings.Text.marki_description.value)
      Characters.Char.health_up_procent(Characters.char, buff.health)
      Characters.Char.damage_up_procent(Characters.char, buff.damage)

   elif x == MyStrings.Text.limon_name.value:
      buff = Buff(30, 50, 5, 0, 0, MyStrings.Text.limon_description.value)
      Characters.Char.health_down_procent(Characters.char, buff.health)
      Characters.Char.damage_up_procent(Characters.char, buff.damage)
      Characters.Char.critical_chance_up(Characters.char, buff.critical_chance)

   elif x == MyStrings.Text.chess_name.value:
      buff = Buff(0, 0, 5, 0, 0, MyStrings.Text.chess_description.value)
      Characters.Char.critical_chance_up(Characters.char, buff.critical_chance)
   
   elif x == MyStrings.Text.vargan_name.value:
      buff = Buff(0, 0, 10, 0, 0, MyStrings.Text.vargan_description.value)
      Characters.Char.critical_chance_up(Characters.char, buff.critical_chance)

   elif x == MyStrings.Text.choops_name.value:
      buff = Buff(0, 0, 0, 0, 10, MyStrings.Text.choops_description.value)
      Characters.Char.lifesteal_up(Characters.char, buff.lifesteal)

   elif x == MyStrings.Text.shiva_bless_name.value:
      buff = Buff(0, 50, 15, 0, 0, MyStrings.Text.shiva_bless_description.value)
      Characters.Char.damage_up_procent(Characters.char, buff.damage)
      Characters.Char.critical_chance_up(Characters.char, buff.critical_chance)

   elif x == MyStrings.Text.makar_bless_name.value:
      buff = Buff(30, 30, 10, 0, 0, MyStrings.Text.makar_bless_description.value)
      Characters.Char.health_up_procent(Characters.char, buff.health)
      Characters.Char.damage_up_procent(Characters.char, buff.damage)
      Characters.Char.critical_chance_up(Characters.char, buff.critical_chance)

   if x not in Characters.char.all_items:
      Characters.char.all_items.append(x)

def item_activation(item_name):
   global item

   if item_name == MyStrings.Text.zhiguli_name.value:
      item = Item(150, MyStrings.Text.zhiguli_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_booze_text.value
         Characters.boss.health_up(item.value)
      else:
         Characters.char.health_up(item.value)

   elif item_name == MyStrings.Text.sidr_name.value:
      item = Item(300, MyStrings.Text.sidr_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_booze_text.value
         Characters.boss.health_up(item.value)
      else:
         Characters.char.health_up(item.value)

   elif item_name == MyStrings.Text.bagbeer_name.value:
      item = Item(500, MyStrings.Text.bagbeer_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_booze_text.value
         Characters.boss.health_up(item.value)
      else:
         Characters.char.health_up(item.value)

   elif item_name == MyStrings.Text.mineralka_name.value:
      item - Item(100, MyStrings.Text.mineralka_description.value)
      Characters.char.regeneration_up(item.value)

   elif item_name == MyStrings.Text.lezvie_name.value:
      item = Item(150, MyStrings.Text.lezvie_description.value)
      Characters.boss.health_down(item.value)
      Characters.boss.bleeding = True

   elif item_name == MyStrings.Text.travmat_name.value:
      item = Item(300, MyStrings.Text.travmat_description.value)
      if Characters.boss.name == MyStrings.Text.viv_name.value:
         Characters.char.health_down(item.value)
         Characters.char.bleeding = True
         item.boss_iteraction_message = MyStrings.Text.viv_travmat_text.value
      else:
         Characters.boss.health_down(item.value)
         Characters.boss.bleeding = True

   elif item_name == MyStrings.Text.cola_name.value:
      item = Item(500, MyStrings.Text.cola_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         Characters.char.health_down(item.value)
         Characters.boss.health_down(item.value)
         item.boss_iteraction_message = MyStrings.Text.doner_cola_text.value
      else:
         Characters.boss.health_down(item.value)

   elif item_name == MyStrings.Text.sick_sock_name.value:
      item = Item(100, MyStrings.Text.sick_sock_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_sock_text.value
         Characters.boss.health_up(item.value)
         Characters.boss.regeneration_up(item.value)
      else:
         Characters.boss.health_down(item.value)
         Characters.boss.poison = True

   elif item_name == MyStrings.Text.harchok_name.value:
      item = Item(200, MyStrings.Text.harchok_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         Characters.boss.health_up(item.value)
         Characters.boss.regeneration_up(item.value)
      else:
         Characters.boss.health_down(item.value)
         Characters.boss.poison = True

   elif item_name == MyStrings.Text.rampag_name.value:
      item = Item(1, MyStrings.Text.rampag_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_rampag_text.value
         Characters.boss.health = 0
      else:
         Characters.boss.stan_timer = 1

   elif item_name == MyStrings.Text.rolex_name.value:
      item = Item(0, MyStrings.Text.rolex_description.value)
      Characters.char.cooldown = item.value

   elif item_name == MyStrings.Text.vaccine_name.value:
      item = Item(0, MyStrings.Text.vaccine_description.value)
      Characters.char.poison = False
      Characters.char.bleeding = False

   elif item_name == MyStrings.Text.shiga_name.value:
      item = Item(30, False)
      foods = MyStrings.Text.sochnik_name.value, MyStrings.Text.dubai_name.value, MyStrings.Text.dron_meat_name.value, MyStrings.Text.pizza5_name.value
      cross_check = [x for x in foods if x in Characters.char.all_items]
      if len(cross_check) == 0:
         Characters.char.health_down_procent(item.value)
         Characters.char.damage_up_procent(item.value)
         item.description = MyStrings.Text.shiga_debuff_description.value
      elif len(cross_check) > 0:
         Characters.char.health_up_procent(item.value)
         Characters.char.damage_up_procent(item.value)
         item.description = MyStrings.Text.shiga_buff_description.value

   elif item_name == MyStrings.Text.madam_name.value:
      item = Item(50, MyStrings.Text.madam_description.value)
      Characters.boss.damage_down_procent(item.value)
      