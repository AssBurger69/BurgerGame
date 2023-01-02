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
bot = TeleBot('2102427745:AAECFy-T6GfMWH1VNshsucAEXZEfzmGUZBk')

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
   Locations.location_choice(random.choice(Locations.Location.location_list))

   # описание локации и дополнительного взаимодействия с ней персонажей
   bot.send_message(message.from_user.id, BotMessages.Message_text.location_description_message())
   if Locations.Location.pers_iteraction_message != False:
      bot.send_message(message.from_user.id, Locations.Location.pers_iteraction_message)
      Locations.Location.pers_iteraction_message = False

   # клавиатура с выводом характеристик игрока и запросом боя
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.get_fight_button_text.value)
   msg = bot.send_message(message.from_user.id, text = BotMessages.Message_text.char_stats_message(), reply_markup=keyboard)
   bot.register_next_step_handler(msg, start_fight)

def start_fight(message):
   # применение способности босса перед боем, отсылка сообщения с ее описанием
   Characters.boss_prelude_skill_activation(Characters.boss.name)
   if Characters.prelude_skill_message != False:
      bot.send_message(message.from_user.id, Characters.prelude_skill_message)
      Characters.prelude_skill_message = False

   # проверка на наличие накопительной способности босса и вывод сообщения с процентом ее заполнения
   if Characters.boss.name == MyStrings.Text.sledovatel_name.value or Characters.boss.name == MyStrings.Text.dron_name.value:
      bot.send_message(message.from_user.id, BotMessages.Message_text.boss_skill_meter_message(Characters.boss.name))

   # вывод характеристик игрока и босса
   bot.send_message(message.from_user.id, BotMessages.Message_text.versus_stats(Characters.char.name, Characters.boss.name))

   # клавиатура с выбором действий игрока
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.attack_button_text.value, Characters.char.skill_name, Characters.char.item)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.start_turn_text.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, action_choice)

def action_choice(message):
   # применение выбранного игроком действия

   if message.text == MyStrings.Text.attack_button_text.value:
      # запуск цикла атаки, если игрок нажал "Атака"
      Fight.attack()

      # проверка количества возникших сообщений в цикле атаки, их вывод
      while len(Fight.Attack_messages.attack_messages_list) > 0:
         bot.send_message(message.from_user.id, Fight.Attack_messages.attack_messages_list[0])
         del Fight.Attack_messages.attack_messages_list[0]

      # клавиатура с подтверждением конца хода, переход на проверку победы в бою
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(MyStrings.Text.end_turn_button_text.value)
      msg = bot.send_message(message.from_user.id, BotMessages.Message_text.versus_stats(Characters.char.name, Characters.boss.name), reply_markup=keyboard)
      bot.register_next_step_handler(msg, victory_check)

   elif message.text == Characters.char.skill_name:
      # применение способности, если игрок нажал "Скилл"
      Fight.char_skill_use()

      # отсылка сообщения
      bot.send_message(message.from_user.id, Fight.Attack_messages.skill_use_message)

      # переход на проверку победы в бою
      victory_check(message)

   elif message.text == Characters.char.item:
      # применение предмета, если игрок нажал "Предмет"
      Fight.char_item_use()

      # отсылка сообщения 
      bot.send_message(message.from_user.id, Fight.Attack_messages.item_use_message)

      # особое сообщение, если предмет влияет на конкретного игрока
      if Drop.Item.char_iteraction_message != False:
         bot.send_message(message.from_user.id, Drop.Item.char_iteraction_message)
         Drop.Item.char_iteraction_message = False

      # особое сообщение, если предмет влияент на конкретного босса
      if Drop.Item.boss_iteraction_message != False:
         bot.send_message(message.from_user.id, Drop.Item.boss_iteraction_message)
         Drop.Item.boss_iteraction_message = False 

      # переход на проверку победы в бою
      victory_check(message)

def victory_check(message):
   # проверка на победу в конце раунда

   if Characters.boss.health > 0 and Characters.char.health > 0:
      # если и босс и игрок живы - переход к следующему раунду
      start_fight(message)

   elif Characters.boss.health <= 0 and Characters.char.health > 0 and Characters.boss.name == MyStrings.Text.makar_name.value:
      # если игрок победил финального босса Короля Макара - поздравительное сообщение, клавиатура с подтверждением перезапуска игры
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(MyStrings.Text.restart_button_text.value)
      msg = bot.send_message(message.from_user.id, text = MyStrings.Text.victory_game_text.value, reply_markup=keyboard)
      bot.register_next_step_handler(msg, get_character)

   elif Characters.boss.health <= 0 and Characters.char.health > 0 and Characters.boss.name != MyStrings.Text.makar_name.value:
      # если игрок победил обычного босса - переход на следующий уровень
      next_fight(message)

   elif Characters.char.health <= 0: 
      # если игрок проиграл, вывод сообщения
      bot.send_message(message.from_user.id, MyStrings.Text.game_over_text.value)

def next_fight(message):
   # обнуление статусов игрока, повышение счетчика побед
   Fight.fight_victory()

   # особое сообщение если игрок Саня победил босса Саню
   if Fight.Attack_messages.sanya_win_sanya_message != False:
      bot.send_message(message.from_user.id, Fight.Attack_messages.sanya_win_sanya_message)

   # особое сообщение для пассивной способности игрока Тошик
   elif Fight.Attack_messages.toshik_passive_skill_message != False:
      bot.send_message(message.from_user.id, Fight.Attack_messages.toshik_passive_skill_message)

   # клавиатура с подтверждением перехода на следующий уровень
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.victory_button_text.value)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.victory_fight_text.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, shop_choice)

bot.polling(none_stop=True, interval=0)