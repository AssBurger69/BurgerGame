# -*- coding: utf-8 -*-

from telebot import TeleBot
from telebot import types
import random
import Characters
import Drop
import Locations
import MyStrings
import BotMessages
bot = TeleBot('2102427745:AAECFy-T6GfMWH1VNshsucAEXZEfzmGUZBk')

def chance(x):
   #генератор вероятности
   chance = random.randint(1, 100) in range(1, x)
   return chance

def stas_passive(x):
   #чек на возвращение урона Черного Стаса
   return_check = boss.name == MyStrings.Text.black_stas_name.value and chance(x) == True
   return return_check
   
def versus_stats(x, y):
   #отображение статистики боя
   str1 = char.icon + x + ' 🆚 ' + y + boss.icon
   str2 = '❤️' + str(char.hp)
   str3 = '🖤' + str(boss.hp)
   str4 = '⚔️' + str(char.dmg)
   str5 = '⚔️' + str(boss.dmg)
   z = len(str2) - len(str3)
   indent1 = ' ' * 8
   indent2 = ' ' * (8 + z)
   result = str1 + '\n' + str2 + indent1 + str3 + '\n' + str4 + indent2 + str5
   return result

def bleeding(message):
   #кровотечение
   if char.bleeding == True and char.immunity == False:
      char.hp_debaff(100)
      bot.send_message(message.from_user.id, '🩸Кровотечение🩸\n' + char.icon + '-100❤️')

   elif boss.bleeding == True:
      boss.hp_debaff(100)
      bot.send_message(message.from_user.id, '🩸Кровотечение🩸\n' + boss.icon + '-100🖤')

def poison(message):
   #яд
   if char.poison == True and char.immunity == False:
      char.hp -= char.hp * parameters.poison_dmg // 100
      bot.send_message(message.from_user.id, '🦠Отравление🦠\n-' + str(parameters.poison_dmg) + '%❤️')
      parameters.poison_dmg += 10
   if boss.poison == True:
      boss.hp -= boss.hp * parameters.poison_dmg // 100
      bot.send_message(message.from_user.id, '🦠Отравление🦠\n-' + str(parameters.poison_dmg) + '%🖤')
      parameters.poison_dmg += 10

def regeneration(message):
   if char.regen > 0:
      char.hp_baff(char.regen)
      bot.send_message(message.from_user.id, '💕Регенерация💕\n' + char.icon + '+' + str(char.regen) + '❤️')
   if boss.regen > 0:
      boss.hp_baff(boss.regen)
      bot.send_message(message.from_user.id, '💕Регенерация💕\n' + boss.icon + '+' + str(boss.regen) + '🖤')

@bot.message_handler(content_types=['text'])

def get_character(message):
   # приветственное сообщение
   bot.send_message(message.from_user.id, MyStrings.Text.hello_text.value)
   
   # клавиатура с кнопками и переходом на следующий шаг
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.mitya_name.value, MyStrings.Text.sanya_name.value, MyStrings.Text.toshik_name.value, MyStrings.Text.kolya_name.value, MyStrings.Text.temich_name.value)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.char_choice_text.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, char_creation)

def char_creation(message):
   # Создание персонажа
   Characters.char_get_stats(message.text)

   # Сообщение с характеристиками персонажа
   bot.send_message(message.from_user.id, BotMessages.Message_text.char_description_message())

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.ready_key_text.value, MyStrings.Text.another_char_key_text.value)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.char_choice_question.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, shop_choice)

def shop_choice(message):
   # выбор магазина
   if message.text == MyStrings.Text.another_char_key_text.value:
      bot.send_message(message.from_user.id, MyStrings.Text.give_answer_text.value)
      bot.register_next_step_handler(message, get_character)
   elif message.text == MyStrings.Text.ready_key_text.value or MyStrings.Text.victory_button_text.value:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(MyStrings.Text.stas_shop_name.value, MyStrings.Text.bratishki_shop_name.value)
      msg = bot.send_message(message.from_user.id, text = MyStrings.Text.shop_choice_text.value, reply_markup=keyboard)
      bot.register_next_step_handler(msg, shop)

def shop(message):
   #применение свойства магазина на персонажа
   Drop.shop_enter(message.text)

   if message.text == MyStrings.Text.stas_shop_name.value:
      bot.send_message(message.from_user.id, MyStrings.Text.stas_shop_description.value)
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(Drop.item_choice[0], Drop.item_choice[1], Drop.item_choice[2])
      msg = bot.send_message(message.from_user.id, text = MyStrings.Text.item_choice_text.value, reply_markup=keyboard)
      bot.register_next_step_handler(msg, items_upgrade)

   elif message.text == MyStrings.Text.bratishki_shop_name.value:
      bot.send_message(message.from_user.id, MyStrings.Text.bratishki_shop_description.value)
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(Drop.buff_choice[0], Drop.buff_choice[1], Drop.buff_choice[2])
      msg = bot.send_message(message.from_user.id, text = MyStrings.Text.item_choice_text.value, reply_markup=keyboard)
      bot.register_next_step_handler(msg, stats_upgrade)

def items_upgrade(message):
   #обновление предмета персонажа если он пошел к Стасу
   Drop.stas_enter(message.text)
   
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.boss_choice_question.value)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.stas_bye_text.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_choice)

def stats_upgrade(message):
   # обновление статов персонажа от выбранного предмета если он пошел к Братишкам
   Drop.bratishki_enter(message.text)
   # сообщение с описанием предмета
   bot.send_message(message.from_user.id, Drop.buff.description)

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.boss_choice_question.value)
   msg = bot.send_message(message.from_user.id, text = BotMessages.Message_text.char_stats_message(), reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_choice)

def boss_choice(message):
   #выбор уровня сложности босса в зависимости от побед
   Characters.boss_difficult_choice(Characters.Char.win_rate)

   Characters.boss_get_stats(Characters.boss_name)

   #проверка в розыске ли персонаж
   if Characters.Char.wanted_level == True:
      Characters.Boss.resurrection = True
      bot.send_message(message.from_user.id, MyStrings.Text.boss_police_upgrade_text.value)

   #проверка на является ли персонаж Сашей Шлякиным при битве с Сашей Шлякиным
   if Characters.boss.name == MyStrings.Text.sasha_name.value and Characters.char.name != MyStrings.Text.sanya_name.value:
      bot.send_message(message.from_user.id, MyStrings.Text.sasha_bye_text.value)
      boss_choice(message)
   else:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(MyStrings.Text.location_choice_question.value)
      msg = bot.send_message(message.from_user.id, text = BotMessages.Message_text.boss_stats_message(), reply_markup=keyboard)
      bot.register_next_step_handler(msg, location)

def police_check(message):
   #применение свойств повышенного до 100% уровня полиции

   char.busted_level = 0

   if message.text == MyStrings.Text.go_to_jail_button_text.value:
      char.hp_baff(random.randint(-500,500))
      char.dmg_baff(random.randint(-200,200))
      char.crit_baff(random.randint(-20,20))
      msg_text_1 = MyStrings.Text.jail_effect_text.value
      msg_text_2 = MyStrings.Text.jail_reply_button_text

   elif message.text == MyStrings.Text.run_away_button_text.value:
      parameters.wanted_level = True
      msg_text_1 = MyStrings.Text.run_away_effect_text.value
      msg_text_2 = MyStrings.Text.run_away_reply_button_text.value

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(msg_text_2)
   msg = bot.send_message(message.from_user.id, text = msg_text_1, reply_markup=keyboard)
   bot.register_next_step_handler(msg, shop_choice)

def location(message):
   #выбор локации, применение ее свойств и вывод ее описания
   Locations.location_choice(Locations.Location.location_name)

   bot.send_message(message.from_user.id, BotMessages.Message_text.location_description_message())
   if Locations.Location.pers_iteraction_message != False:
      bot.send_message(message.from_user.id, Locations.Location.pers_iteraction_message)

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.get_fight_button_text.value)
   msg = bot.send_message(message.from_user.id, text = BotMessages.Message_text.char_stats_message(), reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_prelude)

def boss_prelude(message):
   #описание первого скилла босса перед началом боя
   x = False

def start_fight(message):
   #выбор действия игрока в начале раунда боя
   
   if char.busted_level >= 100:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(MyStrings.Text.go_to_jail_button_text.value, MyStrings.Text.run_away_button_text.value)
      msg = bot.send_message(message.from_user.id, text = MyStrings.Text.busted_text.value, reply_markup=keyboard)
      bot.register_next_step_handler(msg, police_check)

   else:
      boss_startskill(message)

      bot.send_message(message.from_user.id, versus_stats(char.name, boss.name))

      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(MyStrings.Text.attack_button_text.value, char.skill_name, char.item)
      msg = bot.send_message(message.from_user.id, text = MyStrings.Text.start_turn_text.value, reply_markup=keyboard)
      bot.register_next_step_handler(msg, action_choice)

def action_choice(message):
   #применение выбранного игроком действия

   if message.text == MyStrings.Text.attack_button_text.value:
      attack_turn(message)

   elif message.text == char.skill_name:
      if char.cooldown <= 0 and char.silence == False and char.stan_timer <= 0:
         char.cooldown = 0
         skill(char.name)
         bot.send_message(message.from_user.id, skill_description)
      elif char.stan_timer > 0:
         bot.send_message(message.from_user.id, MyStrings.Text.char_stan_text.value)
      elif char.silence == True:
         bot.send_message(message.from_user.id, MyStrings.Text.char_silence_text.value)
      elif char.cooldown > 0:
         bot.send_message(message.from_user.id, MyStrings.Text.cooldown_text.value)
      victory_check(message)

   elif message.text == char.item:
      if char.item != MyStrings.Text.empty_text.value and char.silence == False and char.stan_timer <= 0:
         item_using(char.item)
         char.item = MyStrings.Text.empty_text.value
         bot.send_message(message.from_user.id, item_dscr)
      elif char.stan_timer > 0:
         bot.send_message(message.from_user.id, MyStrings.Text.char_stan_text.value)
      elif char.item != MyStrings.Text.empty_text.value and char.silence == True:
         bot.send_message(message.from_user.id, MyStrings.Text.char_silence_text.value)
      elif char.item == MyStrings.Text.empty_text.value:
         bot.send_message(message.from_user.id, MyStrings.Text.empty_click_text.value)   
      victory_check(message)

def attack_turn(message):

   char.cooldown -= 1

   #проверка на уворот босса
   if chance(boss.miss) == True:
      b_m_indent = ' ' * 9 + str(boss.miss) + '%'
      if boss.name == MyStrings.Text.mel_name.value:
         boss.blazer_level += 1
         bot.send_message(message.from_user.id, MyStrings.Text.mel_miss_text.value)
         bot.send_message(message.from_user.id, MyStrings.Text.miss_text.value + b_m_indent)
      else:
         bot.send_message(message.from_user.id, MyStrings.Text.boss_miss_text.value)
         bot.send_message(message.from_user.id, MyStrings.Text.miss_text.value + b_m_indent)

   #проверка на пассивку Стаса
   elif stas_passive(30) == True:
      char.hp -= char.dmg
      bot.send_message(message.from_user.id, 'Стас отразил твою хуйню\n' + char.icon + '-' + str(char.dmg) + '❤️')
      
   #пошаговый процесс одного раунда
   else:
      if char.stan_timer > 0:
         char.stan_timer -= 1
         bot.send_message(message.from_user.id, char.name + ' недееспособен\n        💤Стан💤')
      elif char.stan_timer <= 0:
         char_attack(message)
         vampire(message)
         boss_returnal(message)
      if boss.stan_timer > 0:
         boss.stan_timer -= 1
         bot.send_message(message.from_user.id, boss.name + ' недееспособен\n        💤Стан💤')
      elif boss.stan_timer <= 0:
         boss_attack(message)

   boss_endskill(message)
   bleeding(message)
   poison(message)
   regeneration(message)

   #особые навыки босса в конце раунда
   if boss.name == MyStrings.Text.dron_name.value:
      boss.obida_level += 5
   elif boss.name == MyStrings.Text.sledovatel_name.value:
      char.busted_level += 20

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.end_turn_button_text.value)
   msg = bot.send_message(message.from_user.id, versus_stats(char.name, boss.name), reply_markup=keyboard)
   bot.register_next_step_handler(msg, victory_check)
      
def skill(x):
   #использование скилла персонажа
   global skill_description

   if x == MyStrings.Text.mitya_name.value:
      char.hp_debaff(100)
      char.dmg_baff(200)
      char.cooldown = 1
      char.elex_count += 1
      skill_description = MyStrings.Text.mitya_skill_effect_text.value

   elif x == MyStrings.Text.sanya_name.value:
      damage = random.randint(50, 500)
      boss.hp_debaff(damage)
      char.cooldown = 3
      skill_description = boss.icon + '-' + str(damage) + MyStrings.Text.sanya_skill_effect_text.value

   elif x == MyStrings.Text.toshik_name.value:
      char.hp += char.hp * 20 // 100
      char.cooldown = 2
      skill_description = MyStrings.Text.toshik_skill_effect_text.value

   elif x == MyStrings.Text.kolya_name.value:
      hack_value = boss.dmg * 50 // 100
      char.dmg += hack_value
      boss.dmg -= hack_value
      char.cooldown = 3
      skill_description = boss.icon + '-' + str(hack_value) + '⚔️\n' + char.icon + '+' + str(hack_value) + MyStrings.Text.kolya_skill_effect_text.value

   elif x == MyStrings.Text.temich_name.value:
      skill_check_temich = chance(21)
      if skill_check_temich == False:
         boss.hp, char.hp = char.hp, boss.hp
         char.cooldown = 1
         skill_description = MyStrings.Text.temich_skill_effect_text.value
      elif skill_check_temich == True:
         char.stan_timer = 1
         skill_description = MyStrings.Text.temich_skill_deffect_text.value + char.icon + '+💤'

def item_using(x):
   #использование предмета персонажа
   x = False

def boss_startskill(message):
   #вывод сообщения о примененном навыке босса в конце раунда
   if boss.name == MyStrings.Text.sledovatel_name.value:
      bot.send_message(message.from_user.id, '⛓Степень упаковки ' + str(char.busted_level) + '%⛓')
   
   elif boss.name == MyStrings.Text.dron_name.value:
      bot.send_message(message.from_user.id, '🤬Риск обиды ' + str(boss.obida_level) + '%🤬')

def char_attack(message):
   #атака персонажа
   global char_attack_damage

   if chance(char.crit) == True:
      char_attack_damage = char.dmg * 2
      boss.hp_debaff(char_attack_damage)
      bot.send_message(message.from_user.id, '💥Критический урон!💥\n' + '👿-' + str(char.dmg * 2) + '🖤')

   else:
      char_attack_damage = char.dmg
      boss.hp_debaff(char_attack_damage)
      bot.send_message(message.from_user.id, '👿-' + str(char.dmg) + '🖤')

def boss_returnal(message):
   #проверка на обратку босса
   if boss.returnal_value > 0:
      returnal_damage = char_attack_damage * boss.returnal_value // 100
      char.hp_debaff(returnal_damage)
      b_r_indent = ' ' * 10 + str(boss.returnal_value) + '%\n'
      bot.send_message(message.from_user.id, '🤕Обратка🤕\n' + b_r_indent + char.icon + '-' + str(returnal_damage) + '❤️')

def boss_attack(message):
   #атака босса
   if char.name == MyStrings.Text.mitya_name.value and boss.name == MyStrings.Text.inkvisizia_name.value:
      char.hp += char.hp * 50 // 100
      bot.send_message(message.from_user.id, MyStrings.Text.mitya_inkvisizia_text.value)
   
   else:
      if chance(char.miss) == True:
         c_m_indent = ' ' * 9 + str(char.miss) + '%'
         bot.send_message(message.from_user.id, char.name + ' скользкий тип\n')
         bot.send_message(message.from_user.id, '🛡Уворотка🛡\n' + c_m_indent)

      elif chance(boss.crit) == True:
         char.hp_debaff(boss.dmg * 2)
         bot.send_message(message.from_user.id, '💥Критический урон!💥\n' + char.icon + '-' + str(boss.dmg * 2) + '❤️')

      elif chance(boss.crit) == False:
         char.hp_debaff(boss.dmg)
         bot.send_message(message.from_user.id, char.icon + '-' + str(boss.dmg) + '❤️')

def vampire(message):
   #проверка на вампиризм
   if char.vamp > 0:
      vampire_value = char_attack_damage * char.vamp // 100
      char.hp_baff(vampire_value)
      v_indent = ' ' * 11 + str(char.vamp) + '%\n'
      bot.send_message(message.from_user.id, '🦇Вампирик🦇\n' + v_indent + char.icon + '+' + str(vampire_value) + '❤️')

def boss_endskill(message):  
   #применение скилла босса в конце раунда

   if boss.name == MyStrings.Text.chaikovskii_name.value and boss.resurrection == True and boss.hp <= 200:
      boss.resurrection = False
      boss.hp_baff(800)
      bot.send_message(message.from_user.id, 'Брат! Не засыпай!\n' + boss.icon + '+800🖤')
   
   elif boss.name == MyStrings.Text.viv_name.value:
      boss.dmg_baff(100)
      bot.send_message(message.from_user.id, 'Бассы подъехали!\n' + boss.icon + '+100⚔️')

   elif boss.name == MyStrings.Text.kitty_name.value and chance(boss.endskill_value) == True:
      kitty_choice = random.randint(0, 11)
      if kitty_choice > 5:
         char.stan_timer = 1
         bot.send_message(message.from_user.id, 'Мурлы-сна!\n' + char.icon + '+💤')
      elif kitty_choice <= 5:
         char.hp_debaff(200)
         char.bleeding = True
         bot.send_message(message.from_user.id, 'Зацепка когтями!\n' + char.icon + '-200❤️🩸')
   
   elif boss.name == MyStrings.Text.drunk_leha_name.value:
      boss.hp += boss.hp * 50 // 100
      boss.dmg += boss.dmg * 50 // 100
      bot.send_message(message.from_user.id, MyStrings.Text.drunk_leha_skill_text.value + boss.icon + '+50%🖤 и +50%⚔️')

   elif boss.name == MyStrings.Text.doc_leha_name.value and chance(boss.endskill_value) == True:
      char.hp_debaff(500)
      char.bleeding = True
      bot.send_message(message.from_user.id, MyStrings.Text.doc_leha_skill_text.value + char.icon + '-500❤️🩸')

   elif boss.name == MyStrings.Text.mel_name.value and boss.blazer_level >= 3:
      boss.blazer_level = 0
      char.hp_debaff(500)
      bot.send_message(message.from_user.id, MyStrings.Text.mel_skill_text.value + char.icon + '-500❤️')

   elif boss.name == MyStrings.Text.dron_name.value:
      if chance(boss.obida_level) == True:
         char.hp_debaff(1000)
         bot.send_message(message.from_user.id, MyStrings.Text.dron_skill_text.value)

   elif boss.name == MyStrings.Text.glad_name.value:
      gadza_choice = random.randint(1, 6)
      if gadza_choice == 1:
         char.hp_debaff(500)
         bot.send_message(message.from_user.id, MyStrings.Text.glad_turbo_text.value + char.icon + '-500❤️')
      elif gadza_choice == 2:
         boss.hp_baff(500)
         bot.send_message(message.from_user.id, MyStrings.Text.glad_church_text.value + boss.icon + '+500🖤')
      elif gadza_choice == 3:
         boss.crit_baff(25)
         bot.send_message(message.from_user.id, MyStrings.Text.glad_cat_text.value + boss.icon + '+25%💥')
      elif gadza_choice == 4:
         char.dmg_debaff(250)
         bot.send_message(message.from_user.id, MyStrings.Text.glad_elf_text.value + char.icon + '-250⚔️')
      elif gadza_choice == 5:
         char.poison = True
         bot.send_message(message.from_user.id, MyStrings.Text.glad_poison_text.value + char.icon + '+🦠')

   elif boss.name == MyStrings.Text.shiva_name.value:
      if boss.crit < 100:
         boss.crit_baff(20)
         bot.send_message(message.from_user.id, MyStrings.Text.shiva_crit_buff_text.value + boss.icon + '+20%💥')
      elif boss.crit == 100:
         boss.dmg_baff(boss.dmg * 2)
         bot.send_message(message.from_user.id, MyStrings.Text.shiva_damage_buff_text.value + boss.icon + '+100%⚔️')

def victory_check(message):
   #проверка на победу в раунде

   if boss.hp > 0 and char.hp > 0:
      start_fight(message)

   elif boss.hp <= 0 and char.hp > 0 and boss.name == MyStrings.Text.makar_name.value:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(MyStrings.Text.restart_button_text.value)
      msg = bot.send_message(message.from_user.id, text = MyStrings.Text.victory_game_text.value, reply_markup=keyboard)
      bot.register_next_step_handler(msg, get_character)

   elif boss.hp <= 0 and char.hp > 0 and boss.name != MyStrings.Text.makar_name.value:
      next_fight(message)

   elif char.hp <= 0: 
      bot.send_message(message.from_user.id, MyStrings.Text.game_over_text.value)

def next_fight(message):
   #конец боя после победы

   char.cooldown = 0
   parameters.win_rate += 1
   char.poison = False
   char.bleeding = False
   char.silence = False
   parameters.poison_dmg = 5
   char.busted_level = 0

   if parameters.win_rate < 8 and boss.name == MyStrings.Text.sanya_name.value:
      char.hp += char.hp * 20 // 100
      char.dmg += char.dmg * 20 // 100
      char.crit_baff(5)
      bot.send_message(message.from_user.id, MyStrings.Text.sanya_sasha_text.value)

   elif parameters.win_rate < 8 and char.name == MyStrings.Text.toshik_name.value:
      char.dmg += char.hp * 5 // 100
      bot.send_message(message.from_user.id, MyStrings.Text.toshik_passive_text.value)

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.victory_button_text.value)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.victory_fight_text.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, shop_choice)

bot.polling(none_stop=True, interval=0)