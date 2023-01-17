import Characters
import CharactersGenerator
import FightFunctions
import FightStrings
import GameStrings
import BossStrings
import StatsStrings
import PlayerStrings
import random
import Drop

class Attack_messages():
   # вспомогательный класс, для создания списка 
   # возникающих сообщений во время боя
   skill_use = False
   item_use = False
   sanya_win_sanya = False
   toshik_passive_skill = False
   # здесь записываются все возникающие сообщения во время цикла боя
   messages_pool = []


# атака
def attack():
   # снижение перезарядки способности игрока
   CharactersGenerator.player.cooldown -= 1

   # проверка на уворот босса
   if FightFunctions.chance(CharactersGenerator.boss.miss_chance) == True:

      # повышение накопительной способности босса при уклонении, 
      # если она у него есть
      if CharactersGenerator.boss.skill_meter_level != 0:
         CharactersGenerator.boss.skill_meter_level += 1

      # особая способность при уклонении босса Черный Стас
      elif CharactersGenerator.boss.name == BossStrings.BlackStas.name:
         CharactersGenerator.player.health_down(CharactersGenerator.player.damage)

      # добавление в пул сообщений баннера Уклонение
      Attack_messages.messages_pool.append(FightStrings.Banners.miss(False))
      
      
   # если босс не увернулся
   else:
      # если игрок оглушен
      if CharactersGenerator.player.stan_timer > 0:
         # понижение таймера оглушения игрока
         CharactersGenerator.player.stan_timer -= 1
         # добавление в пул сообщений баннера Оглушение
         Attack_messages.messages_pool.append(FightStrings.Banners.stan\
                                                (CharactersGenerator.player.name))

      # если игрок не оглушен
      elif CharactersGenerator.player.stan_timer <= 0:
         player_attack()
         FightFunctions.lifesteal()
         FightFunctions.boss_returnal()

      # если босс оглушен
      if CharactersGenerator.boss.stan_timer > 0:
         # понижение таймера оглушения босса
         CharactersGenerator.boss.stan_timer -= 1
         # добавление в пул сообщений баннера Оглушение
         Attack_messages.messages_pool.append(FightStrings.Banners.stan\
                                                (CharactersGenerator.boss.name))
                                                
      # если босс не оглушен
      elif CharactersGenerator.boss.stan_timer <= 0:
         boss_attack()

   boss_end_skill_activation()
   bleeding()
   poison()
   regeneration()
   boss_charge_skill_up()

def player_attack():
   global player_attack_damage
   # переменная со значением урона игрока
   player_attack_damage = CharactersGenerator.player.damage

   # если урон критический, значение урона умножается на 2
   if FightFunctions.chance(CharactersGenerator.player.critical_chance) == True:
      player_attack_damage *= 2
      CharactersGenerator.boss.health_down(player_attack_damage)

      # добавление в пул сообщений баннера Критический урон
      Attack_messages.messages_pool.append(FightStrings.Banners.critical_attack(True))

   # если урон не критический
   else:
      CharactersGenerator.boss.health_down(player_attack_damage)
      Attack_messages.messages_pool.append(StatsStrings.attack(True))
   

def boss_attack():
   global boss_attack_damage
   # проверка является ли игрок Митей и босс Инквизицией
   # для особоых условий боя (босс лечит вместо урона)
   if CharactersGenerator.player.name == PlayerStrings.Mitya.name \
      and CharactersGenerator.boss.name == BossStrings.Inkvisizia.name:

      CharactersGenerator.player.health_up(CharactersGenerator.boss.damage)
      Attack_messages.messages_pool.append(PlayerStrings.Mitya.inkvisizia_interaction())
   
   else:
      # переменная со значением урона босса
      boss_attack_damage = CharactersGenerator.boss.damage
      # проверка на уворот игрока
      if FightFunctions.chance(CharactersGenerator.player.miss_chance) == True:
         Attack_messages.messages_pool.append(FightStrings.Banners.miss(True))

      # критическая атака босса
      elif FightFunctions.chance(CharactersGenerator.boss.critical_chance) == True:
         boss_attack_damage *= 2
         CharactersGenerator.player.health_down(boss_attack_damage)
         Attack_messages.messages_pool.append(FightStrings.Banners.critical_attack(False))

      # обычная атака босса
      elif FightFunctions.chance(CharactersGenerator.boss.critical_chance) == False:
         CharactersGenerator.player.health_down(boss_attack_damage)
         Attack_messages.messages_pool.append(StatsStrings.attack(False))
      
def boss_end_skill_activation():  
   # проверка на уровень здоровья и статус воскрешения босса, применение воскрешения
   if CharactersGenerator.boss.resurrection == True and Characters.boss.health <= 200:
      CharactersGenerator.boss.resurrection = False
      CharactersGenerator.boss.health_up(800)
      # особое сообщение если босс Чайковский
      if CharactersGenerator.boss.name == MyStrings.Text.chaikovskii_name.value:
         Attack_messages.messages_pool.append(BotMessages.Message_text.chaikovskii_ressurection_message())
      # обычное сообщение воскрешения
      else:
         Attack_messages.messages_pool.append(BotMessages.Message_text.boss_ressurection_message())
      
   # применение завершающей способности Вива, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.viv_name.value:
      Characters.boss.damage_up(Characters.boss.viv_end_skill_damage_up)
      Attack_messages.messages_pool.append(BotMessages.Message_text.viv_end_skill_message())

   # применение завершающей рандомной способности Котенка, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.kitty_name.value and chance(Characters.boss.end_skill_chance) == True:
      kitty_skill_choice = random.randint(0, 11)
      # оглушение на игрока
      if kitty_skill_choice > 5:
         Characters.player.stan_timer = 1
         Attack_messages.messages_pool.append(BotMessages.Message_text.kitty_stan_message())
      # кровотечение на игрока
      elif kitty_skill_choice <= 5:
         Characters.player.health_down(Characters.boss.kitty_end_skill_damage)
         Characters.player.bleeding = True
         Attack_messages.messages_pool.append(BotMessages.Message_text.kitty_bleeding_message())
   
   # применение завершающей способности Пьяного Лехи, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.drunk_leha_name.value:
      Characters.boss.health_up_procent(Characters.boss.drunk_leha_end_skill_boost)
      Characters.boss.damage_up_procent(Characters.boss.drunk_leha_end_skill_boost)
      Attack_messages.messages_pool.append(BotMessages.Message_text.drunk_leha_boost_message())
      
   # применение завершающей способности Доктора Лехи, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.doc_leha_name.value and chance(Characters.boss.end_skill_chance) == True:
      Characters.player.health_down(Characters.boss.doc_leha_end_skill_damage)
      Characters.player.bleeding = True
      Attack_messages.messages_pool.append(BotMessages.Message_text.doc_leha_bleeding_message())
      
   # применение завершающей способности Мела, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.mel_name.value and Characters.boss.mel_blazer_level >= 3:
      Characters.boss.mel_blazer_level = 0
      Characters.player.health_down(Characters.boss.mel_end_skill_damage)
      Attack_messages.messages_pool.append(BotMessages.Message_text.mel_end_skill_message())
      
   # применение завершающей способности Дрона, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.dron_name.value:
      if chance(Characters.boss.dron_obida_level) == True:
         Characters.player.health_down(Characters.boss.dron_end_skill_damage)
         Attack_messages.messages_pool.append(BotMessages.Message_text.dron_end_skill_message())
         
   # применение одной из рандомных завершающих способностей Валеры, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.glad_name.value:
      glad_skill_choice = random.randint(1, 6)
      # нанесение урона игроку
      if glad_skill_choice == 1:
         Characters.player.health_down(Characters.boss.glad_end_skill_damage)
         Attack_messages.messages_pool.append(BotMessages.Message_text.glad_damage_skill_message())
      # увеличение здоровье Валеры
      elif glad_skill_choice == 2:
         Characters.boss.health_up(Characters.boss.glad_end_skill_health_up)
         Attack_messages.messages_pool.append(BotMessages.Message_text.glad_health_up_skill_message())
      # увеличение шанса критической атаки Валеры
      elif glad_skill_choice == 3:
         Characters.boss.critical_chance_up(Characters.boss.glad_end_skill_critical_up)
         Attack_messages.messages_pool.append(BotMessages.Message_text.glad_critical_up_skill_message())
      # уменьшение урона игрока
      elif glad_skill_choice == 4:
         Characters.player.damage_down(Characters.boss.glad_damage_down_skill_value)
         Attack_messages.messages_pool.append(BotMessages.Message_text.glad_damage_down_skill_message())
      # наложение яда на игрока
      elif glad_skill_choice == 5:
         Characters.player.poison = True
         Attack_messages.messages_pool.append(BotMessages.Message_text.glad_poison_skill_message())

   # применение завершающей способности Шивы, вывод сообщения
   elif Characters.boss.name == MyStrings.Text.shiva_name.value:
      # увеличение шанса критической атаки Шивы
      if Characters.boss.critical_chance < 100:
         Characters.boss.critical_chance_up(Characters.boss.shiva_end_skill_critical_up)
         Attack_messages.messages_pool.append(BotMessages.Message_text.shiva_critical_skill_message())
      # увеличение атаки Шивы, если шанс критической атаки заполнен до максимума
      elif Characters.boss.critical_chance >= 100:
         Characters.boss.damage_up_procent(Characters.boss.shiva_end_skill_damage_up)
         Attack_messages.messages_pool.append(BotMessages.Message_text.shiva_damage_up_skill_message())   


def boss_charge_skill_up():
   # увеличение шкалы накопительной способности босса
   if Characters.boss.name == MyStrings.Text.dron_name.value:
      Characters.boss.dron_obida_level += 5

   elif Characters.boss.name == MyStrings.Text.sledovatel_name.value:
      Characters.player.police_level += 20   

def player_skill_use():
   # использование активной способности, если игрок не оглушен, не обезмолвлен, способность не перезаряжается
   if Characters.player.cooldown <= 0 and Characters.player.silence == False and Characters.player.stan_timer <= 0:
      Characters.player.cooldown = 0
      skill_activation(Characters.player.name)

   # вывод сообщения если игрок оглушен
   elif Characters.player.stan_timer > 0:
      Attack_messages.skill_use = MyStrings.Text.player_stan_text.value

   # вывод сообщения если игрок обезмолвлен
   elif Characters.player.silence == True:
      Attack_messages.skill_use = MyStrings.Text.player_silence_text.value

   # вывод сообщения если способность перезаряжается
   elif Characters.player.cooldown > 0:
      Attack_messages.skill_use = MyStrings.Text.cooldown_text.value  

def skill_activation(player_name):
   # подбор способности исходя из имени игрока, ее применение, установка перезарядки и вывод сообщения с ее описанием

   if player_name == MyStrings.Text.mitya_name.value:
      Characters.player.health_down(Characters.player.mitya_health_down_skill_value)
      Characters.player.damage_up(Characters.player.mitya_damage_up_skill_value)
      Characters.player.cooldown = 1
      Characters.player.mitya_elexir_count += 1
      Attack_messages.skill_use = MyStrings.PlayerText.mitya_skill_effect()

   elif player_name == MyStrings.Text.sanya_name.value:
      global sanya_skill_damage
      sanya_skill_damage = random.randint(50, 500)
      Characters.boss.health_down(sanya_skill_damage)
      Characters.player.cooldown = 3
      Attack_messages.skill_use = BotMessages.Message_text.sanya_skill_message()

   elif player_name == MyStrings.Text.toshik_name.value:
      Characters.player.health_up_procent(Characters.player.toshik_health_up_skill_procent)
      Characters.player.cooldown = 2
      Attack_messages.skill_use = MyStrings.Text.toshik_skill_effect_text.value

   elif player_name == MyStrings.Text.kolya_name.value:
      global kolya_hack_damage_value
      kolya_hack_damage_value = Characters.boss.damage * 50 // 100
      Characters.player.damage_up(kolya_hack_damage_value)
      Characters.boss.damage_down(kolya_hack_damage_value)
      Characters.player.cooldown = 3
      Attack_messages.skill_use = BotMessages.Message_text.kolya_skill_message()

   elif player_name == MyStrings.Text.temich_name.value:
      temich_skill_check = chance(Characters.player.temich_skill_chance)
      if temich_skill_check == False:
         Characters.boss.health, Characters.player.health = Characters.player.health, Characters.boss.health
         Characters.player.cooldown = 1
         Attack_messages.skill_use = MyStrings.Text.temich_skill_effect_text.value
      elif temich_skill_check == True:
         Characters.player.stan_timer = 1
         Attack_messages.skill_use = BotMessages.Message_text.temich_skill_stan_message()

def player_item_use():
   if Characters.player.item != MyStrings.Text.empty_text.value and Characters.player.silence == False and Characters.player.stan_timer <= 0:
      Drop.item_activation(Characters.player.item)
      Attack_messages.item_use = Drop.item.description
      Characters.player.item = MyStrings.Text.empty_text.value

   elif Characters.player.stan_timer > 0:
      Attack_messages.item_use = MyStrings.Text.player_stan_text.value

   elif Characters.player.item != MyStrings.Text.empty_text.value and Characters.player.silence == True:
      Attack_messages.item_use = MyStrings.Text.player_silence_text.value

   elif Characters.player.item == MyStrings.Text.empty_text.value:
      Attack_messages.item_use = MyStrings.Text.empty_click_text.value

def fight_victory():
   # сброс всех статусов игрока, увеличение количества побед
   Characters.player.cooldown = 0
   Characters.Pers.win_rate += 1
   Characters.player.poison = False
   Characters.player.bleeding = False
   Characters.player.silence = False
   Characters.Pers.poison_damage = 5
   Characters.player.police_level = 0

   # если игрок Саня выиграл босса Саню - применение особых наград, вывод сообщения
   if Characters.Pers.win_rate < 8 and Characters.boss.name == MyStrings.Text.sanya_name.value:
      Characters.player.health_up_procent(Characters.player.sanya_win_sanya_heath_up_procent)
      Characters.player.damage_up_procent(Characters.player.sanya_win_sanya_damage_up_procent)
      Characters.player.critical_chance_up(Characters.player.sanya_win_sanya_critical_up_procent)
      Attack_messages.sanya_win_sanya = MyStrings.Text.sanya_sasha_text.value

   # если игрок Тошик - применение его пассивной способности, вывод сообщения
   elif Characters.Pers.win_rate < 8 and Characters.player.name == MyStrings.Text.toshik_name.value:
      Characters.player.damage_up(Characters.player.health * Characters.player.toshik_passive_skill_procent // 100)
      Attack_messages.toshik_passive_skill = MyStrings.Text.toshik_passive_skill_text.value