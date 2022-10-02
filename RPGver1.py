# -*- coding: utf-8 -*-

from telebot import TeleBot
from telebot import types
import random
bot = TeleBot('2102427745:AAECFy-T6GfMWH1VNshsucAEXZEfzmGUZBk')

def chance(x):
   #генератор вероятности
   chance = random.randint(1, 100) in range(1, x)
   return chance

def game_parameters():
   global poison_damage
   global win_rate
   global jail_respect
   global jail_disrespect
   global jail_simpaty
   global wanted
   global item_list
   global buff_list
   global boss_level_one
   global boss_level_two
   global boss_level_three

   poison_damage = 10
   win_rate = 0
   jail_respect = 0
   jail_disrespect = 0
   jail_simpaty = 0
   wanted = False

   item_list = ['Жигули', 'Лезвия бритвы', 'Потный носок', 'Шига', 'Святая минералочка', 'Золотые Ролексы', 'Сидр',
    '2.5-литровка Колы', 'Блевотный харчок', 'Мадам',
    'Рампаг', 'Вакцина', 'Балабаха Багбира', 'Травмат Володи']

   buff_list = ['Сочник со сгухой', 'Гитара', 'Костюм Эверласт', 'Сыграть в шахматы', 'Дубайский шаурмец', 'Мясо Андрея',
    'Башкерме взрывай', 'Почтовые марки', 'Поиграть на варгане', 'Благословение Шивы', '5 пицц', 'Пика точеная', 'Лимонная голодовочка',
     'Огромный дилдак', 'Благословение Макара', 'Черный чупа чупс']

   boss_level_one = ['Палыч', 'Чайковский', 'Вив', 'Саша Шлякин', 'Качаловская Тварь', 'Рандом Рандомыч', 'Котенок-тролль']
   boss_level_two = ['Инквизиция', 'Доктор Леха', 'Пьяный Леха', 'Мел', 'Рыжий', 'Следователь']
   boss_level_three = ['Донер Кебаб', 'Черный Стас', 'Дрон', 'Валера Гладиатор', 'Великая Шива']

def stas_passive(x):
   #чек на возвращение урона Черного Стаса
   global return_check
   return_check = boss_name == 'Черный Стас' and chance(x) == True
   return return_check
   
def versus_stats(x, y):
   #отображение статистики боя
   str1 = char_icon + x + ' 🆚 ' + y + boss_icon
   str2 = '❤️' + str(char_health)
   str3 = '🖤' + str(boss_health)
   str4 = '⚔️' + str(char_damage)
   str5 = '⚔️' + str(boss_damage)
   z = len(str2) - len(str3)
   indent1 = ' ' * 8
   indent2 = ' ' * (8 + z)
   result = str1 + '\n' + str2 + indent1 + str3 + '\n' + str4 + indent2 + str5
   return result

def bleeding(message):
   #кровотечение
   global char_health
   global boss_health

   if char_bleeding == True and char_immunity == False:
      char_health -= 100
      bot.send_message(message.from_user.id, '🩸Кровотечение🩸\n' + char_icon + '-100❤️')

   elif boss_bleeding == True:
      boss_health -= 100
      bot.send_message(message.from_user.id, '🩸Кровотечение🩸\n' + boss_icon + '-100🖤')

def poison(message):
   #яд
   global char_health
   global boss_health
   global poison_damage

   if char_poison == True and char_immunity == False:
      char_health -= char_health * poison_damage // 100
      bot.send_message(message.from_user.id, '🦠Отравление🦠\n-' + str(poison_damage) + '%❤️')
      poison_damage += 10
   if boss_poison == True:
      boss_health -= boss_health * poison_damage // 100
      bot.send_message(message.from_user.id, '🦠Отравление🦠\n-' + str(poison_damage) + '%🖤')
      poison_damage += 10

def regeneration(message):
   global char_health
   global boss_health

   if char_regen > 0:
      char_health += char_regen
      bot.send_message(message.from_user.id, '💕Регенерация💕\n' + char_icon + '+' + str(char_regen) + '❤️')
   if boss_regen > 0:
      boss_health += boss_regen
      bot.send_message(message.from_user.id, '💕Регенерация💕\n' + boss_icon + '+' + str(boss_regen) + '🖤')

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
   global char_name
   global char_health
   global char_damage
   global char_crit
   global char_miss
   global char_skill_name
   global char_cooldown
   global char_regen
   global char_vampire
   global char_item
   global char_icon
   global char_poison
   global char_bleeding
   global char_stan_timer
   global char_silence
   global char_immunity
   global all_char_items
   global elex_count
   global sueta_count
   global busted_level

   char_name = message.text
   char_item = 'Пусто'
   all_char_items = []
   char_stan_timer = 0
   char_cooldown = 0
   char_regen = 0
   char_vampire = 0
   busted_level = 0
   elex_count = 0
   char_poison = False
   char_bleeding = False
   char_silence = False
   char_immunity = False
   
   if char_name == 'Митя':
      char_health = 800
      char_damage = 100
      char_crit = 0
      char_miss = 0
      char_vampire += 20
      char_skill_name = 'Бахнуть эликсир'
      char_icon = '👨‍🔬'
      char_dscr = '❤️800\n⚔️100\n💥0\nМастер отсоса жизни\nЛюбитель губительно-усиливающих эликсиров, будь с ними осторожен'
      
   elif char_name == 'Саня':
      char_health = 1000
      char_damage = 200
      char_crit = 30
      char_miss = 0
      char_skill_name = 'Кинуть ножницы'
      char_icon = '💇'
      char_dscr = '❤️1000\n⚔️200\n💥30\nЭзотерический парикмахер\nМастер чистого белого неделимого броска ножницами'
      
   elif char_name == 'Тошик':
      char_health = 1500
      char_damage = 100
      char_crit = 0
      char_miss = 0
      char_skill_name = 'Сесть медитировать'
      char_icon = '🦹‍♂️'
      char_dscr = '❤️1500\n⚔️100\n💥0\nПсайтанковый медитатор\nБольше здоровья - больше силы'
      
   elif char_name == 'Коля':
      char_health = 1200
      char_damage = 100
      char_crit = 0
      char_miss = 0
      char_skill_name = 'Хакнуть урон'
      char_icon = '👨‍💻'
      char_dscr = '❤️1200\n⚔️100\n💥0\nХипстерский программист\nПадок на разочарование'
      
   elif char_name == 'Темыч':
      char_health = 800
      char_damage = 150
      char_crit = 0
      char_miss = 15
      char_skill_name = 'Навести суету'
      sueta_count = 0
      char_icon = '🤷‍♂️'
      char_dscr = '❤️800\n⚔️150\n💥0\nНетикающий суетолог\nЕсли не поймет что понес урон - значит этого не было'

   bot.send_message(message.from_user.id, char_name + char_icon + '\n' + char_dscr)
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
   global char_health
   global char_damage

   buff_choice = [random.choice(buff_list), random.choice(buff_list), random.choice(buff_list)]
   item_choice = [random.choice(item_list), random.choice(item_list), random.choice(item_list)]
   
   if message.text == 'Лавка Серого Стаса':
      char_damage += 50
      bot.send_message(message.from_user.id, 'Стас тебя угостил чем-то мощным, чувствуешь себя сильнее! Давай глянем что он там еще наворовал\n+50⚔️')
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(item_choice[0], item_choice[1], item_choice[2])
      msg = bot.send_message(message.from_user.id, text = 'Бери что-то одно', reply_markup=keyboard)
      bot.register_next_step_handler(msg, items_upgrade)

   elif message.text == 'Братишкино логово':
      char_health += 200
      bot.send_message(message.from_user.id, 'Братишки приветсвуют тебя в своем логове! Сядь браток, попей улун молочный, он тебя подлечит\n+200❤️')
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(buff_choice[0], buff_choice[1], buff_choice[2])
      msg = bot.send_message(message.from_user.id, text = 'Бери что-то одно', reply_markup=keyboard)
      bot.register_next_step_handler(msg, stats_upgrade)

def items_upgrade(message):
   global char_item

   x = message.text
   char_item = x
   item_list.remove(x)
   
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add('А с кем деремся?')
   msg = bot.send_message(message.from_user.id, text = 'Хороший выбор, батя', reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_choice)

def stats_upgrade(message):
   global char_health
   global char_damage
   global char_crit
   global char_vampire
   global all_char_items 

   x = message.text
   buff_list.remove(x)
   
   if x == 'Сочник со сгухой':
      char_health += char_health * 25 // 100
      buff_dscr = 'Сгущено-вареное блаженство\n+25%❤️'
   
   elif x == 'Дубайский шаурмец':
      char_health += char_health * 30 // 100
      buff_dscr = 'Неизменная классика\n+30%❤️'

   elif x == 'Мясо Андрея':
      char_health += char_health * 40 // 100
      buff_dscr = 'Держи его по-дальше от Дрона\n+40%❤️'

   elif x == '5 пицц':
      char_health += char_health * 50 // 100
      buff_dscr = 'Промкод на 5 пицц со скидкой 50%\n+50%❤️'

   elif x == 'Гитара':
      char_damage += char_damage * 15 // 100
      buff_dscr = 'Теперь ты - Рокер\n+15%⚔️'

   elif x == 'Башкерме взрывай':
      char_damage += char_damage * 25 // 100
      buff_dscr = 'Баааашкермееее!\n+25%⚔️'

   elif x == 'Пика точеная':
      char_damage += char_damage * 30 // 100
      buff_dscr = 'Ну хоть не хуй дроченый\n+30%⚔️'

   elif x == 'Огромный дилдак':
      char_damage += char_damage * 50 // 100
      buff_dscr = 'В умелых руках дает\n+50%⚔️'
   
   elif x == 'Костюм Эверласт':
      char_health += char_health * 10 // 100
      char_damage += char_damage * 10 // 100
      buff_dscr = 'Костюм Дани Эверласта, легенды миксфайта!\n+10%❤️\n+10%⚔️'

   elif x == 'Почтовые марки':
      char_health += char_health * 20 // 100
      char_damage += char_damage * 20 // 100
      buff_dscr = 'Ты смог уломать ребят на почтовые отправления!\n+20%❤️\n+20%⚔️'

   elif x == 'Лимонная голодовочка':
      char_health -= char_health * 30 // 100
      char_damage += char_damage * 50 // 100
      char_crit += 5
      buff_dscr = '24-часовая голодовка с братишками!\n-30%❤️\n+50%⚔️\n+5%💥'

   elif x == 'Сыграть в шахматы':
      char_crit += 5
      buff_dscr = 'Не важно проиграл ты или да\n+5%💥'
   
   elif x == 'Поиграть на варгане':
      char_crit += 10
      buff_dscr = 'Хорошая работа ртом и языком, дружище\n+10%💥'

   elif x == 'Черный чупа чупс':
      char_vampire += 10
      buff_dscr = 'Навык отсоса повышен!\n+10%🦇'

   elif x == 'Благословение Шивы':
      char_damage += char_damage * 50 // 100
      char_crit += 15
      buff_dscr = 'Великая Шива благоволит тебе воин!\n+50%⚔️\n+15%💥'

   elif x == 'Благословение Макара':
      char_health += char_health * 30 // 100
      char_damage += char_damage * 30 // 100
      char_crit += 10
      buff_dscr = 'Святейший Король Макар снизошел на тебя!\n+30%❤️\n+30%⚔️\n+5%💥'

   if x not in all_char_items:
      all_char_items.append(x)
   
   bot.send_message(message.from_user.id, buff_dscr)

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add('А с кем деремся?')
   msg = bot.send_message(message.from_user.id, text = 'Твои статы:\n❤️ ' + str(char_health) + '\n⚔️ ' + str(char_damage) + '\n💥 ' + str(char_crit), reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_choice)

def boss_stats(x):
   global boss_name
   global boss_health
   global boss_damage
   global boss_crit
   global boss_miss
   global boss_endskill_value
   global boss_returnal_value
   global boss_regen
   global boss_dscr
   global boss_stan_timer
   global boss_bleeding
   global boss_poison
   global boss_icon
   global boss_resurrection
   global obida_level
   global blazer_level
   global busted_level

   boss_crit = 0
   boss_miss = 0
   boss_endskill_value = 0
   boss_returnal_value = 0
   boss_regen = 0
   boss_stan_timer = 0
   boss_resurrection = False
   boss_bleeding = False
   boss_poison = False
   boss_icon = '👿'

   if x == 'Палыч':
      boss_health = 800
      boss_damage = 200
      boss_dscr = 'Раздает перманентные баны'
      
   elif x == 'Чайковский':
      boss_health = 600
      boss_damage = 250
      boss_resurrection = True
      boss_dscr = 'Одна святая песня воскрешает его перед порогом смерти'

   elif x == 'Вив':
      boss_health = 900
      boss_damage = 100
      boss_dscr = 'В конце хода наваливает бассов повышая свой урон'

   elif x == 'Саша Шлякин':
      boss_health = 1000
      boss_damage = 200
      boss_crit = 20
      boss_dscr = 'Убей его и возвысь себя'

   elif x == 'Качаловская Тварь':
      boss_health = 800
      boss_damage = 50
      boss_returnal_value = 50
      boss_dscr = 'Бить ее больно и крайне неприятно, себе хуже только сделаешь'

   elif x == 'Рандом Рандомыч':
      boss_health = random.randint(100, 1001)
      boss_damage = random.randint(10, 301)
      boss_crit = random.randint(0, 51)
      boss_miss = random.randint(0, 51)
      boss_returnal_value = random.randint(0, 51)
      boss_regen = random.randint(0, 301)
      boss_dscr = 'Может быть лох, а может и бог'

   elif x == 'Котенок-тролль':
      boss_health = 1000
      boss_damage = 200
      boss_endskill_value = 50
      boss_dscr = 'Вислоухий и пузатый, мурчанием вызывает бессилие, еще может закогтить тебя'

   elif x == 'Инквизиция':
      boss_health = 500
      boss_damage = 500
      boss_crit = 50
      boss_dscr = 'Неопытных юзеров может моментально умертвить, тут уж как повезет'

   elif x == 'Доктор Леха':
      boss_health = 1500
      boss_damage = 300
      boss_endskill_value = 36
      boss_dscr = 'Может провести вихревой удар джаггернаута своей сумкой'

   elif x == 'Пьяный Леха':
      boss_health = 1200
      boss_damage = 100
      boss_dscr = 'В конце хода накидывает еще коктейльчик, становясь опаснее'

   elif x == 'Мел':
      boss_health = 50
      boss_damage = 0
      boss_miss = 90
      blazer_level = 0
      boss_dscr = 'Отсутвие гордости делает его не восприимчивым к урону, замешкаешься - зальет блазуху тебе в ухо'

   elif x == 'Рыжий':
      boss_health = 2000
      boss_damage = 100
      boss_regen = 300
      boss_dscr = 'Находясь с ним рядом ты травишь свою жизнь, живучая падла'

   elif x == 'Следователь':
      boss_health = 1500
      boss_damage = 100
      boss_miss = 50
      busted_level = 10
      boss_dscr = 'Если успеет заполнить на тебя доки - будешь упакован в тюрьму'

   elif x == 'Донер Кебаб':
      boss_health = 1800
      boss_damage = 350
      boss_dscr = 'При нем лучше не бухать, травля эту мразь делает сильнее'

   elif x == 'Черный Стас':
      boss_health = 1500
      boss_damage = 300
      boss_dscr = 'Правильно выбирай слова для его осадки - закинет за всю хуйню обратно'

   elif x == 'Дрон':
      boss_health = 2000
      boss_damage = 100
      obida_level = 5
      boss_dscr = 'Доведешь Андрея до обиды - умрешь в его глазах'

   elif x == 'Валера Гладиатор':
      boss_health = 3000
      boss_damage = 200
      boss_dscr = 'Владеет арсеналом фирменных гадз'

   elif x == 'Великая Шива':
      boss_health = 2000
      boss_damage = 500
      boss_miss = 30
      boss_dscr = 'Божественность дает ей шанс на уворот, с каждым ходом становится критичнее'

   elif x == 'Король Макар':
      boss_health = char_health
      boss_damage = char_damage
      boss_crit = char_crit
      boss_miss = char_miss
      boss_dscr = 'Пока что финальный, твои статы - его статы'

   elif x == 'Гомогомозеки':
      boss_name = 'Гомогомозеки'
      boss_health = 2000
      boss_damage = 300
      boss_crit = 20
      boss_regen = 200
      boss_dscr = 'Голые, рельефные и агрессивно-активно настроенные'

def boss_choice(message):
   global boss_name
   global boss_resurrection

   if win_rate < 3:
      boss_list = boss_level_one
   elif win_rate < 6 and win_rate >= 3:
      boss_list = boss_level_two
   elif win_rate < 9 and win_rate >= 6:
      boss_list = boss_level_three
   elif win_rate == 9:
      boss_list = ['Король Макар']

   boss_name = random.choice(boss_list)
   boss_list.remove(boss_name)
   boss_stats(boss_name)

   if wanted == True:
      boss_resurrection = True
      bot.send_message(message.from_user.id, 'Босс был усилен стражами порядка')

   if boss_name == 'Саша Шлякин' and char_name != 'Саня':
      bot.send_message(message.from_user.id, boss_name + '\n🖤 ' + str(boss_health) + '\n⚔️ ' + str(boss_damage) + '\n💥 ' + str(boss_crit))
      bot.send_message(message.from_user.id, 'Саша Шлякин нападает только на самого себя, подберем тебе другого')
      boss_choice(message)
   else:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add('А где это я?')
      msg = bot.send_message(message.from_user.id, text = boss_name + '\n🖤 ' + str(boss_health) + '\n⚔️ ' + str(boss_damage) + '\n💥 ' + str(boss_crit) + '\n' + boss_dscr, reply_markup=keyboard)
      bot.register_next_step_handler(msg, location)

def location_choice(x):
   global char_health
   global char_damage
   global char_crit
   global boss_health
   global boss_damage
   global boss_crit
   global loc_icon
   global location_dscr
   global loc_effect_msg

   loc_effect_msg = False

   if x == 'Хата Колбаса':
      loc_icon = '📚'
      char_health -= char_health * 10 // 100
      location_dscr = 'Нахождение здесь насыщает тебя благовонием помойки!\n-10%❤️'
      if boss_name == 'Донер Кебаб':
         boss_health += 500
         loc_effect_msg = 'Ой ой, Донер у Колбаса стал крепче' + '\n+500🖤'
   
   elif x == 'Полазна':
      loc_icon = '⛺️'
      char_health += char_health * 20 // 100
      char_damage -= char_damage * 10 // 100
      location_dscr = 'Палаточные осознанки повысили твою духовность и снизили враждебность\n+20%❤️\n-10%⚔️'

   elif x == 'Город Богов':
      loc_icon = '⚓️'
      char_health += char_health * 10 // 100
      char_damage += char_damage * 10 // 100
      char_crit += 10
      location_dscr = 'Прогулка по нему разносторонне возвышает тебя\n+10%❤️\n+10%⚔️\n+10%💥'
      if boss_name == 'Чайковский':
         boss_health += 100
         boss_damage += 50
         boss_crit += 10
         loc_effect_msg = 'Чайковский здесь чувствует приток самопиздатости\n+100🖤\n+50⚔️\n+10💥'

   elif x == 'Бэд Трип':
      loc_icon = '😵'
      location_dscr = 'Тебя занесло в Бэд Трип! Вот незадача!\n'
      if char_name == 'Коля':
         char_health += 300
         char_damage += 100
         loc_effect_msg = 'Коля любит бэд трипы\n+300❤️\n+100⚔️'
      elif char_name == 'Темыч':
         loc_effect_msg = 'Темыч так и не понял что был в бэде, а значит этого не было!'
      elif char_name != 'Коля' and char_name != 'Темыч':
         char_health -= char_health * 20 // 100
         char_damage -= char_damage * 20 // 100
         loc_effect_msg = '-20%❤️\n-20%⚔️'
      
   elif x == 'Молебка':
      loc_icon = '🎇'
      location_dscr = 'Медитативный псайденс измотал тебя, но в итоге ты стал сильнее\n'
      if char_name == 'Тошик':
         char_health += char_health * 20 // 100
         char_damage += char_damage * 10 // 100
         loc_effect_msg = 'Но Тошика так просто не измотаешь\n+20%❤️\n+10%⚔️'
      elif char_name != 'Тошик':
         char_health -= char_health * 20 // 100
         char_damage += char_damage * 10 // 100
         loc_effect_msg = '-20%❤️\n+10%⚔️'
      
   elif x == 'Армия':
      loc_icon = '🧨'
      char_health -= char_health * 50 // 100
      char_damage += char_damage * 30 // 100
      location_dscr = 'Военкомат добрался до вас, сэр! Армия забрала год твоей жизни, но ты неплохо так подкачался\n-50%❤️\n+30%⚔️'

   elif x == 'Дрочильня':
      loc_icon = '💦'
      char_damage += char_damage * 10 // 100
      char_crit += 10
      location_dscr = 'Тренировка в тесном мужском кругу лишней не бывает, да?\n+10%⚔️\n+10%💥\n'
      if char_name == 'Саня':
         char_crit += 10
         loc_effect_msg = 'Да, Саша?\n+10%💥'

   elif x == '25й этаж':
      loc_icon = '💀'
      char_damage -= char_damage * 50 // 100
      char_crit -= 10
      location_dscr = 'Святое место, где настоящие убийцы смотрят в пол\n-50%⚔️\n-10%💥'
      if char_name == 'Коля':
         char_health -= char_health * 20 // 100
         loc_effect_msg = 'Коле здесь явно не место\n-20%❤️'
      elif char_name == 'Митя':
         char_health += char_health * 20 // 100
         loc_effect_msg = 'Митя тут, как рыба в воде\n+20%❤️'



def police_check(message):
   global busted_level
   global wanted

   busted_level = 0
   x = message.text
   if x == 'Отсидеть':
      bot.send_message(message.from_user.id, 'Вечер в хату')
      jail(message)
   elif x == 'Сбежать':
      wanted = True
      bot.send_message(message.from_user.id, 'Побег дело святое, но теперь ты в розыске')

def jail(message):

   jail_question(random.randint(1,10))
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(quest_answer_1, quest_answer_2, quest_answer_3, 'Быкануть')
   msg = bot.send_message(message.from_user.id, quest_text, reply_markup=keyboard)
   bot.register_next_step_handler(msg, jail_check)

def jail_question(x):
   global quest_text
   global quest_answer_1
   global quest_answer_2
   global quest_answer_3

   if x == 1:
      quest_text = 'Вилкой в глаз или в жопу дашь?'
      quest_answer_1 = 'Вилку в глаз'
      quest_answer_2 = 'В жопу дам'
      quest_answer_3 = 'Приму жопой вилку'
   elif x > 1:
      quest_text = 'Тебе под ноги кинули полотенце, твои действия?'
      quest_answer_1 = 'Вытру ноги'
      quest_answer_2 = 'Подниму'
      quest_answer_3 = 'Отсосу'

def jail_check(message):
   global jail_respect
   global jail_disrespect
   global jail_simpaty

   x = message.text
   if x == quest_answer_1:
      jail_respect += 20
      print('+20 респекта')

   elif x == quest_answer_2:
      jail_disrespect += 20
      print('+20 дизреспекта')

   elif x == quest_answer_3:
      jail_simpaty += 20
      print('+20 симпатии')

   elif x == 'Быкануть':
      jail_disrespect += 100

   judgment(message)
   
def judgment(message):
   global char_immunity

   if jail_respect >= 100:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add('Фарту масти')
      msg = bot.send_message(message.from_user.id, text = 'Твой срок окончен! Зеки подарили тебе самоделку из хлеба', reply_markup=keyboard)
      bot.register_next_step_handler(msg, shop_choice)
      
   elif jail_disrespect >= 100:
      boss_stats('Гомогомозеки')
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add('Да')
      msg = bot.send_message(message.from_user.id, text = 'Ты че петух, совсем рамсы попутал?', reply_markup=keyboard)
      bot.register_next_step_handler(msg, boss_prelude)

   elif jail_simpaty >= 100:
      char_immunity = True
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add('В этом и был мой план')
      msg = bot.send_message(message.from_user.id, text = 'Зеки пробурили в тебе черную дыру! Она поглощает все недуги', reply_markup=keyboard)
      bot.register_next_step_handler(msg, boss_prelude)


   elif jail_respect < 100 and jail_disrespect < 100:
      jail(message)
   
   

def location(message):

   location_list = ['Хата Колбаса', 'Полазна', 'Город Богов', 'Бэд Трип', 'Молебка', 'Армия', 'Дрочильня', '25й этаж']
   location_name = random.choice(location_list)

   location_choice(location_name)

   bot.send_message(message.from_user.id, loc_icon + location_name + loc_icon + '\n' + location_dscr)
   if loc_effect_msg != False:
      bot.send_message(message.from_user.id, loc_effect_msg)

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add('ПОГНАЛИ')
   msg = bot.send_message(message.from_user.id, text = 'Твои статы:\n❤️ ' + str(char_health) + '\n⚔️ ' + str(char_damage) + '\n💥 ' + str(char_crit), reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_prelude)

def boss_prelude(message):
   global boss_health
   global boss_damage
   global obida_level
   global busted_level
   global char_health
   global char_damage
   global char_item
   global char_poison
   global char_bleeding
   global char_silence
   
   if boss_name == 'Палыч':
      char_silence = True
      bot.send_message(message.from_user.id, 'Палыч завалил твой ебалыч - скиллы и предметы не поюзать')
      start_fight(message)

   elif boss_name == 'Вив' and char_item == 'Травмат Володи':
      char_health -= 300
      char_bleeding = True
      char_item = 'Пусто'
      bot.send_message(message.from_user.id, 'Володя забрал свой травмат!\n' + char_icon + '-300❤️🩸')
      start_fight(message)

   elif boss_name == 'Рыжий':
      char_poison = True
      bot.send_message(message.from_user.id, char_icon + ' + 🦠')
      start_fight(message)

   elif boss_name == 'Следователь':
      drugs = 'Шига', 'Мадам', 'Почтовые марки'
      cross_check = [x for x in drugs if x in all_char_items]
      if char_damage > 500:
         char_damage //= 2
         bot.send_message(message.from_user.id, '👮‍♂️: Чет многовато у вас дамага, молодой человек\n' + char_icon + '-50%⚔️')
      if elex_count > 0 or len(cross_check) > 0:
         busted_level += 50
         bot.send_message(message.from_user.id, '👮‍♂️: Употребляли? Тогда быстрее вас упакуем\nСтепень упаковки +50%')
      start_fight(message)

   elif boss_name == 'Дрон':
      obida_level = 0
      obida_level += len(all_char_items) * 5
      bot.send_message(message.from_user.id, 'За каждый поход к братишкам\n🤬+5%')
      if 'Мясо Андрея' in all_char_items:
         obida_level += 10
         bot.send_message(message.from_user.id, 'А за то что ты ел мясо Андрея\n🤬+10%')
      start_fight(message)

   elif boss_name == 'Донер Кебаб':
      if 'Костюм Эверласт' in all_char_items:
         boss_health += boss_health * 10 // 100
         boss_damage += boss_health * 10 // 100
         bot.send_message(message.from_user.id, 'Донер спиздил твой костюм!\n+10%🖤\n+10%⚔️')
      elif '2.5-литровка Колы' == char_item:
         char_health -= 500
         boss_health -= 500
         bot.send_message(message.from_user.id, 'Открывая твою Колу, Донер захуярил и себя, и тебя, и обои!\n-500❤️\n-500🖤')
      start_fight(message)

   elif boss_name == 'Черный Стас' and char_name == 'Митя':
      boss_damage += elex_count * 200
      bot.send_message(message.from_user.id, 'Стас, по-справедливости, бахает столько же эликсиров, что и Митя')

   else: start_fight(message)

def start_fight(message):
   
   if busted_level >= 100:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add('Отсидеть', 'Сбежать')
      msg = bot.send_message(message.from_user.id, text = 'Воу воу парень, ты доигрался, милости прошу в автозак', reply_markup=keyboard)
      bot.register_next_step_handler(msg, police_check)

   else:
      boss_startskill(message)

      bot.send_message(message.from_user.id, versus_stats(char_name, boss_name))

      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add('Атака', char_skill_name, char_item)
      msg = bot.send_message(message.from_user.id, text = 'Ходи, друг', reply_markup=keyboard)
      bot.register_next_step_handler(msg, action_choice)

def action_choice(message):
   global char_item
   global char_cooldown

   if message.text == 'Атака':
      attack_turn(message)

   elif message.text == char_skill_name:
      if char_cooldown <= 0 and char_silence == False and char_stan_timer <= 0:
         char_cooldown = 0
         skill(char_name)
         bot.send_message(message.from_user.id, skill_description)
      elif char_stan_timer > 0:
         bot.send_message(message.from_user.id, 'Не прокатит бро, ты в стане')
      elif char_silence == True:
         bot.send_message(message.from_user.id, 'Сорян, но ты забанен')
      elif char_cooldown > 0:
         bot.send_message(message.from_user.id, 'Обломись, там перезарядка')
      victory_check(message)

   elif message.text == char_item:
      if char_item != 'Пусто' and char_silence == False and char_stan_timer <= 0:
         item_using(char_item)
         char_item = 'Пусто'
         bot.send_message(message.from_user.id, item_dscr)
      elif char_stan_timer > 0:
         bot.send_message(message.from_user.id, 'Не прокатит бро, ты в стане')
      elif char_item != 'Пусто' and char_silence == True:
         bot.send_message(message.from_user.id, 'Сорян, но ты забанен')
      elif char_item == 'Пусто':
         bot.send_message(message.from_user.id, 'Ты че слепой? Нет у тебя расходников')   
      victory_check(message)

def attack_turn(message):
   global boss_health
   global char_cooldown
   global char_stan_timer
   global char_health
   global boss_stan_timer
   global obida_level
   global blazer_level
   global busted_level

   char_cooldown -= 1

   if chance(boss_miss) == True:
      b_m_indent = ' ' * 9 + str(boss_miss) + '%'
      if boss_name == 'Мел':
         blazer_level += 1
         bot.send_message(message.from_user.id, 'Мелу похуй на твой урон\n')
         bot.send_message(message.from_user.id, '🛡Уворотка🛡\n' + b_m_indent)
      else:
         bot.send_message(message.from_user.id, 'Босс пропустил твой урон\n')
         bot.send_message(message.from_user.id, '🛡Уворотка🛡\n' + b_m_indent)

      
   elif stas_passive(30) == True:
      char_health -= char_damage
      bot.send_message(message.from_user.id, 'Стас отразил твою хуйню\n' + char_icon + '-' + str(char_damage) + '❤️')
      
   else:
      if char_stan_timer > 0:
         char_stan_timer -= 1
         bot.send_message(message.from_user.id, char_name + ' недееспособен\n        💤Стан💤')
      elif char_stan_timer <= 0:
         char_attack(message)
         vampire(message)
         boss_returnal(message)
      if boss_stan_timer > 0:
         boss_stan_timer -= 1
         bot.send_message(message.from_user.id, boss_name + ' недееспособен\n        💤Стан💤')
      elif boss_stan_timer <= 0:
         boss_attack(message)

   boss_endskill(message)
   bleeding(message)
   poison(message)
   regeneration(message)

   if boss_name == 'Дрон':
      obida_level += 5
   elif boss_name == 'Следователь':
      busted_level += 20

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add('Закончить ход')
   msg = bot.send_message(message.from_user.id, versus_stats(char_name, boss_name), reply_markup=keyboard)
   bot.register_next_step_handler(msg, victory_check)
      
def skill(x):
   global char_health
   global boss_health
   global char_damage
   global boss_damage
   global char_cooldown
   global skill_description
   global elex_count
   global char_stan_timer

   if x == 'Митя':
      char_health -= 100
      char_damage += 200
      char_cooldown = 1
      elex_count += 1
      skill_description = '-100❤️\n+200⚔️\n🕒1 ход'

   elif x == 'Саня':
      damage = random.randint(50, 500)
      boss_health -= damage
      char_cooldown = 3
      skill_description = boss_icon + '-' + str(damage) + '🖤\n🕒3 хода'

   elif x == 'Тошик':
      char_health += char_health * 20 // 100
      char_cooldown = 2
      skill_description = '+20%❤️\n🕒2 хода'

   elif x == 'Коля':
      hack_value = boss_damage * 50 // 100
      char_damage += hack_value
      boss_damage -= hack_value
      char_cooldown = 3
      skill_description = boss_icon + '-' + str(hack_value) + '⚔️\n' + char_icon + '+' + str(hack_value) + '⚔️\n🕒3 хода'

   elif x == 'Темыч':
      skill_check_temich = chance(31)
      if skill_check_temich == False:
         boss_health, char_health = char_health, boss_health
         char_cooldown = 1
         skill_description = '❤️🔄🖤\n🕒1 ход'
      elif skill_check_temich == True:
         char_stan_timer = 1
         skill_description = 'Ой ой, Темыч запутался в своей суете\n' + char_icon + '+💤'

def item_using(x):
   global char_health
   global char_damage
   global char_cooldown
   global char_poison
   global char_bleeding
   global char_regen
   global boss_health
   global boss_damage
   global boss_bleeding
   global boss_regen
   global boss_poison
   global boss_stan_timer
   global item_dscr

   if x == 'Жигули':
      if boss_name == 'Донер Кебаб':
         boss_health += 150
         item_dscr = 'Пизда твоему бухлу, Донер его выпил\n' + boss_icon + '+150🖤'
      else:
         char_health += 150
         item_dscr = 'Для истинных ценителей\n+100❤️'

   elif x == 'Сидр':
      if boss_name == 'Донер Кебаб':
         boss_health += 300
         item_dscr = 'Пизда твоему бухлу, Донер его выпил\n' + boss_icon + '+300🖤'
      else:
         char_health += 300
         item_dscr = 'Питерская эстетика\n+300❤️'

   elif x == 'Балабаха Багбира':
      if boss_name == 'Донер Кебаб':
         boss_health += 500
         item_dscr = 'Пизда твоему бухлу, Донер его выпил\n' + boss_icon + '+500🖤'
      else:
         char_health += 500
         item_dscr = 'Со вкусом молодости\n+500❤️'

   elif x == 'Святая минералочка':
      char_regen = 100
      item_dscr = 'Освежающий глоток придал тебе сил\n' + char_icon + ' + 💕'

   elif x == 'Лезвия бритвы':
      boss_health -= 150
      boss_bleeding = True
      item_dscr = 'Бросок в глаз! Враг травмирован\n' + boss_icon + '-150🖤🩸'

   elif x == 'Травмат Володи':
      boss_health -= 300
      boss_bleeding = True
      item_dscr = 'Документы должны быть всегда с собой\n' + boss_icon + '-300🖤🩸'

   elif x == '2.5-литровка Колы':
      boss_health -= 500
      item_dscr = 'Грозное оружие судного нового года\n' + boss_icon + '-500🖤'

   elif x == 'Потный носок':
      if boss_name == 'Донер Кебаб':
         boss_health += 50
         boss_regen = 100
         item_dscr = 'Не стоило травить Донера\n' + boss_icon + '+50🖤💕'
      else:
         boss_health -= 50
         boss_poison = True
         item_dscr = boss_name + ' поймал твой носок лицом\n' + boss_icon + '-50🖤🦠'

   elif x == 'Блевотный харчок':
      if boss_name == 'Донер Кебаб':
         boss_health += 200
         boss_regen = 100
         item_dscr = 'Не стоило травить Донера\n' + boss_icon + '+200🖤💕'
      else:
         boss_health -= 200
         boss_poison = True
         item_dscr = 'Пздц ты жесткий, нашел чем замастить врага\n' + boss_icon + '-200🖤🦠'

   elif x == 'Рампаг':
      if boss_name == 'Донер Кебаб':
         boss_health = 0
         item_dscr = 'Рампаг заходит сзади! Моментальная смерть для Донера!'
      else:
         boss_stan_timer = 1
         item_dscr = 'Удар Рампагом! Враг в отрубе\n👿 + 💤'

   elif x == 'Золотые Ролексы':
      char_cooldown = 0
      item_dscr = 'Дороговаты, зато кулдаун скилла сбросили'

   elif x == 'Вакцина':
      char_poison = False
      char_bleeding = False
      item_dscr = 'Лечит от всех твоих недугов\n❌🩸🦠❌'

   elif x == 'Шига':
      foods = 'Сочник со сгухой', 'Дубайский шаурмец', 'Мясо Андрея', '5 пицц'
      cross_check = [x for x in foods if x in all_char_items]
      if len(cross_check) == 0:
         char_health -= 200
         char_damage += 100
         item_dscr = 'Душисто залетела, но теперь ты голоден\n-200❤️\n+100⚔️'
      elif len(cross_check) > 0:
         char_health += 200
         char_damage += 100
         item_dscr = 'Душисто залетела, а еда спасла тебя от голода\n+200❤️\n+100⚔️'

   elif x == 'Мадам':
      boss_damage -= boss_damage * 50 // 100
      item_dscr = 'Мадам умиротворяет всех вокруг\n' + boss_icon + '-50%⚔️'

def boss_startskill(message):
   global boss_damage
   if boss_name == 'Следователь':
      bot.send_message(message.from_user.id, '⛓Степень упаковки ' + str(busted_level) + '%⛓')
   
   elif boss_name == 'Дрон':
      bot.send_message(message.from_user.id, '🤬Риск обиды ' + str(obida_level) + '%🤬')

def char_attack(message):
   global boss_health
   global char_attack_damage

   if chance(char_crit) == True:
      char_attack_damage = char_damage * 2
      boss_health -= char_attack_damage
      bot.send_message(message.from_user.id, '💥Критический урон!💥\n' + '👿-' + str(char_damage * 2) + '🖤')

   else:
      char_attack_damage = char_damage
      boss_health -= char_attack_damage
      bot.send_message(message.from_user.id, '👿-' + str(char_damage) + '🖤')

def boss_returnal(message):
   global char_health
   
   if boss_returnal_value > 0:
      returnal_damage = char_attack_damage * boss_returnal_value // 100
      char_health -= returnal_damage
      b_r_indent = ' ' * 10 + str(boss_returnal_value) + '%\n'
      bot.send_message(message.from_user.id, '🤕Обратка🤕\n' + b_r_indent + char_icon + '-' + str(returnal_damage) + '❤️')

def boss_attack(message):
   global char_health
   global char_damage

   if char_name == 'Митя' and boss_name == 'Инквизиция':
      char_health += char_health * 50 // 100
      bot.send_message(message.from_user.id, 'Вместо урона Митя в инквизиции становится сильнее, она не может причинить ему урон!\n+50%❤️')
   
   else:
      if chance(char_miss) == True:
         c_m_indent = ' ' * 9 + str(char_miss) + '%'
         bot.send_message(message.from_user.id, char_name + ' скользкий тип\n')
         bot.send_message(message.from_user.id, '🛡Уворотка🛡\n' + c_m_indent)

      elif chance(boss_crit) == True:
         char_health -= boss_damage * 2
         bot.send_message(message.from_user.id, '💥Критический урон!💥\n' + char_icon + '-' + str(boss_damage * 2) + '❤️')

      elif chance(boss_crit) == False:
         char_health -= boss_damage
         bot.send_message(message.from_user.id, char_icon + '-' + str(boss_damage) + '❤️')

def vampire(message):
   global char_health

   if char_vampire > 0:
      vampire_value = char_attack_damage * char_vampire // 100
      char_health += vampire_value
      v_indent = ' ' * 11 + str(char_vampire) + '%\n'
      bot.send_message(message.from_user.id, '🦇Вампирик🦇\n' + v_indent + char_icon + '+' + str(vampire_value) + '❤️')

def boss_endskill(message):  
   global boss_name
   global boss_health 
   global boss_damage
   global boss_crit
   global char_health 
   global char_damage 
   global char_poison
   global char_bleeding
   global char_stan_timer
   global obida_level
   global blazer_level
   global boss_resurrection

   if boss_name == 'Чайковский' and boss_resurrection == True and boss_health <= 200:
      boss_resurrection = False
      boss_health += 800
      bot.send_message(message.from_user.id, 'Брат! Не засыпай!\n' + boss_icon + '+800🖤')
   
   elif boss_name == 'Вив':
      boss_damage += 100
      bot.send_message(message.from_user.id, 'Бассы подъехали!\n' + boss_icon + '+100⚔️')

   elif boss_name == 'Котенок-тролль' and chance(boss_endskill_value) == True:
      kitty_choice = random.randint(0, 11)
      if kitty_choice > 5:
         char_stan_timer = 1
         bot.send_message(message.from_user.id, 'Мурлы-сна!\n' + char_icon + '+💤')
      elif kitty_choice <= 5:
         char_health -= 200
         char_bleeding = True
         bot.send_message(message.from_user.id, 'Зацепка когтями!\n' + char_icon + '-200❤️🩸')
   
   elif boss_name == 'Пьяный Леха':
      boss_health += boss_health * 50 // 100
      boss_damage += boss_damage * 50 // 100
      bot.send_message(message.from_user.id, 'Леха бухает! Остановите его!\n' + boss_icon + '+50%🖤 и +50%⚔️')

   elif boss_name == 'Доктор Леха' and chance(boss_endskill_value) == True:
      char_health -= 500
      char_bleeding = True
      bot.send_message(message.from_user.id, 'Джагернаааааут!\n' + char_icon + '-500❤️🩸')

   elif boss_name == 'Мел' and blazer_level >= 3:
      blazer_level = 0
      char_health -= 500
      bot.send_message(message.from_user.id, 'Мел залил тебе блазуху в ухо!\n' + char_icon + '-500❤️')

   elif boss_name == 'Дрон':
      if chance(obida_level) == True:
         char_health = -1000
         bot.send_message(message.from_user.id, '☠️Дрон затаил лютую обиду!☠️')

   elif boss_name == 'Валера Гладиатор':
      gadza_choice = random.randint(1, 6)
      if gadza_choice == 1:
         char_health -= 500
         bot.send_message(message.from_user.id, 'Твин-турбо гадза на минус уши\n' + char_icon + '-500❤️')
      elif gadza_choice == 2:
         boss_health += 500
         bot.send_message(message.from_user.id, 'Церковная целебная гадза\n' + boss_icon + '+500🖤')
      elif gadza_choice == 3:
         boss_crit += 25
         bot.send_message(message.from_user.id, 'Кошачья критическая гадза\n' + boss_icon + '+25%💥')
      elif gadza_choice == 4:
         char_damage -= 250
         bot.send_message(message.from_user.id, 'Эльфийская гадза с эффектом попускания\n' + char_icon + '-250⚔️')
      elif gadza_choice == 5:
         char_poison = True
         bot.send_message(message.from_user.id, 'Ядовитая гадза по-киевски\n' + char_icon + '+🦠')

   elif boss_name == 'Великая Шива':
      if boss_crit < 100:
         boss_crit += 50
         bot.send_message(message.from_user.id, 'Криты завезли!\n' + boss_icon + '+20%💥')
      elif boss_crit == 100:
         boss_damage += boss_damage * 2
         bot.send_message(message.from_user.id, 'Урон завезли!\n' + boss_icon + '+100%⚔️')

def victory_check(message):

   if boss_health > 0 and char_health > 0:
      start_fight(message)

   elif boss_health <= 0 and char_health > 0 and boss_name == 'Король Макар':
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add('ДАВАЙ ЕЩЕ РАЗОК')
      msg = bot.send_message(message.from_user.id, text = '🥳🥳Похоже ты победил. Круто🥳🥳', reply_markup=keyboard)
      bot.register_next_step_handler(msg, get_character)

   elif boss_health <= 0 and char_health > 0 and boss_name != 'Король Макар':
      next_fight(message)

   elif char_health <= 0: 
      bot.send_message(message.from_user.id, '👻Увы, но ты проебал, старина👻\nНапиши мне что-нибудь и начнем сначала')

def next_fight(message):
   global win_rate
   global char_health
   global char_damage
   global char_crit
   global char_cooldown
   global char_poison
   global char_bleeding
   global char_silence
   global poison_damage
   global busted_level

   char_cooldown = 0
   win_rate += 1
   char_poison = False
   char_bleeding = False
   char_silence = False
   poison_damage = 5
   busted_level = 0

   if win_rate < 8 and boss_name == 'Саша Шлякин':
      char_health += char_health * 20 // 100
      char_damage += char_damage * 20 // 100
      char_crit += 5
      bot.send_message(message.from_user.id, 'Победа над собой возвысила тебя!\n+20%❤️\n+20%⚔️\n+5%💥')

   elif win_rate < 8 and char_name == 'Тошик':
      char_damage += char_health * 5 // 100
      bot.send_message(message.from_user.id, 'Твое здоровье - твоя сила\n⚔️+5%❤️')

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add('Я молодец')
   msg = bot.send_message(message.from_user.id, text = 'Ты победил, слабина', reply_markup=keyboard)
   bot.register_next_step_handler(msg, shop_choice)

bot.polling(none_stop=True, interval=0)