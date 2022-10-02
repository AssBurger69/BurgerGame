# -*- coding: utf-8 -*-

from telebot import TeleBot
from telebot import types
import random
import Characters
import Drop
import Locations
import Parameters
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
   loot = Drop.Loot('Пусто')
   bosses = Characters.BossList('makap')

def stas_passive(x):
   #чек на возвращение урона Черного Стаса
   return_check = boss.name == 'Черный Стас' and chance(x) == True
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
   
   bot.send_message(message.from_user.id, 'Приветствую в моем Бургерном рогалике, друг! Играй лучше на телефоне. Наслаждайся...')
   
   game_parameters()

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add('Митя', 'Саня', 'Тошик', 'Коля', 'Темыч')
   msg = bot.send_message(message.from_user.id, text = 'Выбери персонажа', reply_markup=keyboard)
   bot.register_next_step_handler(msg, char_description)

def char_description(message):
   # описание персонажей, назначение их характеристик и кнопка подтверждения
   global char
   
   if message.text == 'Митя':
      char = Characters.Char('Митя', 800, 100, 0, 0, 20, 'Бахнуть элексир', '👨‍🔬')
      char_dscr = '❤️800\n⚔️100\n💥0\nМастер отсоса жизни\nЛюбитель губительно-усиливающих эликсиров, будь с ними осторожен'
      
   elif message.text == 'Саня':
      char = Characters.Char('Саня', 1000, 200, 30, 0, 0, 'Кинуть ножницы', '💇')
      char_dscr = '❤️1000\n⚔️200\n💥30\nЭзотерический парикмахер\nМастер чистого белого неделимого броска ножницами'
      
   elif message.text == 'Тошик':
      char = Characters.Char('Тошик', 1500, 100, 0, 0, 0, 'Сесть медитировать', '🦹‍♂️')
      char_dscr = '❤️1500\n⚔️100\n💥0\nПсайтанковый медитатор\nБольше здоровья - больше силы'
      
   elif message.text == 'Коля':
      char = Characters.Char('Коля', 1200, 100, 0, 0, 0, 'Хакнуть урон', '👨‍💻')
      char_dscr = '❤️1200\n⚔️100\n💥0\nХипстерский программист\nПадок на разочарование'
      
   elif message.text == 'Темыч':
      char = Characters.Char('Темыч', 800, 150, 0, 15, 0, 'Навести суету', '🤷‍♂️')
      char_dscr = '❤️800\n⚔️150\n💥0\nНетикающий суетолог\nЕсли не поймет что понес урон - значит этого не было'

   bot.send_message(message.from_user.id, char.name + char.icon + '\n' + char_dscr)
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add('Я готов!', 'Давай другого')
   msg = bot.send_message(message.from_user.id, text = 'Берешь его?', reply_markup=keyboard)
   bot.register_next_step_handler(msg, shop_choice)

def shop_choice(message):
   # выбор магазина
   if message.text == 'Давай другого':
      bot.send_message(message.from_user.id, 'Напиши мне что-нибудь, потом это подправлю')
      bot.register_next_step_handler(message, get_character)
   elif message.text == 'Я готов!' or 'Я молодец':
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add('Лавка Серого Стаса', 'Братишкино логово')
      msg = bot.send_message(message.from_user.id, text = 'Выбирай куда пойдешь', reply_markup=keyboard)
      bot.register_next_step_handler(msg, shop)

def shop(message):
   #создание списка из трех рандомных итемов/баффов, которые потом будут кнопками
   buff_choice = [random.choice(loot.buff_list), random.choice(loot.buff_list), random.choice(loot.buff_list)]
   item_choice = [random.choice(loot.item_list), random.choice(loot.item_list), random.choice(loot.item_list)]
   
   #развилка магазинов с применением их свойств на персонажа и кнопками выбора
   if message.text == 'Лавка Серого Стаса':
      char.dmg_baff(50)
      bot.send_message(message.from_user.id, 'Стас тебя угостил чем-то мощным, чувствуешь себя сильнее! Давай глянем что он там еще наворовал\n+50⚔️')
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(item_choice[0], item_choice[1], item_choice[2])
      msg = bot.send_message(message.from_user.id, text = 'Бери что-то одно', reply_markup=keyboard)
      bot.register_next_step_handler(msg, items_upgrade)

   elif message.text == 'Братишкино логово':
      char.hp_baff(200)
      bot.send_message(message.from_user.id, 'Братишки приветсвуют тебя в своем логове! Сядь браток, попей улун молочный, он тебя подлечит\n+200❤️')
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(buff_choice[0], buff_choice[1], buff_choice[2])
      msg = bot.send_message(message.from_user.id, text = 'Бери что-то одно', reply_markup=keyboard)
      bot.register_next_step_handler(msg, stats_upgrade)

def items_upgrade(message):
   #обновление предмета персонажа если он пошел к Стасу
   char.item = message.text
   loot.item_list.remove(message.text)
   
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add('А с кем деремся?')
   msg = bot.send_message(message.from_user.id, text = 'Хороший выбор, батя', reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_choice)

def stats_upgrade(message):
   #обновление статов персонажа от выбранного предмета если он пошел к Братишкам
   x = message.text
   loot.buff_list.remove(x)
   
   if x == 'Сочник со сгухой':
      buff = Drop.Buff(25, 'Сгущено-вареное блаженство\n+25%❤️')
      char.hp += char.hp * buff.value_1 // 100
   
   elif x == 'Дубайский шаурмец':
      buff = Drop.Buff(30, 'Неизменная классика\n+30%❤️')
      char.hp += char.hp * buff.value_1 // 100

   elif x == 'Мясо Андрея':
      buff = Drop.Buff(40, 'Держи его по-дальше от Дрона\n+40%❤️')
      char.hp += char.hp * buff.value_1 // 100

   elif x == '5 пицц':
      buff = Drop.Buff(50, 'Промкод на 5 пицц со скидкой 50%\n+50%❤️')
      char.hp += char.hp * buff.value_1 // 100

   elif x == 'Гитара':
      buff = Drop.Buff(15, 'Теперь ты - Рокер\n+15%⚔️')
      char.dmg += char.dmg * buff.value_1 // 100

   elif x == 'Башкерме взрывай':
      buff = Drop.Buff(25, 'Баааашкермееее!\n+25%⚔️')
      char.dmg += char.dmg * buff.value_1 // 100

   elif x == 'Пика точеная':
      buff = Drop.Buff(30, 'Ну хоть не хуй дроченый\n+30%⚔️')
      char.dmg += char.dmg * buff.value_1 // 100

   elif x == 'Огромный дилдак':
      buff = Drop.Buff(50, 'В умелых руках дает\n+50%⚔️')
      char.dmg += char.dmg * buff.value_1 // 100
   
   elif x == 'Костюм Эверласт':
      buff = Drop.SuperBuff(10, 10, 'Костюм Дани Эверласта, легенды миксфайта!\n+10%❤️\n+10%⚔️')
      char.hp += char.hp * buff.value_1 // 100
      char.dmg += char.dmg * buff.value_2 // 100

   elif x == 'Почтовые марки':
      buff = Drop.SuperBuff(20, 20, 'Ты смог уломать ребят на почтовые отправления!\n+20%❤️\n+20%⚔️')
      char.hp += char.hp * buff.value_1 // 100
      char.dmg += char.dmg * buff.value_2 // 100

   elif x == 'Лимонная голодовочка':
      buff = Drop.UltraBuff(30, 50, 5, '24-часовая голодовка с братишками!\n-30%❤️\n+50%⚔️\n+5%💥')
      char.hp -= char.hp * buff.value_1 // 100
      char.dmg += char.dmg * buff.value_2 // 100
      char.crit += buff.value_3

   elif x == 'Сыграть в шахматы':
      buff = Drop.Buff(5, 'Не важно проиграл ты или да\n+5%💥')
      char.crit += buff.value_1
   
   elif x == 'Поиграть на варгане':
      buff = Drop.Buff(10, 'Хорошая работа ртом и языком, дружище\n+10%💥')
      char.crit += buff.value_1

   elif x == 'Черный чупа чупс':
      buff = Drop.Buff(10, 'Навык отсоса повышен!\n+10%🦇')
      char.vamp += buff.value_1

   elif x == 'Благословение Шивы':
      buff = Drop.SuperBuff(50, 15, 'Великая Шива благоволит тебе воин!\n+50%⚔️\n+15%💥')
      char.dmg += char.dmg * buff.value_1 // 100
      char.crit += buff.value_2

   elif x == 'Благословение Макара':
      buff = Drop.UltraBuff(30, 30, 10, 'Святейший Король Макар снизошел на тебя!\n+30%❤️\n+30%⚔️\n+5%💥')
      char.hp += char.hp * buff.value_1 // 100
      char.dmg += char.dmg * buff.value_2 // 100
      char.crit += buff.value_3

   if x not in char.all_items:
      char.all_items.append(x)
   
   bot.send_message(message.from_user.id, buff.dscr)

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add('А с кем деремся?')
   msg = bot.send_message(message.from_user.id, text = char.icon + char.name + ':\n❤️ ' + str(char.hp) + '\n⚔️ ' + str(char.dmg) + '\n💥 ' + str(char.crit), reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_choice)

def boss_stats(x):
   #назначение босса и его уникальных свойств
   global boss

   if x == 'Палыч':
      boss = Characters.Boss('Палыч', 800, 200, 0, 0, 0, 'Раздает перманентные баны')
      
   elif x == 'Чайковский':
      boss = Characters.Boss('Чайковский', 600, 250, 0, 0, 0, 'Одна святая песня воскрешает его перед порогом смерти')
      boss.resurrection = True

   elif x == 'Вив':
      boss = Characters.Boss('Вив', 900, 100, 0, 0, 0, 'В конце хода наваливает бассов повышая свой урон')

   elif x == 'Саша Шлякин':
      boss = Characters.Boss('Саша Шлякин', 1000, 200, 20, 0, 0, 'Убей его и возвысь себя')

   elif x == 'Качаловская Тварь':
      boss = Characters.Boss('Качаловская Тварь', 800, 50, 0, 0, 0, 'Бить ее больно и крайне неприятно, себе хуже только сделаешь')
      boss.returnal_value = 50

   elif x == 'Рандом Рандомыч':
      boss = Characters.Boss('Рандом Рандомыч', random.randint(100, 1001), random.randint(10, 301), random.randint(0, 51), random.randint(0, 51), 0, 'Может быть лох, а может и бог')
      boss.returnal_value = random.randint(0, 51)
      boss.regen = random.randint(0, 301)

   elif x == 'Котенок-тролль':
      boss = Characters.Boss('Котенок-тролль', 1000, 200, 0, 0, 0, 'Вислоухий и пузатый, мурчанием вызывает бессилие, еще может закогтить тебя')
      boss.endskill_value = 50

   elif x == 'Инквизиция':
      boss = Characters.Boss('Инквизиция', 500, 500, 50, 0, 0, 'Неопытных юзеров может моментально умертвить, тут уж как повезет')

   elif x == 'Доктор Леха':
      boss = Characters.Boss('Доктор Леха', 1500, 300, 0, 0, 0, 'Может провести вихревой удар джаггернаута своей сумкой')
      boss.endskill_value = 36

   elif x == 'Пьяный Леха':
      boss = Characters.Boss('Пьяный Леха', 1200, 100, 0, 0, 0, 'В конце хода накидывает еще коктейльчик, становясь опаснее')

   elif x == 'Мел':
      boss = Characters.Boss('Мел', 50, 0, 0, 90, 0, 'Отсутвие гордости делает его не восприимчивым к урону, замешкаешься - зальет блазуху тебе в ухо')

   elif x == 'Рыжий':
      boss = Characters.Boss('Рыжий', 2000, 100, 0, 0, 0, 'Находясь с ним рядом ты травишь свою жизнь, живучая падла')
      boss.regen = 300

   elif x == 'Следователь':
      boss = Characters.Boss('Следователь', 1500, 100, 0, 50, 0, 'Если успеет заполнить на тебя доки - будешь упакован в тюрьму')
      boss.busted_level = 10

   elif x == 'Донер Кебаб':
      boss = Characters.Boss('Донер Кебаб', 1800, 350, 0, 0, 0, 'При нем лучше не бухать, травля эту мразь делает сильнее')

   elif x == 'Черный Стас':
      boss = Characters.Boss('Черный Стас', 1500, 300, 0, 0, 0, 'Правильно выбирай слова для его осадки - закинет за всю хуйню обратно')

   elif x == 'Дрон':
      boss = Characters.Boss('Дрон', 2000, 100, 0, 0, 0, 'Доведешь Андрея до обиды - умрешь в его глазах')
      boss.obida_level = 5

   elif x == 'Валера Гладиатор':
      boss = Characters.Boss('Валера Гладиатор', 3000, 200, 0, 0, 0, 'Владеет арсеналом фирменных гадз')

   elif x == 'Великая Шива':
      boss = Characters.Boss('Великая Шива', 2000, 500, 0, 30, 0, 'Божественность дает ей шанс на уворот, с каждым ходом становится критичнее')

   elif x == 'Король Макар':
      boss = Characters.Boss('Король Макар', char.hp, char.dmg, char.crit, char.miss, char.vamp, 'Пока что финальный, твои статы - его статы')

   elif x == 'Гомогомозеки':
      boss = Characters.Boss('Гомогомозеки', 2000, 300, 20, 0, 0, 'Голые, рельефные и агрессивно-активно настроенные')
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
      boss_list = ['Король Макар']

   #выбор босса, удаление его из пула боссов и применение его статов
   boss_name = random.choice(boss_list)
   boss_list.remove(boss_name)
   boss_stats(boss_name)

   #проверка в розыске ли персонаж
   if parameters.wanted_level == True:
      boss.resurrection = True
      bot.send_message(message.from_user.id, 'Босс был усилен стражами порядка')

   #проверка на является ли персонаж Сашей Шлякиным при битве с Сашей Шлякиным
   if boss.name == 'Саша Шлякин' and char.name != 'Саня':
      bot.send_message(message.from_user.id, boss.name + '\n🖤 ' + str(boss.hp) + '\n⚔️ ' + str(boss.dmg) + '\n💥 ' + str(boss.crit))
      bot.send_message(message.from_user.id, 'Саша Шлякин нападает только на самого себя, подберем тебе другого')
      boss_choice(message)
   else:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add('А где это я?')
      msg = bot.send_message(message.from_user.id, text = boss.name + '\n🖤 ' + str(boss.hp) + '\n⚔️ ' + str(boss.dmg) + '\n💥 ' + str(boss.crit) + '\n' + boss.dscr, reply_markup=keyboard)
      bot.register_next_step_handler(msg, location)

def location_choice(x):
   #описание локаций и их свойств на персонажа
   global loc

   if x == 'Хата Колбаса':
      loc = Locations.Location(10, 'Нахождение здесь насыщает тебя благовонием помойки!\n-10%❤️', '📚')
      char.hp -= char.hp * loc.value_1 // 100
      if boss.name == 'Донер Кебаб':
         boss.hp += 500
         loc.loc_effect_msg = 'Ой ой, Донер у Колбаса стал крепче' + '\n+500🖤'
   
   elif x == 'Полазна':
      loc = Locations.SuperLocation(20, 10, 'Палаточные осознанки повысили твою духовность и снизили враждебность\n+20%❤️\n-10%⚔️', '⛺️')
      char.hp += char.hp * loc.value_1 // 100
      char.dmg -= char.dmg * loc.value_2 // 100

   elif x == 'Город Богов':
      loc = Locations.UltraLocation(10, 10, 10, 'Прогулка по нему разносторонне возвышает тебя\n+10%❤️\n+10%⚔️\n+10%💥', '⚓️')
      char.hp += char.hp * loc.value_1 // 100
      char.dmg += char.dmg * loc.value_2 // 100
      char.crit += loc.value_3
      if boss.name == 'Чайковский':
         boss.hp += 100
         boss.dmg += 50
         boss.crit += 10
         loc.loc_effect_msg = 'Чайковский здесь чувствует приток самопиздатости\n+100🖤\n+50⚔️\n+10💥'

   elif x == 'Бэд Трип':
      loc = Locations.SuperLocation(20, 20, 'Тебя занесло в Бэд Трип! Вот незадача!\n', '😵')
      if char.name == 'Коля':
         char.hp_baff(300)
         char.dmg_baff(100)
         loc.loc_effect_msg = 'Коля любит бэд трипы\n+300❤️\n+100⚔️'
      elif char.name == 'Темыч':
         loc.loc_effect_msg = 'Темыч так и не понял что был в бэде, а значит этого не было!'
      elif char.name != 'Коля' and char.name != 'Темыч':
         char.hp -= char.hp * loc.value_1 // 100
         char.dmg -= char.dmg * loc.value_2 // 100
         loc.loc_effect_msg = '-20%❤️\n-20%⚔️'
      
   elif x == 'Молебка':
      loc = Locations.SuperLocation(20, 10, 'Медитативный псайденс измотал тебя, но в итоге ты стал сильнее\n', '🎇')
      if char.name == 'Тошик':
         char.hp += char.hp * loc.value_1 // 100
         char.dmg += char.dmg * loc.value_2 // 100
         loc.loc_effect_msg = 'Но Тошика так просто не измотаешь\n+20%❤️\n+10%⚔️'
      elif char.name != 'Тошик':
         char.hp -= char.hp * loc.value_1 // 100
         char.dmg += char.dmg * loc.value_2 // 100
         loc.loc_effect_msg = '-20%❤️\n+10%⚔️'
      
   elif x == 'Армия':
      loc = Locations.SuperLocation(50, 30, 'Военкомат добрался до вас, сэр! Армия забрала год твоей жизни, но ты неплохо так подкачался\n-50%❤️\n+30%⚔️', '🧨')
      char.hp -= char.hp * loc.value_1 // 100
      char.dmg += char.dmg * loc.value_2 // 100

   elif x == 'Дрочильня':
      loc = Locations.SuperLocation(10, 10, 'Тренировка в тесном мужском кругу лишней не бывает, да?\n+10%⚔️\n+10%💥\n', '💦')
      char.dmg += char.dmg * loc.value_1 // 100
      char.crit_baff(loc.value_2)
      if char.name == 'Саня':
         char.crit_baff(loc.value_2)
         loc.loc_effect_msg = 'Да, Саша?\n+10%💥'

   elif x == '25й этаж':
      loc = Locations.SuperLocation(50, 10, 'Святое место, где настоящие убийцы смотрят в пол\n-50%⚔️\n-10%💥', '💀')
      char.dmg -= char.dmg * loc.value_1 // 100
      char.crit_debaff(loc.value_2)
      if char.name == 'Коля':
         char.hp -= char.hp * 20 // 100
         loc.loc_effect_msg = 'Коле здесь явно не место\n-20%❤️'
      elif char.name == 'Митя':
         char.hp += char.hp * 20 // 100
         loc.loc_effect_msg = 'Митя тут, как рыба в воде\n+20%❤️'

def police_check(message):
   #применение свойств повышенного до 100% уровня полиции

   char.busted_level = 0

   if message.text == 'Отсидеть':
      char.hp_baff(random.randint(-500,500))
      char.dmg_baff(random.randint(-200,200))
      char.crit_baff(random.randint(-20,20))
      msg_text_1 = 'Тюрьма кардиАнально преобразила тебя! Теперь у тебя есть воровской карман'
      msg_text_2 = 'Спасибо'

   elif message.text == 'Сбежать':
      parameters.wanted_level = True
      msg_text_1 = 'Побег дело святое, но теперь ты в розыске'
      msg_text_2 = 'Сам ты в розыске'

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(msg_text_2)
   msg = bot.send_message(message.from_user.id, text = msg_text_1, reply_markup=keyboard)
   bot.register_next_step_handler(msg, shop_choice)

def location(message):
   #выбор рандомной локации, применение ее свойств и вывод ее описания

   location_list = ['Хата Колбаса', 'Полазна', 'Город Богов', 'Бэд Трип', 'Молебка', 'Армия', 'Дрочильня', '25й этаж']
   location_name = random.choice(location_list)

   location_choice(location_name)

   bot.send_message(message.from_user.id, loc.icon + location_name + loc.icon + '\n' + loc.dscr)
   if loc.loc_effect_msg != False:
      bot.send_message(message.from_user.id, loc.loc_effect_msg)

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add('ПОГНАЛИ')
   msg = bot.send_message(message.from_user.id, text = 'Твои статы:\n❤️ ' + str(char.hp) + '\n⚔️ ' + str(char.dmg) + '\n💥 ' + str(char.crit), reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_prelude)

def boss_prelude(message):
   #описание первого скилла босса перед началом боя
   
   if boss.name == 'Палыч':
      char.silence = True
      bot.send_message(message.from_user.id, 'Палыч завалил твой ебалыч - скиллы и предметы не поюзать')
      start_fight(message)

   elif boss.name == 'Вив' and char.item == 'Травмат Володи':
      char.hp_debaff(300)
      char.bleeding = True
      char.item = 'Пусто'
      bot.send_message(message.from_user.id, 'Володя забрал свой травмат!\n' + char.icon + '-300❤️🩸')
      start_fight(message)

   elif boss.name == 'Рыжий':
      char.poison = True
      bot.send_message(message.from_user.id, char.icon + ' + 🦠')
      start_fight(message)

   elif boss.name == 'Следователь':
      drugs = 'Шига', 'Мадам', 'Почтовые марки'
      cross_check = [x for x in drugs if x in char.all_items]
      if char.dmg > 500:
         char.dmg //= 2
         bot.send_message(message.from_user.id, '👮‍♂️: Чет многовато у вас дамага, молодой человек\n' + char.icon + '-50%⚔️')
      if char.elex_count > 0 or len(cross_check) > 0:
         char.busted_level += 50
         bot.send_message(message.from_user.id, '👮‍♂️: Употребляли? Тогда быстрее вас упакуем\nСтепень упаковки +50%')
      start_fight(message)

   elif boss.name == 'Дрон':
      obida_level = 0
      obida_level += len(char.all_items) * 5
      bot.send_message(message.from_user.id, 'За каждый поход к братишкам\n🤬+5%')
      if 'Мясо Андрея' in char.all_items:
         obida_level += 10
         bot.send_message(message.from_user.id, 'А за то что ты ел мясо Андрея\n🤬+10%')
      start_fight(message)

   elif boss.name == 'Донер Кебаб':
      if 'Костюм Эверласт' in char.all_items:
         boss.hp += boss.hp * 10 // 100
         boss.dmg += boss.dmg * 10 // 100
         bot.send_message(message.from_user.id, 'Донер спиздил твой костюм!\n+10%🖤\n+10%⚔️')
      elif '2.5-литровка Колы' == char.item:
         char.hp_debaff(500)
         boss.hp_debaff(500)
         bot.send_message(message.from_user.id, 'Открывая твою Колу, Донер захуярил и себя, и тебя, и обои!\n-500❤️\n-500🖤')
      start_fight(message)

   elif boss.name == 'Черный Стас' and char.name == 'Митя':
      boss.dmg += char.elex_count * 200
      bot.send_message(message.from_user.id, 'Стас, по-справедливости, бахает столько же эликсиров, что и Митя')
      start_fight(message)

   else: start_fight(message)

def start_fight(message):
   #выбор действия игрока в начале раунда боя
   
   if char.busted_level >= 100:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add('Отсидеть', 'Сбежать')
      msg = bot.send_message(message.from_user.id, text = 'Воу воу парень, ты доигрался, милости прошу в автозак', reply_markup=keyboard)
      bot.register_next_step_handler(msg, police_check)

   else:
      boss_startskill(message)

      bot.send_message(message.from_user.id, versus_stats(char.name, boss.name))

      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add('Атака', char.skill_name, char.item)
      msg = bot.send_message(message.from_user.id, text = 'Ходи, друг', reply_markup=keyboard)
      bot.register_next_step_handler(msg, action_choice)

def action_choice(message):
   #применение выбранного игроком действия

   if message.text == 'Атака':
      attack_turn(message)

   elif message.text == char.skill_name:
      if char.cooldown <= 0 and char.silence == False and char.stan_timer <= 0:
         char.cooldown = 0
         skill(char.name)
         bot.send_message(message.from_user.id, skill_description)
      elif char.stan_timer > 0:
         bot.send_message(message.from_user.id, 'Не прокатит бро, ты в стане')
      elif char.silence == True:
         bot.send_message(message.from_user.id, 'Сорян, но ты забанен')
      elif char.cooldown > 0:
         bot.send_message(message.from_user.id, 'Обломись, там перезарядка')
      victory_check(message)

   elif message.text == char.item:
      if char.item != 'Пусто' and char.silence == False and char.stan_timer <= 0:
         item_using(char.item)
         char.item = 'Пусто'
         bot.send_message(message.from_user.id, item_dscr)
      elif char.stan_timer > 0:
         bot.send_message(message.from_user.id, 'Не прокатит бро, ты в стане')
      elif char.item != 'Пусто' and char.silence == True:
         bot.send_message(message.from_user.id, 'Сорян, но ты забанен')
      elif char.item == 'Пусто':
         bot.send_message(message.from_user.id, 'Не прокатит, друг')   
      victory_check(message)

def attack_turn(message):

   char.cooldown -= 1

   #проверка на уворот босса
   if chance(boss.miss) == True:
      b_m_indent = ' ' * 9 + str(boss.miss) + '%'
      if boss.name == 'Мел':
         boss.blazer_level += 1
         bot.send_message(message.from_user.id, 'Мелу похуй на твой урон\n')
         bot.send_message(message.from_user.id, '🛡Уворотка🛡\n' + b_m_indent)
      else:
         bot.send_message(message.from_user.id, 'Босс пропустил твой урон\n')
         bot.send_message(message.from_user.id, '🛡Уворотка🛡\n' + b_m_indent)

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
   if boss.name == 'Дрон':
      boss.obida_level += 5
   elif boss.name == 'Следователь':
      char.busted_level += 20

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add('Закончить ход')
   msg = bot.send_message(message.from_user.id, versus_stats(char.name, boss.name), reply_markup=keyboard)
   bot.register_next_step_handler(msg, victory_check)
      
def skill(x):
   #использование скилла персонажа
   global skill_description

   if x == 'Митя':
      char.hp_debaff(100)
      char.dmg_baff(200)
      char.cooldown = 1
      char.elex_count += 1
      skill_description = '-100❤️\n+200⚔️\n🕒1 ход'

   elif x == 'Саня':
      damage = random.randint(50, 500)
      boss.hp_debaff(damage)
      char.cooldown = 3
      skill_description = boss.icon + '-' + str(damage) + '🖤\n🕒3 хода'

   elif x == 'Тошик':
      char.hp += char.hp * 20 // 100
      char.cooldown = 2
      skill_description = '+20%❤️\n🕒2 хода'

   elif x == 'Коля':
      hack_value = boss.dmg * 50 // 100
      char.dmg += hack_value
      boss.dmg -= hack_value
      char.cooldown = 3
      skill_description = boss.icon + '-' + str(hack_value) + '⚔️\n' + char.icon + '+' + str(hack_value) + '⚔️\n🕒3 хода'

   elif x == 'Темыч':
      skill_check_temich = chance(21)
      if skill_check_temich == False:
         boss.hp, char.hp = char.hp, boss.hp
         char.cooldown = 1
         skill_description = '❤️🔄🖤\n🕒1 ход'
      elif skill_check_temich == True:
         char.stan_timer = 1
         skill_description = 'Ой ой, Темыч запутался в своей суете\n' + char.icon + '+💤'

def item_using(x):
   #использование предмета персонажа
   global item_dscr

   if x == 'Жигули':
      if boss.name == 'Донер Кебаб':
         boss.hp_baff(150)
         item_dscr = 'Пизда твоему бухлу, Донер его выпил\n' + boss.icon + '+150🖤'
      else:
         char.hp_baff(150)
         item_dscr = 'Для истинных ценителей\n+150❤️'

   elif x == 'Сидр':
      if boss.name == 'Донер Кебаб':
         boss.hp_baff(300)
         item_dscr = 'Пизда твоему бухлу, Донер его выпил\n' + boss.icon + '+300🖤'
      else:
         char.hp_baff(300)
         item_dscr = 'Питерская эстетика\n+300❤️'

   elif x == 'Балабаха Багбира':
      if boss.name == 'Донер Кебаб':
         boss.hp_baff(500)
         item_dscr = 'Пизда твоему бухлу, Донер его выпил\n' + boss.icon + '+500🖤'
      else:
         char.hp_baff(500)
         item_dscr = 'Со вкусом молодости\n+500❤️'

   elif x == 'Святая минералочка':
      char.regen = 100
      item_dscr = 'Освежающий глоток придал тебе сил\n' + char.icon + ' + 💕'

   elif x == 'Лезвия бритвы':
      boss.hp_debaff(150)
      boss.bleeding = True
      item_dscr = 'Бросок в глаз! Враг травмирован\n' + boss.icon + '-150🖤🩸'

   elif x == 'Травмат Володи':
      boss.hp_debaff(300)
      boss.bleeding = True
      item_dscr = 'Документы должны быть всегда с собой\n' + boss.icon + '-300🖤🩸'

   elif x == '2.5-литровка Колы':
      boss.hp_debaff(500)
      item_dscr = 'Грозное оружие судного нового года\n' + boss.icon + '-500🖤'

   elif x == 'Потный носок':
      if boss.name == 'Донер Кебаб':
         boss.hp_baff(50)
         boss.regen = 100
         item_dscr = 'Не стоило травить Донера\n' + boss.icon + '+50🖤💕'
      else:
         boss.hp_debaff(50)
         boss.poison = True
         item_dscr = boss.name + ' поймал твой носок лицом\n' + boss.icon + '-50🖤🦠'

   elif x == 'Блевотный харчок':
      if boss.name == 'Донер Кебаб':
         boss.hp_baff(200)
         boss.regen = 100
         item_dscr = 'Не стоило травить Донера\n' + boss.icon + '+200🖤💕'
      else:
         boss.hp_debaff(200)
         boss.poison = True
         item_dscr = 'Пздц ты жесткий, нашел чем замастить врага\n' + boss.icon + '-200🖤🦠'

   elif x == 'Рампаг':
      if boss.name == 'Донер Кебаб':
         boss.hp = 0
         item_dscr = 'Рампаг заходит сзади! Моментальная смерть для Донера!'
      else:
         boss.stan_timer = 1
         item_dscr = 'Удар Рампагом! Враг в отрубе\n👿 + 💤'

   elif x == 'Золотые Ролексы':
      char.cooldown = 0
      item_dscr = 'Дороговаты, зато кулдаун скилла сбросили'

   elif x == 'Вакцина':
      char.poison = False
      char.bleeding = False
      item_dscr = 'Лечит от всех твоих недугов\n❌🩸🦠❌'

   elif x == 'Шига':
      foods = 'Сочник со сгухой', 'Дубайский шаурмец', 'Мясо Андрея', '5 пицц'
      cross_check = [x for x in foods if x in char.all_items]
      if len(cross_check) == 0:
         char.hp_debaff(200)
         char.dmg_baff(100)
         item_dscr = 'Душисто залетела, но теперь ты голоден\n-200❤️\n+100⚔️'
      elif len(cross_check) > 0:
         char.hp_baff(200)
         char.dmg_baff(100)
         item_dscr = 'Душисто залетела, а еда спасла тебя от голода\n+200❤️\n+100⚔️'

   elif x == 'Мадам':
      boss.dmg -= boss.dmg * 50 // 100
      item_dscr = 'Мадам умиротворяет всех вокруг\n' + boss.icon + '-50%⚔️'

def boss_startskill(message):
   #вывод сообщения о примененном навыке босса в конце раунда
   if boss.name == 'Следователь':
      bot.send_message(message.from_user.id, '⛓Степень упаковки ' + str(char.busted_level) + '%⛓')
   
   elif boss.name == 'Дрон':
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
   if char.name == 'Митя' and boss.name == 'Инквизиция':
      char.hp += char.hp * 50 // 100
      bot.send_message(message.from_user.id, 'Вместо урона Митя в инквизиции становится сильнее, она не может причинить ему урон!\n+50%❤️')
   
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

   if boss.name == 'Чайковский' and boss.resurrection == True and boss.hp <= 200:
      boss.resurrection = False
      boss.hp_baff(800)
      bot.send_message(message.from_user.id, 'Брат! Не засыпай!\n' + boss.icon + '+800🖤')
   
   elif boss.name == 'Вив':
      boss.dmg_baff(100)
      bot.send_message(message.from_user.id, 'Бассы подъехали!\n' + boss.icon + '+100⚔️')

   elif boss.name == 'Котенок-тролль' and chance(boss.endskill_value) == True:
      kitty_choice = random.randint(0, 11)
      if kitty_choice > 5:
         char.stan_timer = 1
         bot.send_message(message.from_user.id, 'Мурлы-сна!\n' + char.icon + '+💤')
      elif kitty_choice <= 5:
         char.hp_debaff(200)
         char.bleeding = True
         bot.send_message(message.from_user.id, 'Зацепка когтями!\n' + char.icon + '-200❤️🩸')
   
   elif boss.name == 'Пьяный Леха':
      boss.hp += boss.hp * 50 // 100
      boss.dmg += boss.dmg * 50 // 100
      bot.send_message(message.from_user.id, 'Леха бухает! Остановите его!\n' + boss.icon + '+50%🖤 и +50%⚔️')

   elif boss.name == 'Доктор Леха' and chance(boss.endskill_value) == True:
      char.hp_debaff(500)
      char.bleeding = True
      bot.send_message(message.from_user.id, 'Джагернаааааут!\n' + char.icon + '-500❤️🩸')

   elif boss.name == 'Мел' and boss.blazer_level >= 3:
      boss.blazer_level = 0
      char.hp_debaff(500)
      bot.send_message(message.from_user.id, 'Мел залил тебе блазуху в ухо!\n' + char.icon + '-500❤️')

   elif boss.name == 'Дрон':
      if chance(boss.obida_level) == True:
         char.hp_debaff(1000)
         bot.send_message(message.from_user.id, '☠️Дрон затаил лютую обиду!☠️')

   elif boss.name == 'Валера Гладиатор':
      gadza_choice = random.randint(1, 6)
      if gadza_choice == 1:
         char.hp_debaff(500)
         bot.send_message(message.from_user.id, 'Твин-турбо гадза на минус уши\n' + char.icon + '-500❤️')
      elif gadza_choice == 2:
         boss.hp_baff(500)
         bot.send_message(message.from_user.id, 'Церковная целебная гадза\n' + boss.icon + '+500🖤')
      elif gadza_choice == 3:
         boss.crit_baff(25)
         bot.send_message(message.from_user.id, 'Кошачья критическая гадза\n' + boss.icon + '+25%💥')
      elif gadza_choice == 4:
         char.dmg_debaff(250)
         bot.send_message(message.from_user.id, 'Эльфийская гадза с эффектом попускания\n' + char.icon + '-250⚔️')
      elif gadza_choice == 5:
         char.poison = True
         bot.send_message(message.from_user.id, 'Ядовитая гадза по-киевски\n' + char.icon + '+🦠')

   elif boss.name == 'Великая Шива':
      if boss.crit < 100:
         boss.crit_baff(20)
         bot.send_message(message.from_user.id, 'Криты завезли!\n' + boss.icon + '+20%💥')
      elif boss.crit == 100:
         boss.dmg_baff(boss.dmg * 2)
         bot.send_message(message.from_user.id, 'Урон завезли!\n' + boss.icon + '+100%⚔️')

def victory_check(message):
   #проверка на победу в раунде

   if boss.hp > 0 and char.hp > 0:
      start_fight(message)

   elif boss.hp <= 0 and char.hp > 0 and boss.name == 'Король Макар':
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add('ДАВАЙ ЕЩЕ РАЗОК')
      msg = bot.send_message(message.from_user.id, text = '🥳Похоже ты победил. Круто🥳', reply_markup=keyboard)
      bot.register_next_step_handler(msg, get_character)

   elif boss.hp <= 0 and char.hp > 0 and boss.name != 'Король Макар':
      next_fight(message)

   elif char.hp <= 0: 
      bot.send_message(message.from_user.id, '👻Увы, но ты проебал, старина👻\nНапиши мне что-нибудь и начнем сначала')

def next_fight(message):
   #конец боя после победы

   char.cooldown = 0
   parameters.win_rate += 1
   char.poison = False
   char.bleeding = False
   char.silence = False
   parameters.poison_dmg = 5
   char.busted_level = 0

   if parameters.win_rate < 8 and boss.name == 'Саша Шлякин':
      char.hp += char.hp * 20 // 100
      char.dmg += char.dmg * 20 // 100
      char.crit_baff(5)
      bot.send_message(message.from_user.id, 'Победа над собой возвысила тебя!\n+20%❤️\n+20%⚔️\n+5%💥')

   elif parameters.win_rate < 8 and char.name == 'Тошик':
      char.dmg += char.hp * 5 // 100
      bot.send_message(message.from_user.id, 'Твое здоровье - твоя сила\n⚔️+5%❤️')

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add('Я молодец')
   msg = bot.send_message(message.from_user.id, text = 'Ты победил, слабина', reply_markup=keyboard)
   bot.register_next_step_handler(msg, shop_choice)

bot.polling(none_stop=True, interval=0)