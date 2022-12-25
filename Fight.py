import Characters
import random
import MyStrings
import BotMessages

def chance(x):
   # генератор вероятности
   chance = random.randint(1, 100) in range(1, x)
   return chance

def char_attack():
   # используемые переменные
   miss_message = False
   mel_miss_message = False
   boss_miss_message = False
   black_stas_returnal_message = False

   # снижение кулдауна игрока
   Characters.char.cooldown -= 1

   # проверка на уворот босса
   if chance(Characters.boss.miss_chance) == True:
      # сообщение с процентом шанса уворота
      miss_message = MyStrings.Text.miss_text.value + BotMessages.Message_text.miss_text_indent(Characters.boss.miss_chance)
      # особое сообщения уворота Мела
      if Characters.boss.name == MyStrings.Text.mel_name.value:
         Characters.boss.blazer_level += 1
         mel_miss_message = MyStrings.Text.mel_miss_text.value
      # сообщение об увороте босса   
      else:
         boss_miss_message = MyStrings.Text.boss_miss_text.value

   # проверка на пассивный навык Черного Стаса, вывод сообщения если да
   elif chance(30) == True and Characters.boss.name == MyStrings.Text.black_stas_name.value:
      Characters.char.health_down(Characters.char.damage)
      black_stas_returnal_message = BotMessages.Message_text.black_stas_returnal_message()
      
   # если босс не увернулся
   else:
      # проверка на оглушенность игрока
      if Characters.char.stan_timer > 0:
         Characters.char.stan_timer -= 1
         BotMessages.Message_text.stan_effect_message(Characters.char.name)
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