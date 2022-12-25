import Characters
import random
import MyStrings
import BotMessages

def chance(x):
   # генератор вероятности
   chance = random.randint(1, 100) in range(1, x)
   return chance

def attack():
   # используемые переменные
   miss_message = False
   mel_miss_message = False
   boss_miss_message = False
   black_stas_returnal_message = False
   stan_message = False
   attack_message = False
   lifesteal_message = False
   returnal_message = False
   mitya_inkvisizia_message = False
   boss_attack_message = False

   # снижение кулдауна игрока
   Characters.char.cooldown -= 1

   # проверка на уворот босса
   if chance(Characters.boss.miss_chance) == True:
      # сообщение с процентом шанса уворота
      miss_message = MyStrings.Text.miss_text.value + BotMessages.Message_text.miss_message(Characters.boss.miss_chance)
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
      # если игрок оглушен
      if Characters.char.stan_timer > 0:
         Characters.char.stan_timer -= 1
         stan_message = BotMessages.Message_text.stan_effect_message(Characters.char.name)
      # если игрок не оглушен
      elif Characters.char.stan_timer <= 0:
         attack_turn()
         lifesteal()
         boss_returnal()
      # если босс оглушен
      if Characters.boss.stan_timer > 0:
         Characters.boss.stan_timer -= 1
         stan_message = BotMessages.Message_text.stan_effect_message(Characters.boss.name)
      # если босс не оглушен
      elif Characters.boss.stan_timer <= 0:
         boss_attack()

   boss_endskill(message)
   bleeding(message)
   poison(message)
   regeneration(message)

   # применение способностей босса в конце раунда
   if Characters.boss.name == MyStrings.Text.dron_name.value:
      Characters.boss.obida_level += 5
   elif Characters.boss.name == MyStrings.Text.sledovatel_name.value:
      Characters.char.busted_level += 20

   keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
   keyboard.add(MyStrings.Text.end_turn_button_text.value)
   msg = bot.send_message(message.from_user.id, versus_stats(char.name, boss.name), reply_markup=keyboard)
   bot.register_next_step_handler(msg, victory_check)

def attack_turn():
   global char_attack_damage
   # проверка критической атаки для вывода нужного сообщения и ее применение
   char_attack_damage = Characters.char.damage
   if chance(Characters.char.critical_chance) == True:
      Characters.boss.health_down(char_attack_damage * 2)
      attack_message = BotMessages.Message_text.char_critical_attack_message()
   else:
      Characters.boss.health_down(char_attack_damage)
      attack_message = BotMessages.Message_text.char_attack_message()
   
def lifesteal():
   # проверка на вампиризм, применение и вывод сообщения
   if Characters.char.lifesteal > 0:
      Characters.char.health_up(char_attack_damage * Characters.char.lifesteal // 100)
      lifesteal_message = BotMessages.Message_text.lifesteal_message()

def boss_returnal():
   # проверка на обратку босса, применение и вывод сообщения 
   if Characters.boss.returnal_value > 0:
      Characters.char.health_down(char_attack_damage * Characters.boss.returnal_value // 100)
      returnal_message = BotMessages.Message_text.returnal_message()

def boss_attack():
   global boss_attack_damage
   # проверка является ли игрок Митей, а босс Инквизицией для особоых условий боя + вывод сообщения
   if Characters.char.name == MyStrings.Text.mitya_name.value and Characters.boss.name == MyStrings.Text.inkvisizia_name.value:
      Characters.char.health_up_procent(50)
      mitya_inkvisizia_message = MyStrings.Text.mitya_inkvisizia_text.value
   
   else:
      # проверка на уворот игрока с выводом сообщения
      if chance(Characters.char.miss_chance) == True:
         char_miss_message = Characters.char.name + BotMessages.Message_text.miss_message(Characters.char.miss_chance)
      # критическая атака босса с выводом сообщения
      elif chance(Characters.boss.critical_chance) == True:
         boss_attack_damage = Characters.boss.damage * 2
         Characters.char.health_down(boss_attack_damage)
         boss_attack_message = BotMessages.Message_text.boss_critical_attack_message()
      # обычная атака босса с выводом сообщения
      elif chance(Characters.boss.critical_chance) == False:
         boss_attack_damage = Characters.boss.damage
         Characters.char.health_down(boss_attack_damage)
         boss_attack_message = BotMessages.Message_text.boss_attack_message()
      
      
      