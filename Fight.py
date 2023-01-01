import Characters
import random
import MyStrings
import BotMessages

class Attack_messages():
   # вспомогательный класс для создания списка возникающих сообщений в цикле атаки
   miss_message = False
   mel_miss_message = False
   boss_miss_message = False
   black_stas_returnal_message = False
   stan_message = False
   char_attack_message = False
   lifesteal_message = False
   returnal_message = False
   mitya_inkvisizia_message = False
   boss_attack_message = False
   boss_ressurection_message = False
   boss_end_skill_message = False
   bleeding_message = False
   regeneration_message = False
   char_miss_message = False
   poison_message = False
   def list_generator():
      attack_message_list = [Attack_messages.miss_message, Attack_messages.mel_miss_message, Attack_messages.boss_miss_message, 
                              Attack_messages.black_stas_returnal_message, Attack_messages.stan_message, Attack_messages.char_attack_message,
                              Attack_messages.lifesteal_message, Attack_messages.returnal_message, Attack_messages.mitya_inkvisizia_message,
                              Attack_messages.boss_attack_message, Attack_messages.boss_ressurection_message, Attack_messages.boss_end_skill_message,
                              Attack_messages.bleeding_message, Attack_messages.regeneration_message, Attack_messages.char_miss_message,
                              Attack_messages.poison_message]
      return attack_message_list

def chance(x):
   # генератор вероятности
   chance = random.randint(1, 100) in range(1, x)
   return chance

def attack():
   # снижение перезарядки способности игрока
   Characters.char.cooldown -= 1

   # проверка на уворот босса
   if chance(Characters.boss.miss_chance) == True:
      # сообщение с процентом шанса уворота
      Attack_messages.miss_message = MyStrings.Text.miss_text.value + BotMessages.Message_text.miss_message(Characters.boss.miss_chance)
      # особое сообщения уворота Мела
      if Characters.boss.name == MyStrings.Text.mel_name.value:
         Characters.boss.mel_blazer_level += 1
         Attack_messages.mel_miss_message = MyStrings.Text.mel_miss_text.value
      # сообщение об увороте босса   
      else:
         Attack_messages.boss_miss_message = MyStrings.Text.boss_miss_text.value

   # проверка на пассивный навык Черного Стаса, вывод сообщения если да
   elif chance(30) == True and Characters.boss.name == MyStrings.Text.black_stas_name.value:
      Characters.char.health_down(Characters.char.damage)
      Attack_messages.black_stas_returnal_message = BotMessages.Message_text.black_stas_returnal_message()
      
   # если босс не увернулся
   else:
      # если игрок оглушен
      if Characters.char.stan_timer > 0:
         Characters.char.stan_timer -= 1
         Attack_messages.stan_message = BotMessages.Message_text.stan_effect_message(Characters.char.name)
      # если игрок не оглушен
      elif Characters.char.stan_timer <= 0:
         attack_turn()
         lifesteal()
         boss_returnal()
      # если босс оглушен
      if Characters.boss.stan_timer > 0:
         Characters.boss.stan_timer -= 1
         Attack_messages.stan_message = BotMessages.Message_text.stan_effect_message(Characters.boss.name)
      # если босс не оглушен
      elif Characters.boss.stan_timer <= 0:
         boss_attack()

   boss_end_skill_activation()
   bleeding()
   poison()
   regeneration()
   boss_charge_skill_up()

def attack_turn():
   global char_attack_damage
   # проверка критической атаки для вывода нужного сообщения и ее применение
   char_attack_damage = Characters.char.damage
   if chance(Characters.char.critical_chance) == True:
      Characters.boss.health_down(char_attack_damage * 2)
      Attack_messages.char_attack_message = BotMessages.Message_text.char_critical_attack_message()
   else:
      Characters.boss.health_down(char_attack_damage)
      Attack_messages.char_attack_message = BotMessages.Message_text.char_attack_message()
   
def lifesteal():
   # проверка на вампиризм, применение и вывод сообщения
   if Characters.char.lifesteal > 0:
      Characters.char.health_up(char_attack_damage * Characters.char.lifesteal // 100)
      Attack_messages.lifesteal_message = BotMessages.Message_text.lifesteal_message()

def boss_returnal():
   # проверка на обратку босса, применение и вывод сообщения 
   if Characters.boss.returnal_value > 0:
      Characters.char.health_down(char_attack_damage * Characters.boss.returnal_value // 100)
      Attack_messages.returnal_message = BotMessages.Message_text.returnal_message()

def boss_attack():
   global boss_attack_damage
   # проверка является ли игрок Митей, а босс Инквизицией для особоых условий боя + вывод сообщения
   if Characters.char.name == MyStrings.Text.mitya_name.value and Characters.boss.name == MyStrings.Text.inkvisizia_name.value:
      Characters.char.health_up_procent(50)
      Attack_messages.mitya_inkvisizia_message = MyStrings.Text.mitya_inkvisizia_text.value
   
   else:
      # проверка на уворот игрока с выводом сообщения
      if chance(Characters.char.miss_chance) == True:
         Attack_messages.char_miss_message = Characters.char.name + BotMessages.Message_text.miss_message(Characters.char.miss_chance)
      # критическая атака босса с выводом сообщения
      elif chance(Characters.boss.critical_chance) == True:
         boss_attack_damage = Characters.boss.damage * 2
         Characters.char.health_down(boss_attack_damage)
         Attack_messages.boss_attack_message = BotMessages.Message_text.boss_critical_attack_message()
      # обычная атака босса с выводом сообщения
      elif chance(Characters.boss.critical_chance) == False:
         boss_attack_damage = Characters.boss.damage
         Characters.char.health_down(boss_attack_damage)
         Attack_messages.boss_attack_message = BotMessages.Message_text.boss_attack_message()
      
def boss_end_skill_activation():  
   # проверка на уровень здоровья и статус воскрешения босса, применение воскрешения с выводом сообщения
   if Characters.boss.resurrection == True and Characters.boss.health <= 200:
      Characters.boss.resurrection = False
      Characters.boss.health_up(800)
      # особое сообщение если босс Чайковский
      if Characters.boss.name == MyStrings.Text.chaikovskii_name.value:
         Attack_messages.boss_ressurection_message = BotMessages.Message_text.chaikovskii_ressurection_message()
      # обычное сообщение воскрешения
      else:
         Attack_messages.boss_ressurection_message = BotMessages.Message_text.boss_ressurection_message()
      
   # применение завершающей способности Вива, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.viv_name.value:
      Characters.boss.damage_up(Characters.boss.viv_damage_up_skill_value)
      Attack_messages.boss_end_skill_message = BotMessages.Message_text.viv_end_skill_message()

   # применение завершающей рандомной способности Котенка, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.kitty_name.value and chance(Characters.boss.end_skill_chance) == True:
      kitty_skill_choice = random.randint(0, 11)
      # оглушение на игрока
      if kitty_skill_choice > 5:
         Characters.char.stan_timer = 1
         Attack_messages.boss_end_skill_message = BotMessages.Message_text.kitty_stan_message()
      # кровотечение на игрока
      elif kitty_skill_choice <= 5:
         Characters.char.health_down(Characters.boss.kity_end_skill_damage)
         Characters.char.bleeding = True
         Attack_messages.boss_end_skill_message = BotMessages.Message_text.kitty_bleeding_message()
   
   # применение завершающей способности Пьяного Лехи, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.drunk_leha_name.value:
      Characters.boss.health_up_procent(Characters.boss.drunk_leha_boost_skill_value)
      Characters.boss.damage_up_procent(Characters.boss.drunk_leha_boost_skill_value)
      Attack_messages.boss_end_skill_message = BotMessages.Message_text.drunk_leha_boost_message()
      
   # применение завершающей способности Доктора Лехи, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.doc_leha_name.value and chance(Characters.boss.end_skill_chance) == True:
      Characters.char.health_down(Characters.boss.doc_leha_end_skill_damage)
      Characters.char.bleeding = True
      Attack_messages.boss_end_skill_message = BotMessages.Message_text.doc_leha_bleeding_message()
      
   # применение завершающей способности Мела, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.mel_name.value and Characters.boss.mel_blazer_level >= 3:
      Characters.boss.mel_blazer_level = 0
      Characters.char.health_down(Characters.boss.mel_end_skill_damage)
      Attack_messages.boss_end_skill_message = BotMessages.Message_text.mel_end_skill_message()
      
   # применение завершающей способности Дрона, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.dron_name.value:
      if chance(Characters.boss.dron_obida_level) == True:
         Characters.char.health_down(Characters.boss.dron_end_skill_damage)
         Attack_messages.boss_end_skill_message = BotMessages.Message_text.dron_end_skill_message()
         
   # применение одной из рандомных завершающих способностей Валеры, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.glad_name.value:
      glad_skill_choice = random.randint(1, 6)
      # нанесение урона игроку
      if glad_skill_choice == 1:
         Characters.char.health_down(Characters.boss.glad_end_skill_damage)
         Attack_messages.boss_end_skill_message = BotMessages.Message_text.glad_damage_skill_message()
      # увеличение здоровье Валеры
      elif glad_skill_choice == 2:
         Characters.boss.health_up(Characters.boss.glad_health_up_skill_value)
         Attack_messages.boss_end_skill_message = BotMessages.Message_text.glad_health_up_skill_message()
      # увеличение шанса критической атаки Валеры
      elif glad_skill_choice == 3:
         Characters.boss.critical_chance_up(Characters.boss.glad_critical_up_skill_value)
         Attack_messages.boss_end_skill_message = BotMessages.Message_text.glad_critical_up_skill_message()
      # уменьшение урона игрока
      elif glad_skill_choice == 4:
         Characters.char.damage_down(Characters.boss.glad_damage_down_skill_value)
         Attack_messages.boss_end_skill_message = BotMessages.Message_text.glad_damage_down_skill_message()
      # наложение яда на игрока
      elif glad_skill_choice == 5:
         Characters.char.poison = True
         Attack_messages.boss_end_skill_message = BotMessages.Message_text.glad_poison_skill_message()

   # применение завершающей способности Шивы, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.shiva_name.value:
      # увеличение шанса критической атаки Шивы
      if Characters.boss.critical_chance < 100:
         Characters.boss.critical_chance_up(Characters.boss.shiva_critical_up_skill_value)
         Attack_messages.boss_end_skill_message = BotMessages.Message_text.shiva_critical_skill_message()
      # увеличение атаки Шивы, если шанс критической атаки заполнен до максимума
      elif Characters.boss.critical_chance >= 100:
         Characters.boss.damage_up_procent(Characters.boss.shiva_damage_up_skill_value)
         Attack_messages.boss_end_skill_message = BotMessages.Message_text.shiva_damage_up_skill_message()    

def bleeding():
   # проверка игрока на кровотечение и отсутствие иммунитета к нему, применение кровотечения, вывод сообщения
   if Characters.char.bleeding == True and Characters.char.immunity == False:
      Characters.char.health_down(Characters.Pers.bleeding_damage)
      Attack_messages.bleeding_message = BotMessages.Message_text.bleeding_message(Characters.char.icon, MyStrings.Text.char_health_icon.value)
      
   # проверка босса на кровотечение, его применение и вывод сообщения
   if Characters.boss.bleeding == True:
      Characters.boss.health_down(Characters.Pers.bleeding_damage)
      Attack_messages.bleeding_message = BotMessages.Message_text.bleeding_message(Characters.boss.icon, MyStrings.Text.boss_health_icon.value)

def poison():
   # проверка игрока на отравление и отсутствие иммунитета к нему, применение, вывод сообщения
   if Characters.char.poison == True and Characters.char.immunity == False:
      Characters.char.health_down_procent(Characters.Pers.poison_damage)
      Attack_messages.poison_message = BotMessages.Message_text.poison_message(Characters.char.icon, MyStrings.Text.char_health_icon.value)

   # проверка босса на отравление, применение, вывод сообщения
   if Characters.boss.poison == True:
      Characters.boss.health_down_procent(Characters.Pers.poison_damage)
      Attack_messages.poison_message = BotMessages.Message_text.poison_message(Characters.boss.icon, MyStrings.Text.boss_health_icon.value) 

   # увеличение на 10% урона отравления на время боя
   Characters.Pers.poison_damage += 10

def regeneration():
   # проверка игрока на регенерацию, применение, вывод сообщения
   if Characters.char.regeneration > 0:
      Characters.char.health_up(Characters.Pers.regeneration_value)
      Attack_messages.regeneration_message = BotMessages.Message_text.regeneration_message(Characters.char.icon, MyStrings.Text.char_health_icon.value)

   # проверка босса на регенерацию, применение, вывод сообщения   
   if Characters.boss.regeneration > 0:
      Characters.boss.health_up(Characters.Pers.regeneration_value)
      Attack_messages.regeneration_message = BotMessages.Message_text.regeneration_message(Characters.boss.icon, MyStrings.Text.boss_health_icon.value)

def boss_charge_skill_up():
   # увеличение шкалы накопительной способности босса
   if Characters.boss.name == MyStrings.Text.dron_name.value:
      Characters.boss.dron_obida_level += 5

   elif Characters.boss.name == MyStrings.Text.sledovatel_name.value:
      Characters.char.busted_level += 20      