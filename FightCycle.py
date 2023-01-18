import Characters
import ItemsGenerator
import CharactersGenerator
import FightFunctions
import FightStrings
import InteractionParameters
import BossStrings
import GameStrings
import StatsStrings
import PlayerStrings
import random

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

      # особая способность при уклонении босса Черный Стас
      if CharactersGenerator.boss.name == BossStrings.BlackStas.name:
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
   FightFunctions.bleeding()
   FightFunctions.poison()
   FightFunctions.regeneration()
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
   if CharactersGenerator.boss.resurrection == True and \
      CharactersGenerator.boss.health <= 200:
      CharactersGenerator.boss.resurrection = False
      CharactersGenerator.boss.health_up(Characters.Pers.ressurection_value)
      Attack_messages.messages_pool.append(FightStrings.Banners.ressurection(False))
      
   # применение завершающей способности Вива
   elif CharactersGenerator.boss.name == BossStrings.Viv.name:
      CharactersGenerator.boss.damage_up(Characters.Boss.viv_end_skill_damage_up)
      Attack_messages.messages_pool.append(FightStrings.BossMessages.viv_end_skill())

   # применение завершающей рандомной способности Котенка
   elif CharactersGenerator.boss.name == BossStrings.Kitty.name and \
         FightFunctions.chance(CharactersGenerator.boss.end_skill_chance) == True:
      kitty_skill_choice = random.randint(0, 11)
      # оглушение на игрока
      if kitty_skill_choice > 5:
         CharactersGenerator.player.stan_timer = 1
         Attack_messages.messages_pool.append(FightStrings.BossMessages.kitty_stan())
      # кровотечение на игрока
      elif kitty_skill_choice <= 5:
         CharactersGenerator.player.health_down(CharactersGenerator.boss.kitty_end_skill_damage)
         CharactersGenerator.player.bleeding = True
         Attack_messages.messages_pool.append(FightStrings.BossMessages.kitty_bleeding())
   
   # применение завершающей способности Пьяного Лехи
   elif CharactersGenerator.boss.name == BossStrings.DrunkLeha.name:
      CharactersGenerator.boss.health_up_procent(CharactersGenerator.boss.drunk_leha_end_skill_boost)
      CharactersGenerator.boss.damage_up_procent(CharactersGenerator.boss.drunk_leha_end_skill_boost)
      Attack_messages.messages_pool.append(FightStrings.BossMessages.drunk_leha_boost())
      
   # применение завершающей способности Доктора Лехи
   elif CharactersGenerator.boss.name == BossStrings.DocLeha.name \
         and FightFunctions.chance(CharactersGenerator.boss.end_skill_chance) == True:
      CharactersGenerator.player.health_down(CharactersGenerator.boss.doc_leha_end_skill_damage)
      CharactersGenerator.player.bleeding = True
      Attack_messages.messages_pool.append(FightStrings.BossMessages.doc_leha_bleeding())
      
   # применение завершающей способности Мела
   elif CharactersGenerator.boss.name == BossStrings.Mel.name \
         and CharactersGenerator.boss.skill_meter_level >= 3:
      CharactersGenerator.boss.skill_meter_level = 0
      CharactersGenerator.player.health_down(CharactersGenerator.boss.mel_end_skill_damage)
      Attack_messages.messages_pool.append(FightStrings.BossMessages.mel_end_skill())
      
   # применение завершающей способности Дрона
   elif CharactersGenerator.boss.name == BossStrings.Dron.name \
      and FightFunctions.chance(CharactersGenerator.boss.skill_meter_level) == True:
         CharactersGenerator.player.health_down(CharactersGenerator.boss.dron_end_skill_damage)
         Attack_messages.messages_pool.append(FightStrings.BossMessages.dron_end_skill())
         
   # применение одной из рандомных завершающих способностей Валеры
   elif CharactersGenerator.boss.name == BossStrings.Glad.name:
      glad_skill_choice = random.randint(1, 6)
      # нанесение урона игроку
      if glad_skill_choice == 1:
         CharactersGenerator.player.health_down(CharactersGenerator.boss.glad_end_skill_damage)
         Attack_messages.messages_pool.append(FightStrings.BossMessages.glad_damage_skill())
      # увеличение здоровье Валеры
      elif glad_skill_choice == 2:
         CharactersGenerator.boss.health_up(CharactersGenerator.boss.glad_end_skill_health_up)
         Attack_messages.messages_pool.append(FightStrings.BossMessages.glad_health_up_skill())
      # увеличение шанса критической атаки Валеры
      elif glad_skill_choice == 3:
         CharactersGenerator.boss.critical_chance_up(CharactersGenerator.boss.glad_end_skill_critical_up)
         Attack_messages.messages_pool.append(FightStrings.BossMessages.glad_critical_up_skill())
      # уменьшение урона игрока
      elif glad_skill_choice == 4:
         CharactersGenerator.player.damage_down(CharactersGenerator.boss.glad_end_skill_damage_down)
         Attack_messages.messages_pool.append(FightStrings.BossMessages.glad_damage_down_skill())
      # наложение яда на игрока
      elif glad_skill_choice == 5:
         CharactersGenerator.player.poison = True
         Attack_messages.messages_pool.append(FightStrings.BossMessages.glad_poison_skill())

   # применение завершающей способности Шивы
   elif CharactersGenerator.boss.name == BossStrings.Shiva.name:
      # увеличение шанса критической атаки Шивы
      if CharactersGenerator.boss.critical_chance < 100:
         CharactersGenerator.boss.critical_chance_up(CharactersGenerator.boss.shiva_end_skill_critical_up)
         Attack_messages.messages_pool.append(FightStrings.BossMessages.shiva_critical_skill())
      # увеличение атаки Шивы, если шанс критической атаки заполнен до максимума
      elif CharactersGenerator.boss.critical_chance >= 100:
         CharactersGenerator.boss.damage_up_procent(CharactersGenerator.boss.shiva_end_skill_damage_up)
         Attack_messages.messages_pool.append(FightStrings.BossMessages.shiva_damage_up_skill())   


def boss_charge_skill_up():
   # увеличение шкалы накопительной способности босса
   if CharactersGenerator.boss.name == BossStrings.Dron.name:
      CharactersGenerator.boss.skill_meter_level += 10

   elif CharactersGenerator.boss.name == BossStrings.Sledovatel.name:
      CharactersGenerator.player.police_wanted += 20 

   elif CharactersGenerator.boss.name == BossStrings.Mel.name:
      CharactersGenerator.boss.skill_meter_level += 1

def player_skill_use():
   # использование активной способности, 
   # если игрок не оглушен, не обезмолвлен, 
   # способность не перезаряжается

   if CharactersGenerator.player.cooldown <= 0 and \
         CharactersGenerator.player.silence == False and \
            CharactersGenerator.player.stan_timer <= 0:
      CharactersGenerator.player.cooldown = 0
      skill_activation(CharactersGenerator.player.name)

   # вывод сообщения если игрок оглушен
   elif CharactersGenerator.player.stan_timer > 0:
      Attack_messages.skill_use = GameStrings.Text.player_stan

   # вывод сообщения если игрок обезмолвлен
   elif CharactersGenerator.player.silence == True:
      Attack_messages.skill_use = GameStrings.Text.player_silence

   # вывод сообщения если способность перезаряжается
   elif CharactersGenerator.player.cooldown > 0:
      Attack_messages.skill_use = GameStrings.Text.player_cooldown  

def skill_activation(player_name):
   # подбор способности исходя из имени игрока, 
   # ее применение, установка перезарядки

   if player_name == PlayerStrings.Mitya.name:
      CharactersGenerator.player.health_down(Characters.Player.mitya_health_down_skill_value)
      CharactersGenerator.player.damage_up(Characters.Player.mitya_damage_up_skill_value)
      CharactersGenerator.player.cooldown = 1
      CharactersGenerator.player.mitya_elexir_count += 1
      Attack_messages.skill_use = PlayerStrings.Mitya.skill_effect()

   elif player_name == PlayerStrings.Sanya.name:
      global sanya_skill_damage
      sanya_skill_damage = random.randint(50, 500)
      CharactersGenerator.boss.health_down(sanya_skill_damage)
      CharactersGenerator.player.cooldown = 3
      Attack_messages.skill_use = PlayerStrings.Sanya.skill_effect()

   elif player_name == PlayerStrings.Toshik.name:
      CharactersGenerator.player.health_up_procent(Characters.Player.toshik_health_up_skill_procent)
      CharactersGenerator.player.cooldown = 2
      Attack_messages.skill_use = PlayerStrings.Toshik.skill_effect()

   elif player_name == PlayerStrings.Kolya.name:
      global kolya_hack_damage_value
      kolya_hack_damage_value = CharactersGenerator.boss.damage * 50 // 100
      CharactersGenerator.player.damage_up(kolya_hack_damage_value)
      CharactersGenerator.boss.damage_down(kolya_hack_damage_value)
      CharactersGenerator.player.cooldown = 3
      Attack_messages.skill_use = PlayerStrings.Kolya.skill_effect()

   elif player_name == PlayerStrings.Temich.name:
      temich_skill_check = FightFunctions.chance(CharactersGenerator.player.temich_skill_chance)
      if temich_skill_check == False:
         CharactersGenerator.boss.health, CharactersGenerator.player.health = \
            CharactersGenerator.player.health, CharactersGenerator.boss.health
         CharactersGenerator.player.cooldown = 1
         Attack_messages.skill_use = PlayerStrings.Temich.good_skill_effect()
      elif temich_skill_check == True:
         CharactersGenerator.player.stan_timer = 1
         Attack_messages.skill_use = PlayerStrings.Temich.bad_skill_effect()

def player_item_use():
   if CharactersGenerator.player.item != GameStrings.Text.empty and \
         CharactersGenerator.player.silence == False and \
            CharactersGenerator.player.stan_timer <= 0:
      ItemsGenerator.item_activation(CharactersGenerator.player.item)
      Attack_messages.item_use = ItemsGenerator.item.description
      CharactersGenerator.player.item = GameStrings.Text.empty

   elif CharactersGenerator.player.stan_timer > 0:
      Attack_messages.item_use = GameStrings.Text.player_stan

   elif CharactersGenerator.player.item != GameStrings.Text.player_stan and \
         CharactersGenerator.player.silence == True:
      Attack_messages.item_use = GameStrings.Text.player_silence

   elif CharactersGenerator.player.item == GameStrings.Text.empty:
      Attack_messages.item_use = GameStrings.Text.empty_click

def fight_victory():
   # сброс всех статусов игрока, увеличение количества побед
   CharactersGenerator.player.cooldown = 0
   Characters.Pers.win_rate += 1
   CharactersGenerator.player.poison = False
   CharactersGenerator.player.bleeding = False
   CharactersGenerator.player.silence = False
   Characters.Pers.poison_damage = 5

   # если игрок Саня выиграл босса Саню - применение особых наград
   if Characters.Pers.win_rate < 8 and CharactersGenerator.boss.name == BossStrings.Sasha:
      CharactersGenerator.player.health_up_procent(InteractionParameters.Boss.sanya_sasha_health_up)
      CharactersGenerator.player.damage_up_procent(InteractionParameters.Boss.sanya_sasha_damage_up)
      CharactersGenerator.player.critical_chance_up(InteractionParameters.Boss.sanya_sasha_critical_up)
      Attack_messages.messages_pool.append(FightStrings.BossMessages.sasha_victory())

   # если игрок Тошик - применение его пассивной способности
   elif Characters.Pers.win_rate < 8 and \
      CharactersGenerator.player.name == PlayerStrings.Toshik.name:
      CharactersGenerator.player.damage_up(CharactersGenerator.player.health 
                                             * CharactersGenerator.player.toshik_passive_skill_procent 
                                             // 100)
      Attack_messages.messages_pool.append(PlayerStrings.Toshik.passive_effect())