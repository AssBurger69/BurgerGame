# -*- coding: utf-8 -*-

from telebot import TeleBot
from telebot import types
import random
import Characters
import Drop
import Locations
import Parameters
import MyStrings
bot = TeleBot('2102427745:AAECFy-T6GfMWH1VNshsucAEXZEfzmGUZBk')

def chance(x):
   #генератор вероятности
   chance = random.randint(1, 100) in range(1, x)
   return chance

def game_parameters():
   #назначение базовых классов
   global loot
   global bosses
   global parameters

   parameters = Parameters.BaseParameters(10, 0, False)
   loot = Drop.Loot(MyStrings.Text.empty_text.value)
   bosses = Characters.BossList(MyStrings.Text.empty_text.value)

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
   # начальное сообщение и кнопки выбора персонажей
   
   bot.send_message(message.from_user.id, MyStrings.Text.hello_text.value)
   
   game_parameters()

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.mitya_name.value, MyStrings.Text.sanya_name.value, MyStrings.Text.toshik_name.value, MyStrings.Text.kolya_name.value, MyStrings.Text.temich_name.value)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.char_choice_text.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, char_description)

def char_description(message):
   # описание персонажей, назначение их характеристик и кнопка подтверждения

   Characters.Char_get_stats(message.text)

   bot.send_message(message.from_user.id, Characters.Message_text.char_stats_message())

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.ready_key_text.value, MyStrings.Text.another_char_key_text.value)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.char_choice_question.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, shop_choice)

def shop_choice(message):
   # выбор магазина
   if message.text == MyStrings.Text.another_char_key_text.value:
      bot.send_message(message.from_user.id, 'Напиши мне что-нибудь, потом это подправлю')
      bot.register_next_step_handler(message, get_character)
   elif message.text == MyStrings.Text.ready_key_text.value or MyStrings.Text.victory_button_text.value:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(MyStrings.Text.stas_shop_name.value, MyStrings.Text.bratishkino_shop_name.value)
      msg = bot.send_message(message.from_user.id, text = MyStrings.Text.shop_choice_text.value, reply_markup=keyboard)
      bot.register_next_step_handler(msg, shop)

def shop(message):
   #создание списка из трех рандомных итемов/баффов, которые потом будут кнопками
   buff_choice = [random.choice(loot.buff_list), random.choice(loot.buff_list), random.choice(loot.buff_list)]
   item_choice = [random.choice(loot.item_list), random.choice(loot.item_list), random.choice(loot.item_list)]
   
   #развилка магазинов с применением их свойств на персонажа и кнопками выбора
   if message.text == MyStrings.Text.stas_shop_name.value:
      char.dmg_baff(50)
      bot.send_message(message.from_user.id, MyStrings.Text.stas_shop_description.value)
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(item_choice[0], item_choice[1], item_choice[2])
      msg = bot.send_message(message.from_user.id, text = MyStrings.Text.item_choice_text.value, reply_markup=keyboard)
      bot.register_next_step_handler(msg, items_upgrade)

   elif message.text == MyStrings.Text.bratishkino_shop_name.value:
      char.hp_baff(200)
      bot.send_message(message.from_user.id, MyStrings.Text.bratishkino_shop_description.value)
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(buff_choice[0], buff_choice[1], buff_choice[2])
      msg = bot.send_message(message.from_user.id, text = MyStrings.Text.item_choice_text.value, reply_markup=keyboard)
      bot.register_next_step_handler(msg, stats_upgrade)

def items_upgrade(message):
   #обновление предмета персонажа если он пошел к Стасу
   char.item = message.text
   loot.item_list.remove(message.text)
   
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.boss_choice_question.value)
   msg = bot.send_message(message.from_user.id, text = MyStrings.Text.stas_bye_text.value, reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_choice)

def stats_upgrade(message):
   #обновление статов персонажа от выбранного предмета если он пошел к Братишкам
   x = message.text
   loot.buff_list.remove(x)
   
   if x == MyStrings.Text.sochnik_name.value:
      buff = Drop.Buff(25, MyStrings.Text.sochnik_description.value)
      char.hp += char.hp * buff.value_1 // 100
   
   elif x == MyStrings.Text.dubai_name.value:
      buff = Drop.Buff(30, MyStrings.Text.dubai_description.value)
      char.hp += char.hp * buff.value_1 // 100

   elif x == MyStrings.Text.dron_meat_name.value:
      buff = Drop.Buff(40, MyStrings.Text.dron_meat_description.value)
      char.hp += char.hp * buff.value_1 // 100

   elif x == MyStrings.Text.pizza5_name.value:
      buff = Drop.Buff(50, MyStrings.Text.pizza5_description.value)
      char.hp += char.hp * buff.value_1 // 100

   elif x == MyStrings.Text.guitar_name.value:
      buff = Drop.Buff(15, MyStrings.Text.guitar__description.value)
      char.dmg += char.dmg * buff.value_1 // 100

   elif x == MyStrings.Text.bashkerme_name.value:
      buff = Drop.Buff(25, MyStrings.Text.bashkerme_description.value)
      char.dmg += char.dmg * buff.value_1 // 100

   elif x == MyStrings.Text.pika_name.value:
      buff = Drop.Buff(30, MyStrings.Text.pika_description.value)
      char.dmg += char.dmg * buff.value_1 // 100

   elif x == MyStrings.Text.dildo_name.value:
      buff = Drop.Buff(50, MyStrings.Text.dildo_description.value)
      char.dmg += char.dmg * buff.value_1 // 100
   
   elif x == MyStrings.Text.everlast_name.value:
      buff = Drop.SuperBuff(10, 10, MyStrings.Text.everlast_description.value)
      char.hp += char.hp * buff.value_1 // 100
      char.dmg += char.dmg * buff.value_2 // 100

   elif x == MyStrings.Text.marki_name.value:
      buff = Drop.SuperBuff(20, 20, MyStrings.Text.marki_description.value)
      char.hp += char.hp * buff.value_1 // 100
      char.dmg += char.dmg * buff.value_2 // 100

   elif x == MyStrings.Text.limon_name.value:
      buff = Drop.UltraBuff(30, 50, 5, MyStrings.Text.limon_description.value)
      char.hp -= char.hp * buff.value_1 // 100
      char.dmg += char.dmg * buff.value_2 // 100
      char.crit += buff.value_3

   elif x == MyStrings.Text.chess_name.value:
      buff = Drop.Buff(5, MyStrings.Text.chess_description.value)
      char.crit += buff.value_1
   
   elif x == MyStrings.Text.vargan_name.value:
      buff = Drop.Buff(10, MyStrings.Text.vargan_description.value)
      char.crit += buff.value_1

   elif x == MyStrings.Text.choops_name.value:
      buff = Drop.Buff(10, MyStrings.Text.choops_description.value)
      char.vamp += buff.value_1

   elif x == MyStrings.Text.shiva_bless_name.value:
      buff = Drop.SuperBuff(50, 15, MyStrings.Text.shiva_bless_description.value)
      char.dmg += char.dmg * buff.value_1 // 100
      char.crit += buff.value_2

   elif x == MyStrings.Text.makar_bless_name.value:
      buff = Drop.UltraBuff(30, 30, 10, MyStrings.Text.makar_bless_description.value)
      char.hp += char.hp * buff.value_1 // 100
      char.dmg += char.dmg * buff.value_2 // 100
      char.crit += buff.value_3

   if x not in char.all_items:
      char.all_items.append(x)
   
   bot.send_message(message.from_user.id, buff.dscr)

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.boss_choice_question.value)
   msg = bot.send_message(message.from_user.id, text = char.icon + char.name + ':\n❤️ ' + str(char.hp) + '\n⚔️ ' + str(char.dmg) + '\n💥 ' + str(char.crit), reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_choice)

def boss_stats(x):
   #назначение босса и его уникальных свойств
   global boss

   if x == MyStrings.Text.palich_name.value:
      boss = Characters.Boss(x, 800, 200, 0, 0, 0, MyStrings.Text.palich_description.value)
      
   elif x == MyStrings.Text.chaikovskii_name.value:
      boss = Characters.Boss(x, 600, 250, 0, 0, 0, MyStrings.Text.chaikovskii_description.value)
      boss.resurrection = True

   elif x == MyStrings.Text.viv_name.value:
      boss = Characters.Boss(x, 900, 100, 0, 0, 0, MyStrings.Text.viv_description.value)

   elif x == MyStrings.Text.sasha_name.value:
      boss = Characters.Boss(x, 1000, 200, 20, 0, 0, MyStrings.Text.sasha_description.value)

   elif x == MyStrings.Text.tvar_name.value:
      boss = Characters.Boss(x, 800, 50, 0, 0, 0, MyStrings.Text.tvar_description.value)
      boss.returnal_value = 50

   elif x == MyStrings.Text.randomich_name.value:
      boss = Characters.Boss(x, random.randint(100, 1001), random.randint(10, 301), random.randint(0, 51), random.randint(0, 51), 0, MyStrings.Text.randomich_description.value)
      boss.returnal_value = random.randint(0, 51)
      boss.regen = random.randint(0, 301)

   elif x == MyStrings.Text.kitty_name.value:
      boss = Characters.Boss(x, 1000, 200, 0, 0, 0, MyStrings.Text.kitty_description.value)
      boss.endskill_value = 50

   elif x == MyStrings.Text.inkvisizia_name.value:
      boss = Characters.Boss(x, 500, 500, 50, 0, 0, MyStrings.Text.inkvisizia_description.value)

   elif x == MyStrings.Text.doc_leha_name.value:
      boss = Characters.Boss(x, 1500, 300, 0, 0, 0, MyStrings.Text.doc_leha_description.value)
      boss.endskill_value = 36

   elif x == MyStrings.Text.drunk_leha_name.value:
      boss = Characters.Boss(x, 1200, 100, 0, 0, 0, MyStrings.Text.doc_leha_description.value)

   elif x == MyStrings.Text.mel_name.value:
      boss = Characters.Boss(x, 50, 0, 0, 90, 0, MyStrings.Text.mel_description.value)

   elif x == MyStrings.Text.redhead_name.value:
      boss = Characters.Boss(x, 2000, 100, 0, 0, 0, MyStrings.Text.redhead_description.value)
      boss.regen = 300

   elif x == MyStrings.Text.sledovatel_name.value:
      boss = Characters.Boss(x, 1500, 100, 0, 50, 0, MyStrings.Text.redhead_description.value)
      boss.busted_level = 10

   elif x == MyStrings.Text.doner_name.value:
      boss = Characters.Boss(x, 1800, 350, 0, 0, 0, MyStrings.Text.doner_description.value)

   elif x == MyStrings.Text.black_stas_name.value:
      boss = Characters.Boss(x, 1500, 300, 0, 0, 0, MyStrings.Text.black_stas_description.value)

   elif x == MyStrings.Text.dron_name.value:
      boss = Characters.Boss(x, 2000, 100, 0, 0, 0, MyStrings.Text.dron_description.value)
      boss.obida_level = 5

   elif x == MyStrings.Text.glad_name.value:
      boss = Characters.Boss(x, 3000, 200, 0, 0, 0, MyStrings.Text.glad_description.value)

   elif x == MyStrings.Text.shiva_name.value:
      boss = Characters.Boss(x, 2000, 500, 0, 30, 0, MyStrings.Text.shiva_description.value)

   elif x == MyStrings.Text.makar_name.value:
      boss = Characters.Boss(x, char.hp, char.dmg, char.crit, char.miss, char.vamp, MyStrings.Text.makar_description.value)

   elif x == MyStrings.Text.gomozeki_name.value:
      boss = Characters.Boss(x, 2000, 300, 20, 0, 0, MyStrings.Text.gomozeki_description.value)
      boss.regen = 200

def boss_choice(message):
   #выбор уровня сложности босса в зависимости от побед

   if parameters.win_rate < 3:
      boss_list = bosses.list_easy
   elif parameters.win_rate < 6 and parameters.win_rate >= 3:
      boss_list = bosses.list_medium
   elif parameters.win_rate < 9 and parameters.win_rate >= 6:
      boss_list = bosses.list_hard
   elif parameters.win_rate == 9:
      boss_list = [MyStrings.Text.makar_name.value]

   #выбор босса, удаление его из пула боссов и применение его статов
   boss_name = random.choice(boss_list)
   boss_list.remove(boss_name)
   boss_stats(boss_name)

   #проверка в розыске ли персонаж
   if parameters.wanted_level == True:
      boss.resurrection = True
      bot.send_message(message.from_user.id, MyStrings.Text.boss_police_upgrade_text.value)

   #проверка на является ли персонаж Сашей Шлякиным при битве с Сашей Шлякиным
   if boss.name == MyStrings.Text.sasha_name.value and char.name != MyStrings.Text.sanya_name.value:
      bot.send_message(message.from_user.id, boss.name + '\n🖤 ' + str(boss.hp) + '\n⚔️ ' + str(boss.dmg) + '\n💥 ' + str(boss.crit))
      bot.send_message(message.from_user.id, MyStrings.Text.sasha_bye_text.value)
      boss_choice(message)
   else:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(MyStrings.Text.location_choice_question.value)
      msg = bot.send_message(message.from_user.id, text = boss.name + '\n🖤 ' + str(boss.hp) + '\n⚔️ ' + str(boss.dmg) + '\n💥 ' + str(boss.crit) + '\n' + boss.dscr, reply_markup=keyboard)
      bot.register_next_step_handler(msg, location)

def location_choice(x):
   #описание локаций и их свойств на персонажа
   global loc

   if x == MyStrings.Text.kolbas_name.value:
      loc = Locations.Location(10, MyStrings.Text.kolbas_description.value, MyStrings.Text.kolbas_icon.value)
      char.hp -= char.hp * loc.value_1 // 100
      if boss.name == MyStrings.Text.doner_name.value:
         boss.hp += 500
         loc.loc_effect_msg = MyStrings.Text.doner_kolbas_text.value
   
   elif x == MyStrings.Text.polazna_name.value:
      loc = Locations.SuperLocation(20, 10, MyStrings.Text.polazna_description.value, MyStrings.Text.polazna_icon.value)
      char.hp += char.hp * loc.value_1 // 100
      char.dmg -= char.dmg * loc.value_2 // 100

   elif x == MyStrings.Text.god_city_name.value:
      loc = Locations.UltraLocation(10, 10, 10, MyStrings.Text.god_city_description.value, MyStrings.Text.god_city_icon.value)
      char.hp += char.hp * loc.value_1 // 100
      char.dmg += char.dmg * loc.value_2 // 100
      char.crit += loc.value_3
      if boss.name == MyStrings.Text.chaikovskii_name.value:
         boss.hp += 100
         boss.dmg += 50
         boss.crit += 10
         loc.loc_effect_msg = MyStrings.Text.chaikovskii_god_city_text.value

   elif x == MyStrings.Text.bad_trip_name.value:
      loc = Locations.SuperLocation(20, 20, MyStrings.Text.bad_trip_description.value, MyStrings.Text.bad_trip_icon.value)
      if char.name == MyStrings.Text.kolya_name.value:
         char.hp_baff(300)
         char.dmg_baff(100)
         loc.loc_effect_msg = MyStrings.Text.kolya_bad_trip_text.value
      elif char.name == MyStrings.Text.temich_name.value:
         loc.loc_effect_msg = MyStrings.Text.temich_bad_trip_text.value
      elif char.name != MyStrings.Text.kolya_name.value and char.name != MyStrings.Text.temich_name.value:
         char.hp -= char.hp * loc.value_1 // 100
         char.dmg -= char.dmg * loc.value_2 // 100
         loc.loc_effect_msg = MyStrings.Text.bad_trip_effect_text.value
      
   elif x == MyStrings.Text.molebka_name.value:
      loc = Locations.SuperLocation(20, 10, MyStrings.Text.molebka_description.value, MyStrings.Text.molebka_icon.value)
      if char.name == MyStrings.Text.toshik_name.value:
         char.hp += char.hp * loc.value_1 // 100
         char.dmg += char.dmg * loc.value_2 // 100
         loc.loc_effect_msg = MyStrings.Text.toshik_molebka_text.value
      elif char.name != MyStrings.Text.toshik_name.value:
         char.hp -= char.hp * loc.value_1 // 100
         char.dmg += char.dmg * loc.value_2 // 100
         loc.loc_effect_msg = MyStrings.Text.molebka_effect_text.value
      
   elif x == MyStrings.Text.army_name.value:
      loc = Locations.SuperLocation(50, 30, MyStrings.Text.army_description.value, MyStrings.Text.army_icon.value)
      char.hp -= char.hp * loc.value_1 // 100
      char.dmg += char.dmg * loc.value_2 // 100

   elif x == MyStrings.Text.drochilnya_name.value:
      loc = Locations.SuperLocation(10, 10, MyStrings.Text.drochilnya_description.value, MyStrings.Text.drochilnya_icon.value)
      char.dmg += char.dmg * loc.value_1 // 100
      char.crit_baff(loc.value_2)
      if char.name == MyStrings.Text.sanya_name.value:
         char.crit_baff(loc.value_2)
         loc.loc_effect_msg = MyStrings.Text.sanya_drochilnya_text.value

   elif x == MyStrings.Text.stage25_name.value:
      loc = Locations.SuperLocation(50, 10, MyStrings.Text.stage25_description.value, MyStrings.Text.stage25_icon.value)
      char.dmg -= char.dmg * loc.value_1 // 100
      char.crit_debaff(loc.value_2)
      if char.name == MyStrings.Text.kolya_name.value:
         char.hp -= char.hp * 20 // 100
         loc.loc_effect_msg = MyStrings.Text.kolya_stage25_text.value
      elif char.name == MyStrings.Text.mitya_name.value:
         char.hp += char.hp * 20 // 100
         loc.loc_effect_msg = MyStrings.Text.mitya_stage25_text.value

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
   #выбор рандомной локации, применение ее свойств и вывод ее описания

   location_list = [MyStrings.Text.kolbas_name.value, MyStrings.Text.polazna_name.value, MyStrings.Text.god_city_name.value, MyStrings.Text.bad_trip_name.value, MyStrings.Text.molebka_name.value, MyStrings.Text.army_name.value, MyStrings.Text.drochilnya_name.value, MyStrings.Text.stage25_name.value]
   location_name = random.choice(location_list)

   location_choice(location_name)

   bot.send_message(message.from_user.id, loc.icon + location_name + loc.icon + '\n' + loc.dscr)
   if loc.loc_effect_msg != False:
      bot.send_message(message.from_user.id, loc.loc_effect_msg)

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.get_fight_button_text.value)
   msg = bot.send_message(message.from_user.id, text = 'Твои статы:\n❤️ ' + str(char.hp) + '\n⚔️ ' + str(char.dmg) + '\n💥 ' + str(char.crit), reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_prelude)

def boss_prelude(message):
   #описание первого скилла босса перед началом боя
   
   if boss.name == MyStrings.Text.palich_name.value:
      char.silence = True
      bot.send_message(message.from_user.id, MyStrings.Text.palich_prelude_text.value)
      start_fight(message)

   elif boss.name == MyStrings.Text.viv_name.viv_name and char.item == 'Травмат Володи':
      char.hp_debaff(300)
      char.bleeding = True
      char.item = MyStrings.Text.empty_text.value
      bot.send_message(message.from_user.id, 'Володя забрал свой травмат!\n' + char.icon + '-300❤️🩸')
      start_fight(message)

   elif boss.name == MyStrings.Text.redhead_name.value:
      char.poison = True
      bot.send_message(message.from_user.id, char.icon + ' + 🦠')
      start_fight(message)

   elif boss.name == MyStrings.Text.sledovatel_name.value:
      drugs = 'Шига', 'Мадам', MyStrings.Text.marki_name.value
      cross_check = [x for x in drugs if x in char.all_items]
      if char.dmg > 500:
         char.dmg //= 2
         bot.send_message(message.from_user.id, '👮‍♂️: Чет многовато у вас дамага, молодой человек\n' + char.icon + '-50%⚔️')
      if char.elex_count > 0 or len(cross_check) > 0:
         char.busted_level += 50
         bot.send_message(message.from_user.id, MyStrings.Text.sledovatel_drugcheck_text.value)
      start_fight(message)

   elif boss.name == MyStrings.Text.dron_name.value:
      obida_level = 0
      obida_level += len(char.all_items) * 5
      bot.send_message(message.from_user.id, MyStrings.Text.dron_bratishki_text.value)
      if MyStrings.Text.dron_meat_name.value in char.all_items:
         obida_level += 10
         bot.send_message(message.from_user.id, MyStrings.Text.dron_dron_meat_text.value)
      start_fight(message)

   elif boss.name == MyStrings.Text.doner_name.value:
      if MyStrings.Text.everlast_name.value in char.all_items:
         boss.hp += boss.hp * 10 // 100
         boss.dmg += boss.dmg * 10 // 100
         bot.send_message(message.from_user.id, MyStrings.Text.doner_everlast_text.value)
      elif '2.5-литровка Колы' == char.item:
         char.hp_debaff(500)
         boss.hp_debaff(500)
         bot.send_message(message.from_user.id, MyStrings.Text.doner_cola_text)
      start_fight(message)

   elif boss.name == MyStrings.Text.black_stas_name.value and char.name == MyStrings.Text.mitya_name.value:
      boss.dmg += char.elex_count * 200
      bot.send_message(message.from_user.id, MyStrings.Text.black_stas_mitya_text.value)
      start_fight(message)

   else: start_fight(message)

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
   global item_dscr

   if x == MyStrings.Text.zhiguli_name.vaccine_name:
      if boss.name == MyStrings.Text.doner_name.value:
         boss.hp_baff(150)
         item_dscr = 'Пизда твоему бухлу, Донер его выпил\n' + boss.icon + '+150🖤'
      else:
         char.hp_baff(150)
         item_dscr = MyStrings.Text.zhiguli_description.value

   elif x == MyStrings.Text.sidr_name.value:
      if boss.name == MyStrings.Text.doner_name.value:
         boss.hp_baff(300)
         item_dscr = 'Пизда твоему бухлу, Донер его выпил\n' + boss.icon + '+300🖤'
      else:
         char.hp_baff(300)
         item_dscr = MyStrings.Text.sidr_description.value

   elif x == MyStrings.Text.bagbeer_name.value:
      if boss.name == MyStrings.Text.doner_name.value:
         boss.hp_baff(500)
         item_dscr = 'Пизда твоему бухлу, Донер его выпил\n' + boss.icon + '+500🖤'
      else:
         char.hp_baff(500)
         item_dscr = MyStrings.Text.bagbeer_description.value

   elif x == MyStrings.Text.mineralka_name.value:
      char.regen = 100
      item_dscr = MyStrings.Text.mineralka_description.value + char.icon + ' + 💕'

   elif x == MyStrings.Text.lezvie_name.value:
      boss.hp_debaff(150)
      boss.bleeding = True
      item_dscr = MyStrings.Text.lezvie_description.value + boss.icon + '-150🖤🩸'

   elif x == MyStrings.Text.travmat_name.value:
      boss.hp_debaff(300)
      boss.bleeding = True
      item_dscr = MyStrings.Text.travmat_description.value + boss.icon + '-300🖤🩸'

   elif x == MyStrings.Text.cola_name.value:
      boss.hp_debaff(500)
      item_dscr = MyStrings.Text.cola_description.value + boss.icon + '-500🖤'

   elif x == MyStrings.Text.sick_sock_name.value:
      if boss.name == MyStrings.Text.doner_name.value:
         boss.hp_baff(50)
         boss.regen = 100
         item_dscr = 'Не стоило травить Донера\n' + boss.icon + '+50🖤💕'
      else:
         boss.hp_debaff(50)
         boss.poison = True
         item_dscr = boss.name + MyStrings.Text.sick_sock_description.value + boss.icon + '-50🖤🦠'

   elif x == MyStrings.Text.harchok_name.value:
      if boss.name == MyStrings.Text.doner_name.value:
         boss.hp_baff(200)
         boss.regen = 100
         item_dscr = 'Не стоило травить Донера\n' + boss.icon + '+200🖤💕'
      else:
         boss.hp_debaff(200)
         boss.poison = True
         item_dscr = MyStrings.Text.harchok_description.value + boss.icon + '-200🖤🦠'

   elif x == MyStrings.Text.rampag_name.value:
      if boss.name == MyStrings.Text.doner_name.value:
         boss.hp = 0
         item_dscr = MyStrings.Text.doner_rampag_text.value
      else:
         boss.stan_timer = 1
         item_dscr = MyStrings.Text.rampag_description.value

   elif x == MyStrings.Text.rolex_name.value:
      char.cooldown = 0
      item_dscr = MyStrings.Text.rolex_description.value

   elif x == MyStrings.Text.vaccine_name.value:
      char.poison = False
      char.bleeding = False
      item_dscr = MyStrings.Text.vaccine_description.value

   elif x == MyStrings.Text.shiga_name.value:
      foods = MyStrings.Text.sochnik_name.value, MyStrings.Text.dubai_name.value, MyStrings.Text.dron_meat_name.value, MyStrings.Text.pizza5_name.value
      cross_check = [x for x in foods if x in char.all_items]
      if len(cross_check) == 0:
         char.hp_debaff(200)
         char.dmg_baff(100)
         item_dscr = MyStrings.Text.shiga_debuff_description.value
      elif len(cross_check) > 0:
         char.hp_baff(200)
         char.dmg_baff(100)
         item_dscr = MyStrings.Text.shiga_buff_description.value

   elif x == MyStrings.Text.madam_name.value:
      boss.dmg -= boss.dmg * 50 // 100
      item_dscr = MyStrings.Text.madam_description.value + boss.icon + '-50%⚔️'

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