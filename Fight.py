import Characters
import random
import MyStrings
import BotMessages
import Drop

class Attack_messages():
   # вспомогательный класс для создания списка возникающих сообщений во время боя
   skill_use_message = False
   item_use_message = False
   attack_messages_list = []
   sanya_win_sanya_message = False
   toshik_passive_skill_message = False

def chance(x):
   # генератор вероятности
   chance = random.randint(1, 100) in range(1, x)
   return chance

def attack():
   # снижение перезарядки способности игрока
   Characters.player.cooldown -= 1

   # проверка на уворот босса
   if chance(Characters.boss.miss_chance) == True:
      # сообщение с процентом шанса уворота
      Attack_messages.attack_messages_list.append(MyStrings.Text.miss_text.value + BotMessages.Message_text.miss_message(Characters.boss.miss_chance))
      # особое сообщения уворота Мела
      if Characters.boss.name == MyStrings.Text.mel_name.value:
         Characters.boss.mel_blazer_level += 1
         Attack_messages.attack_messages_list.append(MyStrings.Text.mel_miss_text.value)
      # сообщение об увороте босса   
      else:
         Attack_messages.attack_messages_list.append(MyStrings.Text.boss_miss_text.value)

   # проверка на пассивный навык Черного Стаса, вывод сообщения если да
   elif chance(30) == True and Characters.boss.name == MyStrings.Text.black_stas_name.value:
      Characters.player.health_down(Characters.player.damage)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.black_stas_returnal_message())
      
   # если босс не увернулся
   else:
      # если игрок оглушен
      if Characters.player.stan_timer > 0:
         Characters.player.stan_timer -= 1
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.stan_effect_message(Characters.player.name))
      # если игрок не оглушен
      elif Characters.player.stan_timer <= 0:
         attack_turn()
         lifesteal()
         boss_returnal()
      # если босс оглушен
      if Characters.boss.stan_timer > 0:
         Characters.boss.stan_timer -= 1
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.stan_effect_message(Characters.boss.name))
      # если босс не оглушен
      elif Characters.boss.stan_timer <= 0:
         boss_attack()

   boss_end_skill_activation()
   bleeding()
   poison()
   regeneration()
   boss_charge_skill_up()

def attack_turn():
   global player_attack_damage
   # проверка критической атаки для вывода нужного сообщения и ее применение
   player_attack_damage = Characters.player.damage
   if chance(Characters.player.critical_chance) == True:
      Characters.boss.health_down(player_attack_damage * 2)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.player_critical_attack_message())
   else:
      Characters.boss.health_down(player_attack_damage)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.player_attack_message())
   
def lifesteal():
   # проверка на вампиризм, применение и вывод сообщения
   if Characters.player.lifesteal > 0:
      Characters.player.health_up(player_attack_damage * Characters.player.lifesteal // 100)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.lifesteal_message())

def boss_returnal():
   # проверка на обратку босса, применение и вывод сообщения 
   if Characters.boss.returnal_value > 0:
      Characters.player.health_down(player_attack_damage * Characters.boss.returnal_value // 100)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.returnal_message())

def boss_attack():
   global boss_attack_damage
   # проверка является ли игрок Митей, а босс Инквизицией для особоых условий боя + вывод сообщения
   if Characters.player.name == MyStrings.Text.mitya_name.value and Characters.boss.name == MyStrings.Text.inkvisizia_name.value:
      Characters.player.health_up_procent(50)
      Attack_messages.attack_messages_list.append(MyStrings.Text.mitya_inkvisizia_text.value)
   
   else:
      # проверка на уворот игрока с выводом сообщения
      if chance(Characters.player.miss_chance) == True:
         Attack_messages.attack_messages_list.append(Characters.player.name + BotMessages.Message_text.miss_message(Characters.player.miss_chance))
      # критическая атака босса с выводом сообщения
      elif chance(Characters.boss.critical_chance) == True:
         boss_attack_damage = Characters.boss.damage * 2
         Characters.player.health_down(boss_attack_damage)
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.boss_critical_attack_message())
      # обычная атака босса с выводом сообщения
      elif chance(Characters.boss.critical_chance) == False:
         boss_attack_damage = Characters.boss.damage
         Characters.player.health_down(boss_attack_damage)
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.boss_attack_message())
      
def boss_end_skill_activation():  
   # проверка на уровень здоровья и статус воскрешения босса, применение воскрешения с выводом сообщения
   if Characters.boss.resurrection == True and Characters.boss.health <= 200:
      Characters.boss.resurrection = False
      Characters.boss.health_up(800)
      # особое сообщение если босс Чайковский
      if Characters.boss.name == MyStrings.Text.chaikovskii_name.value:
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.chaikovskii_ressurection_message())
      # обычное сообщение воскрешения
      else:
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.boss_ressurection_message())
      
   # применение завершающей способности Вива, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.viv_name.value:
      Characters.boss.damage_up(Characters.boss.viv_damage_up_skill_value)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.viv_end_skill_message())

   # применение завершающей рандомной способности Котенка, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.kitty_name.value and chance(Characters.boss.end_skill_chance) == True:
      kitty_skill_choice = random.randint(0, 11)
      # оглушение на игрока
      if kitty_skill_choice > 5:
         Characters.player.stan_timer = 1
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.kitty_stan_message())
      # кровотечение на игрока
      elif kitty_skill_choice <= 5:
         Characters.player.health_down(Characters.boss.kity_end_skill_damage)
         Characters.player.bleeding = True
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.kitty_bleeding_message())
   
   # применение завершающей способности Пьяного Лехи, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.drunk_leha_name.value:
      Characters.boss.health_up_procent(Characters.boss.drunk_leha_boost_skill_value)
      Characters.boss.damage_up_procent(Characters.boss.drunk_leha_boost_skill_value)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.drunk_leha_boost_message())
      
   # применение завершающей способности Доктора Лехи, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.doc_leha_name.value and chance(Characters.boss.end_skill_chance) == True:
      Characters.player.health_down(Characters.boss.doc_leha_end_skill_damage)
      Characters.player.bleeding = True
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.doc_leha_bleeding_message())
      
   # применение завершающей способности Мела, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.mel_name.value and Characters.boss.mel_blazer_level >= 3:
      Characters.boss.mel_blazer_level = 0
      Characters.player.health_down(Characters.boss.mel_end_skill_damage)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.mel_end_skill_message())
      
   # применение завершающей способности Дрона, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.dron_name.value:
      if chance(Characters.boss.dron_obida_level) == True:
         Characters.player.health_down(Characters.boss.dron_end_skill_damage)
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.dron_end_skill_message())
         
   # применение одной из рандомных завершающих способностей Валеры, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.glad_name.value:
      glad_skill_choice = random.randint(1, 6)
      # нанесение урона игроку
      if glad_skill_choice == 1:
         Characters.player.health_down(Characters.boss.glad_end_skill_damage)
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.glad_damage_skill_message())
      # увеличение здоровье Валеры
      elif glad_skill_choice == 2:
         Characters.boss.health_up(Characters.boss.glad_health_up_skill_value)
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.glad_health_up_skill_message())
      # увеличение шанса критической атаки Валеры
      elif glad_skill_choice == 3:
         Characters.boss.critical_chance_up(Characters.boss.glad_critical_up_skill_value)
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.glad_critical_up_skill_message())
      # уменьшение урона игрока
      elif glad_skill_choice == 4:
         Characters.player.damage_down(Characters.boss.glad_damage_down_skill_value)
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.glad_damage_down_skill_message())
      # наложение яда на игрока
      elif glad_skill_choice == 5:
         Characters.player.poison = True
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.glad_poison_skill_message())

   # применение завершающей способности Шивы, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.shiva_name.value:
      # увеличение шанса критической атаки Шивы
      if Characters.boss.critical_chance < 100:
         Characters.boss.critical_chance_up(Characters.boss.shiva_critical_up_skill_value)
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.shiva_critical_skill_message())
      # увеличение атаки Шивы, если шанс критической атаки заполнен до максимума
      elif Characters.boss.critical_chance >= 100:
         Characters.boss.damage_up_procent(Characters.boss.shiva_damage_up_skill_value)
         Attack_messages.attack_messages_list.append(BotMessages.Message_text.shiva_damage_up_skill_message())   

def bleeding():
   # проверка игрока на кровотечение и отсутствие иммунитета к нему, применение кровотечения, вывод сообщения
   if Characters.player.bleeding == True and Characters.player.immunity == False:
      Characters.player.health_down(Characters.Pers.bleeding_damage)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.bleeding_message(Characters.player.icon, MyStrings.Text.player_health_icon.value))
      
   # проверка босса на кровотечение, его применение и вывод сообщения
   if Characters.boss.bleeding == True:
      Characters.boss.health_down(Characters.Pers.bleeding_damage)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.bleeding_message(Characters.boss.icon, MyStrings.Text.boss_health_icon.value))

def poison():
   # проверка игрока на отравление и отсутствие иммунитета к нему, применение, вывод сообщения
   if Characters.player.poison == True and Characters.player.immunity == False:
      Characters.player.health_down_procent(Characters.Pers.poison_damage)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.poison_message(Characters.player.icon, MyStrings.Text.player_health_icon.value))

   # проверка босса на отравление, применение, вывод сообщения
   if Characters.boss.poison == True:
      Characters.boss.health_down_procent(Characters.Pers.poison_damage)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.poison_message(Characters.boss.icon, MyStrings.Text.boss_health_icon.value))

   # увеличение на 10% урона отравления на время боя
   Characters.Pers.poison_damage += 10

def regeneration():
   # проверка игрока на регенерацию, применение, вывод сообщения
   if Characters.player.regeneration > 0:
      Characters.player.health_up(Characters.Pers.regeneration_value)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.regeneration_message(Characters.player.icon, MyStrings.Text.player_health_icon.value))

   # проверка босса на регенерацию, применение, вывод сообщения   
   if Characters.boss.regeneration > 0:
      Characters.boss.health_up(Characters.Pers.regeneration_value)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.regeneration_message(Characters.boss.icon, MyStrings.Text.boss_health_icon.value))

def boss_charge_skill_up():
   # увеличение шкалы накопительной способности босса
   if Characters.boss.name == MyStrings.Text.dron_name.value:
      Characters.boss.dron_obida_level += 5

   elif Characters.boss.name == MyStrings.Text.sledovatel_name.value:
      Characters.player.busted_level += 20   

def player_skill_use():
   # использование активной способности, если игрок не оглушен, не обезмолвлен, способность не перезаряжается
   if Characters.player.cooldown <= 0 and Characters.player.silence == False and Characters.player.stan_timer <= 0:
      Characters.player.cooldown = 0
      skill_activation(Characters.player.name)

   # вывод сообщения если игрок оглушен
   elif Characters.player.stan_timer > 0:
      Attack_messages.skill_use_message = MyStrings.Text.player_stan_text.value

   # вывод сообщения если игрок обезмолвлен
   elif Characters.player.silence == True:
      Attack_messages.skill_use_message = MyStrings.Text.player_silence_text.value

   # вывод сообщения если способность перезаряжается
   elif Characters.player.cooldown > 0:
      Attack_messages.skill_use_message = MyStrings.Text.cooldown_text.value  

def skill_activation(player_name):
   # подбор способности исходя из имени игрока, ее применение, установка перезарядки и вывод сообщения с ее описанием

   if player_name == MyStrings.Text.mitya_name.value:
      Characters.player.health_down(Characters.player.mitya_health_down_skill_value)
      Characters.player.damage_up(Characters.player.mitya_damage_up_skill_value)
      Characters.player.cooldown = 1
      Characters.player.mitya_elexir_count += 1
      Attack_messages.skill_use_message = MyStrings.Text.mitya_skill_effect_text.value

   elif player_name == MyStrings.Text.sanya_name.value:
      global sanya_skill_damage
      sanya_skill_damage = random.randint(50, 500)
      Characters.boss.health_down(sanya_skill_damage)
      Characters.player.cooldown = 3
      Attack_messages.skill_use_message = BotMessages.Message_text.sanya_skill_message()

   elif player_name == MyStrings.Text.toshik_name.value:
      Characters.player.health_up_procent(Characters.player.toshik_health_up_skill_procent)
      Characters.player.cooldown = 2
      Attack_messages.skill_use_message = MyStrings.Text.toshik_skill_effect_text.value

   elif player_name == MyStrings.Text.kolya_name.value:
      global kolya_hack_damage_value
      kolya_hack_damage_value = Characters.boss.damage * 50 // 100
      Characters.player.damage_up(kolya_hack_damage_value)
      Characters.boss.damage_down(kolya_hack_damage_value)
      Characters.player.cooldown = 3
      Attack_messages.skill_use_message = BotMessages.Message_text.kolya_skill_message()

   elif player_name == MyStrings.Text.temich_name.value:
      temich_skill_check = chance(Characters.player.temich_skill_chance)
      if temich_skill_check == False:
         Characters.boss.health, Characters.player.health = Characters.player.health, Characters.boss.health
         Characters.player.cooldown = 1
         Attack_messages.skill_use_message = MyStrings.Text.temich_skill_effect_text.value
      elif temich_skill_check == True:
         Characters.player.stan_timer = 1
         Attack_messages.skill_use_message = BotMessages.Message_text.temich_skill_stan_message()

def player_item_use():
   if Characters.player.item != MyStrings.Text.empty_text.value and Characters.player.silence == False and Characters.player.stan_timer <= 0:
      Drop.item_activation(Characters.player.item)
      Attack_messages.item_use_message = Drop.item.description
      Characters.player.item = MyStrings.Text.empty_text.value

   elif Characters.player.stan_timer > 0:
      Attack_messages.item_use_message = MyStrings.Text.player_stan_text.value

   elif Characters.player.item != MyStrings.Text.empty_text.value and Characters.player.silence == True:
      Attack_messages.item_use_message = MyStrings.Text.player_silence_text.value

   elif Characters.player.item == MyStrings.Text.empty_text.value:
      Attack_messages.item_use_message = MyStrings.Text.empty_click_text.value

def fight_victory():
   # сброс всех статусов игрока, увеличение количества побед
   Characters.player.cooldown = 0
   Characters.Pers.win_rate += 1
   Characters.player.poison = False
   Characters.player.bleeding = False
   Characters.player.silence = False
   Characters.Pers.poison_damage = 5
   Characters.player.busted_level = 0

   # если игрок Саня выиграл босса Саню - применение особых наград, вывод сообщения
   if Characters.Pers.win_rate < 8 and Characters.boss.name == MyStrings.Text.sanya_name.value:
      Characters.player.health_up_procent(Characters.player.sanya_win_sanya_heath_up_procent)
      Characters.player.damage_up_procent(Characters.player.sanya_win_sanya_damage_up_procent)
      Characters.player.critical_chance_up(Characters.player.sanya_win_sanya_critical_up_procent)
      Attack_messages.sanya_win_sanya_message = MyStrings.Text.sanya_sasha_text.value

   # если игрок Тошик - применение его пассивной способности, вывод сообщения
   elif Characters.Pers.win_rate < 8 and Characters.player.name == MyStrings.Text.toshik_name.value:
      Characters.player.damage_up(Characters.player.health * Characters.player.toshik_passive_skill_procent // 100)
      Attack_messages.toshik_passive_skill_message = MyStrings.Text.toshik_passive_skill_text.value