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
   boss_ressurection_message = False
   boss_end_skill_message = False

   # снижение кулдауна игрока
   Characters.char.cooldown -= 1

   # проверка на уворот босса
   if chance(Characters.boss.miss_chance) == True:
      # сообщение с процентом шанса уворота
      miss_message = MyStrings.Text.miss_text.value + BotMessages.Message_text.miss_message(Characters.boss.miss_chance)
      # особое сообщения уворота Мела
      if Characters.boss.name == MyStrings.Text.mel_name.value:
         Characters.boss.mel_blazer_level += 1
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

   boss_end_skill_activation()
   bleeding(message)
   poison(message)
   regeneration(message)

   # применение способностей босса в конце раунда
   if Characters.boss.name == MyStrings.Text.dron_name.value:
      Characters.boss.dron_obida_level += 5
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
      
def boss_end_skill_activation():  
   global boss_ressurection_message
   global boss_end_skill_message

   # проверка на уровень здоровья и статус воскрешения босса, применение воскрешения с выводом сообщения
   if Characters.boss.resurrection == True and Characters.boss.health <= 200:
      Characters.boss.resurrection = False
      Characters.boss.health_up(800)
      # особое сообщение если босс Чайковский
      if Characters.boss.name == MyStrings.Text.chaikovskii_name.value:
         boss_ressurection_message = BotMessages.Message_text.chaikovskii_ressurection_message()
      # обычное сообщение воскрешения
      else:
         boss_ressurection_message = BotMessages.Message_text.boss_ressurection_message()
      
   # применение завершающей способности Вива, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.viv_name.value:
      Characters.boss.damage_up(Characters.boss.viv_damage_up_skill_value)
      boss_end_skill_message = BotMessages.Message_text.viv_end_skill_message()

   # применение завершающей рандомной способности Котенка, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.kitty_name.value and chance(Characters.boss.end_skill_chance) == True:
      kitty_skill_choice = random.randint(0, 11)
      # оглушение на игрока
      if kitty_skill_choice > 5:
         Characters.char.stan_timer = 1
         boss_end_skill_message = BotMessages.Message_text.kitty_stan_message()
      # кровотечение на игрока
      elif kitty_skill_choice <= 5:
         Characters.char.health_down(Characters.boss.kity_end_skill_damage)
         Characters.char.bleeding = True
         boss_end_skill_message = BotMessages.Message_text.kitty_bleeding_message()
   
   # применение завершающей способности Пьяного Лехи, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.drunk_leha_name.value:
      Characters.boss.health_up_procent(Characters.boss.drunk_leha_boost_skill_value)
      Characters.boss.damage_up_procent(Characters.boss.drunk_leha_boost_skill_value)
      boss_end_skill_message = BotMessages.Message_text.drunk_leha_boost_message()
      
   # применение завершающей способности Доктора Лехи, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.doc_leha_name.value and chance(Characters.boss.end_skill_chance) == True:
      Characters.char.health_down(Characters.boss.doc_leha_end_skill_damage)
      Characters.char.bleeding = True
      boss_end_skill_message = BotMessages.Message_text.doc_leha_bleeding_message()
      
   # применение завершающей способности Мела, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.mel_name.value and Characters.boss.mel_blazer_level >= 3:
      Characters.boss.mel_blazer_level = 0
      Characters.char.health_down(Characters.boss.mel_end_skill_damage)
      boss_end_skill_message = BotMessages.Message_text.mel_end_skill_message()
      
   # применение завершающей способности Дрона, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.dron_name.value:
      if chance(Characters.boss.dron_obida_level) == True:
         Characters.char.health_down(Characters.boss.dron_end_skill_damage)
         boss_end_skill_message = BotMessages.Message_text.dron_end_skill_message()
         
   # применение одной из рандомных завершающих способностей Валеры, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.glad_name.value:
      glad_skill_choice = random.randint(1, 6)
      # нанесение урона игроку
      if glad_skill_choice == 1:
         Characters.char.health_down(Characters.boss.glad_end_skill_damage)
         boss_end_skill_message = BotMessages.Message_text.glad_damage_skill_message()
      # увеличение здоровье Валеры
      elif glad_skill_choice == 2:
         Characters.boss.health_up(Characters.boss.glad_health_up_skill_value)
         boss_end_skill_message = BotMessages.Message_text.glad_health_up_skill_message()
      # увеличение шанса критической атаки Валеры
      elif glad_skill_choice == 3:
         Characters.boss.critical_chance_up(Characters.boss.glad_critical_up_skill_value)
         boss_end_skill_message = BotMessages.Message_text.glad_critical_up_skill_message()
      # уменьшение урона игрока
      elif glad_skill_choice == 4:
         Characters.char.damage_down(Characters.boss.glad_damage_down_skill_value)
         boss_end_skill_message = BotMessages.Message_text.glad_damage_down_skill_message()
      # наложение яда на игрока
      elif glad_skill_choice == 5:
         Characters.char.poison = True
         boss_end_skill_message = BotMessages.Message_text.glad_poison_skill_message()

   # применение завершающей способности Шивы, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.shiva_name.value:
      # увеличение шанса критической атаки Шивы
      if Characters.boss.critical_chance < 100:
         Characters.boss.critical_chance_up(Characters.boss.shiva_critical_up_skill_value)
         boss_end_skill_message = BotMessages.Message_text.shiva_critical_skill_message()
      # увеличение атаки Шивы, если шанс критической атаки заполнен до максимума
      elif Characters.boss.critical_chance >= 100:
         Characters.boss.damage_up_procent(Characters.boss.shiva_damage_up_skill_value)
         boss_end_skill_message = BotMessages.Message_text.shiva_damage_up_skill_message()    
      