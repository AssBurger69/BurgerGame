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