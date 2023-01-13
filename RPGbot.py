# -*- coding: utf-8 -*-

from telebot import TeleBot
from telebot import types
import random
import Characters
import Drop
import Locations
import GameStrings
import PlayerStrings
import DropStrings
import StatsStrings
import BossStrings
import BotMessages
import FightProcess
import FightFunctions
import CharactersGenerator
import ItemsGenerator
import BuffsGenerator
bot = TeleBot('2102427745:AAECFy-T6GfMWH1VNshsucAEXZEfzmGUZBk')

@bot.message_handler(content_types=['text'])


def choose_hero(message):
   # приветственное сообщение
   bot.send_message(message.from_user.id, GameStrings.Text.hello)
   
   # клавиатура с именами героев
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(PlayerStrings.Mitya.name, PlayerStrings.Sanya.name, PlayerStrings.Toshik.name,
                PlayerStrings.Kolya.name, PlayerStrings.Temich.name)

   # сообщение с запросом на героя, переход к созданию игрока
   msg = bot.send_message(message.from_user.id, text = GameStrings.Text.choose_hero, 
                           reply_markup=keyboard)
   bot.register_next_step_handler(msg, player_creation)


def player_creation(message):
   # назначение характеристик выбранному герою
   CharactersGenerator.player_get_stats(message.text)

   # сообщение с характеристиками героя
   bot.send_message(message.from_user.id, PlayerStrings.Text.hero_description)

   # клавиатура с подтверждением героя или его заменой
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(GameStrings.ButtonText.ready, GameStrings.ButtonText.another_hero)

   # сообщение с потдверждением героя или его заменой, переход к выбору магазина
   msg = bot.send_message(message.from_user.id, text = GameStrings.Text.hero_confirmed_question, 
                           reply_markup=keyboard)
   bot.register_next_step_handler(msg, shop_choice)


def shop_choice(message):
   # перезапуск если герой не подтвержден игроком
   if message.text == GameStrings.ButtonText.another_hero:
      bot.send_message(message.from_user.id, GameStrings.Text.user_input)
      bot.register_next_step_handler(message, choose_hero)
   
   # клавиатура с именами магазинов при подтверждении героя или победе в бою
   elif message.text == GameStrings.ButtonText.ready or GameStrings.ButtonText.victory:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(GameStrings.Text.stas_shop_name, GameStrings.Text.bratishki_shop_name)

      # сообщение с выбором магазина, переход к выбранному магазину
      msg = bot.send_message(message.from_user.id, text = GameStrings.Text.shop_choice, 
                              reply_markup=keyboard)
      bot.register_next_step_handler(msg, shop)


def shop(message):
   # применение свойств магазина при входе игрока
   Drop.shop_enter(message.text)

   # если игрок пошел в Лавку Серого Стаса
   if message.text == GameStrings.ButtonText.stas_shop_name:

      # реплика Стаса с приветствием
      bot.send_message(message.from_user.id, DropStrings.Items.stas_hello())

      # клавиатура с тремя рандомными итемами 
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(Drop.item_choice[0], Drop.item_choice[1], Drop.item_choice[2])

      # реплика Стаса перед выбором итемов, переход к обновлению слота итема игрока
      msg = bot.send_message(message.from_user.id, text = DropStrings.Items.stas_item_offer, 
                              reply_markup=keyboard)
      bot.register_next_step_handler(msg, items_upgrade)

   # если игрок пошел в Братишкино логово
   elif message.text == GameStrings.ButtonText.bratishki_shop_name:

      # реплика Братишек с приветствием 
      bot.send_message(message.from_user.id, DropStrings.Buffs.bratishki_hello())

      # клавиатура с тремя рандомными баффами
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(Drop.buff_choice[0], Drop.buff_choice[1], Drop.buff_choice[2])

      # реплика Братишек перед выбором баффов, переход к применению их свойств на игрока 
      msg = bot.send_message(message.from_user.id, text = DropStrings.Buffs.bratishki_buff_offer,
                               reply_markup=keyboard)
      bot.register_next_step_handler(msg, stats_upgrade)


def items_upgrade(message):
   # обновление слота предмета игрока если он пошел к Стасу
   ItemsGenerator.stas_enter(message.text)
   
   # клавитура с запросом на подбор босса
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(GameStrings.Text.boss_choice_question)

   # реплика Стаса с прощанием, переход к подбору босса
   msg = bot.send_message(message.from_user.id, text = DropStrings.Items.stas_bye,
                           reply_markup=keyboard)
   bot.register_next_step_handler(msg, boss_choice)


def stats_upgrade(message):
   # обновление характеристик игрока если он пошел к Братишкам
   BuffsGenerator.bratishki_enter(message.text)

   # сообщение с описанием выбранного баффа
   bot.send_message(message.from_user.id, BuffsGenerator.buff.description)

   # клавитура с выводом характеристик игрока и запросом босса
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(GameStrings.Text.boss_choice_question)

   # реплика Братишек с прощанием
   msg = bot.send_message(message.from_user.id, text = DropStrings.Buffs.bratishki_bye,
                           reply_markup=keyboard)

   # сообщение с характеристиками персонажа                           
   bot.send_message(message.from_user_id, StatsStrings.player_stats_message())

   # переход к подбору босса                           
   bot.register_next_step_handler(msg, boss_choice)

def boss_choice(message):
   # выбор босса в зависимости от количества побед в боях
   FightFunctions.boss_difficult_choice(Characters.Player.win_rate)

   # назначение характеристик боссу
   CharactersGenerator.boss_get_stats(FightFunctions.boss_name)

   # проверка в розыске ли игрок, приминение свйоств если да
   if CharactersGenerator.player.wanted_level == True:
      CharactersGenerator.boss.resurrection = True
      bot.send_message(message.from_user.id, MyStrings.Text.boss_police_upgrade_text.value)

   # проверка является ли игрок Сашей Шлякиным при битве с Сашей Шлякиным, с перезапуском если нет
   if CharactersGenerator.boss.name == BossStrings.Sasha.name and CharactersGenerator.player.name != PlayerStrings.Sanya.name:
      bot.send_message(message.from_user.id, BossStrings.Sasha.cancel_fight)
      boss_choice(message)

   # клавиатура с выводом характеристик босса и запросом локации
   else:
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(GameStrings.Text.location_choice_question)
      msg = bot.send_message(message.from_user.id, text = StatsStrings.boss_stats_message(), reply_markup=keyboard)
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
   msg = bot.send_message(message.from_user.id, text = BotMessages.Message_text.player_stats_message(), reply_markup=keyboard)
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
   bot.send_message(message.from_user.id, BotMessages.Message_text.versus_stats(Characters.player.name, Characters.boss.name))

   # клавиатура с выбором действий игрока
   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.attack_button_text.value, Characters.player.skill_name, Characters.player.item)
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
      msg = bot.send_message(message.from_user.id, BotMessages.Message_text.versus_stats(Characters.player.name, Characters.boss.name), reply_markup=keyboard)
      bot.register_next_step_handler(msg, victory_check)

   elif message.text == Characters.player.skill_name:
      # применение способности, если игрок нажал "Скилл"
      Fight.player_skill_use()

      # отсылка сообщения
      bot.send_message(message.from_user.id, Fight.Attack_messages.skill_use_message)

      # переход на проверку победы в бою
      victory_check(message)

   elif message.text == Characters.player.item:
      # применение предмета, если игрок нажал "Предмет"
      Fight.player_item_use()

      # отсылка сообщения 
      bot.send_message(message.from_user.id, Fight.Attack_messages.item_use_message)

      # особое сообщение, если предмет влияет на конкретного игрока
      if Drop.Item.player_iteraction_message != False:
         bot.send_message(message.from_user.id, Drop.Item.player_iteraction_message)
         Drop.Item.player_iteraction_message = False

      # особое сообщение, если предмет влияент на конкретного босса
      if Drop.Item.boss_iteraction_message != False:
         bot.send_message(message.from_user.id, Drop.Item.boss_iteraction_message)
         Drop.Item.boss_iteraction_message = False 

      # переход на проверку победы в бою
      victory_check(message)

def victory_check(message):
   # проверка на победу в конце раунда

   if Characters.boss.health > 0 and Characters.player.health > 0:
      # если и босс и игрок живы - переход к следующему раунду
      start_fight(message)

   elif Characters.boss.health <= 0 and Characters.player.health > 0 and Characters.boss.name == MyStrings.Text.makar_name.value:
      # если игрок победил финального босса Короля Макара - поздравительное сообщение, клавиатура с подтверждением перезапуска игры
      keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
      keyboard.add(MyStrings.Text.restart_button_text.value)
      msg = bot.send_message(message.from_user.id, text = MyStrings.Text.victory_game_text.value, reply_markup=keyboard)
      bot.register_next_step_handler(msg, choose_hero)

   elif Characters.boss.health <= 0 and Characters.player.health > 0 and Characters.boss.name != MyStrings.Text.makar_name.value:
      # если игрок победил обычного босса - переход на следующий уровень
      next_fight(message)

   elif Characters.player.health <= 0: 
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