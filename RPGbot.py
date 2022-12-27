# -*- coding: utf-8 -*-

from telebot import TeleBot
from telebot import types
import random
import Characters
import Drop
import Locations
import MyStrings
import BotMessages
import Fight
bot = TeleBot('')

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
   
   # клавиатура с кнопками выбора героев
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.mitya_name.value, MyStrings.Text.sanya_name.value, MyStrings.Text.toshik_name.value, MyStrings.Text.kolya_name.value, MyStrings.Text.temich_name.value)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.char_choice_text.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, char_creation)

def char_creation(message):
   # назначение характеристик выбранному герою
   Characters.char_get_stats(message.text)

   # сообщение с характеристиками героя
   bot.send_message(message.from_user.id, BotMessages.Message_text.char_description_message())

   # клавиатура с подтверждением выбора героя
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.ready_key_text.value, MyStrings.Text.another_char_key_text.value)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.char_choice_question.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, shop_choice)

def shop_choice(message):
   # перезапуск если герой не подтвержден игроком
   if message.text == MyStrings.Text.another_char_key_text.value:
      bot.send_message(message.from_user.id, MyStrings.Text.give_answer_text.value)
      bot.register_next_step_handler(message, get_character)
   
   # клавиатура с выбором магазина при подтверждении героя или победе в бою
   elif message.text == MyStrings.Text.ready_key_text.value or MyStrings.Text.victory_button_text.value:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(MyStrings.Text.stas_shop_name.value, MyStrings.Text.bratishki_shop_name.value)
      msg = bot.send_message(message.from_user.id, text = MyStrings.Text.shop_choice_text.value, reply_markup=keyboard)
      bot.register_next_step_handler(msg, shop)

def shop(message):
   # применение свойств магазина на игрока
   Drop.shop_enter(message.text)

   # приветственное сообщение магазина и клавиатура с предлагаемыми предметами
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
   # обновление слота предмета игрока если он пошел к Стасу
   Drop.stas_enter(message.text)
   
   # клавитура с запросом босса
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.boss_choice_question.value)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.stas_bye_text.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_choice)

def stats_upgrade(message):
   # обновление статов игрока от выбранного предмета если он пошел к Братишкам
   Drop.bratishki_enter(message.text)

   # сообщение с описанием предмета
   bot.send_message(message.from_user.id, Drop.buff.description)

   # клавитура с выводом характеристик игрока и запросом босса
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.boss_choice_question.value)
   msg = bot.send_message(message.from_user.id, text = BotMessages.Message_text.char_stats_message(), reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_choice)

def boss_choice(message):
   # выбор уровня сложности босса в зависимости от количества побед
   Characters.boss_difficult_choice(Characters.Char.win_rate)

   # назначение характеристик боссу
   Characters.boss_get_stats(Characters.boss_name)

   # проверка в розыске ли игрок, приминение свйоств если да
   if Characters.char.wanted_level == True:
      Characters.boss.resurrection = True
      bot.send_message(message.from_user.id, MyStrings.Text.boss_police_upgrade_text.value)

   # проверка является ли игрок Сашей Шлякиным при битве с Сашей Шлякиным, с перезапуском если да
   if Characters.boss.name == MyStrings.Text.sasha_name.value and Characters.char.name != MyStrings.Text.sanya_name.value:
      bot.send_message(message.from_user.id, MyStrings.Text.sasha_bye_text.value)
      boss_choice(message)

   # клавиатура с выводом характеристик босса и запросом локации
   else:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(MyStrings.Text.location_choice_question.value)
      msg = bot.send_message(message.from_user.id, text = BotMessages.Message_text.boss_stats_message(), reply_markup=keyboard)
      bot.register_next_step_handler(msg, location)

def location(message):
   # случайный выбор локации и применение ее свойств
   Locations.location_choice(Locations.Location.location_name)

   # описание локации и дополнительного взаимодействия с ней персонажей
   bot.send_message(message.from_user.id, BotMessages.Message_text.location_description_message())
   if Locations.Location.pers_iteraction_message != False:
      bot.send_message(message.from_user.id, Locations.Location.pers_iteraction_message)

   # клавиатура с выводом характеристик игрока и запросом боя
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.get_fight_button_text.value)
   msg = bot.send_message(message.from_user.id, text = BotMessages.Message_text.char_stats_message(), reply_markup=keyboard)
   bot.register_next_step_handler(msg, start_fight)

def start_fight(message):
   # применение способности босса перед боем и вывод ее описания
   Characters.boss_prelude_skill_activation(Characters.boss.name)
   if Characters.prelude_skill_message != False:
      bot.send_message(message.from_user.id, Characters.prelude_skill_message)

   # проверка на наличие накопительной способности босса и вывод сообщения с процентом ее заполнения
   if Characters.boss.name == MyStrings.Text.sledovatel_name.value or Characters.boss.name == MyStrings.Text.dron_name.value:
      bot.send_message(message.from_user.id, text = BotMessages.Message_text.boss_skill_meter_message())

   # вывод характеристик игрока и босса
   bot.send_message(message.from_user.id, BotMessages.Message_text.versus_stats(Characters.char.name, Characters.boss.name))

   # клавиатура с выбором действий игрока
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.attack_button_text.value, Characters.char.skill_name, Characters.char.item)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.start_turn_text.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, action_choice)

def action_choice(message):
   #применение выбранного игроком действия

   if message.text == MyStrings.Text.attack_button_text.value:
      Fight.attack()

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