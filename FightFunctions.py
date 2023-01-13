import random
import BossStrings

class BossList():
   list_easy = ['Палыч', 'Чайковский', 'Вив', 'Саша Шлякин', 'Качаловская Тварь', 'Рандом Рандомыч', 'Котенок-тролль']
   list_medium = ['Инквизиция', 'Доктор Леха', 'Пьяный Леха', 'Мел', 'Рыжий', 'Следователь']
   list_hard = ['Донер Кебаб', 'Черный Стас', 'Дрон', 'Валера Гладиатор', 'Великая Шива']

def boss_difficult_choice(win_rate):
   global boss_name

   if win_rate < 3:
      boss_name = random.choice(BossList.list_easy)
      BossList.list_easy.remove(boss_name)
   elif win_rate < 6 and win_rate >= 3:
      boss_name = random.choice(BossList.list_medium)
      BossList.list_medium.remove(boss_name)
   elif win_rate < 9 and win_rate >= 6:
      boss_name = random.choice(BossList.list_hard)
      BossList.list_hard.remove(boss_name)
   elif win_rate == 9:
      boss_name = [BossStrings.Makar.name]

def boss_prelude_skill_activation(boss_name):
   global prelude_skill_message
   
   prelude_skill_message = False

   if boss_name == MyStrings.Text.palich_name.value:
      player.silence = True
      prelude_skill_message = MyStrings.Text.palich_prelude_text.value

   elif boss_name == MyStrings.Text.redhead_name.value:
      player.poison = True
      prelude_skill_message = MyStrings.Text.redhead_prelude_text.value

   elif boss_name == MyStrings.Text.sledovatel_name.value:
      drugs = MyStrings.Text.marki_name.value, MyStrings.Text.madam_name.value, MyStrings.Text.marki_name.value
      cross_check = [x for x in drugs if x in player.all_items]
      if player.damage > 500:
         player.health_down_procent(50)
         prelude_skill_message = MyStrings.Text.sledovatel_damage_prelude_text.value
      elif player.mitya_elexir_count > 0 or len(cross_check) > 0:
         player.police_level += 50
         prelude_skill_message = MyStrings.Text.sledovatel_drugcheck_text.value
      elif player.damage > 500 and player.mitya_elexir_count > 0 or len(cross_check) > 0:
         player.health_down_procent(50)
         player.police_level += 50
         prelude_skill_message = MyStrings.Text.sledovatel_damage_prelude_text.value + '\n' + MyStrings.Text.sledovatel_drugcheck_text.value

   elif boss_name == MyStrings.Text.dron_name.value:
      obida_level = 0
      obida_level += len(player.all_items) * 5
      prelude_skill_message = MyStrings.Text.dron_bratishki_text.value
      if MyStrings.Text.dron_meat_name.value in player.all_items:
         obida_level += 10
         prelude_skill_message += '\n' + MyStrings.Text.dron_dron_meat_text.value

   elif boss_name == MyStrings.Text.doner_name.value and MyStrings.Text.everlast_name.value in player.all_items:
      boss.health_up_procent(10)
      boss.damage_up_procent(10)
      prelude_skill_message = MyStrings.Text.doner_everlast_text.value

   elif boss_name == MyStrings.Text.black_stas_name.value and player.name == MyStrings.Text.mitya_name.value:
      boss.damage_up(player.mitya_elexir_count * 200)
      prelude_skill_message = MyStrings.Text.black_stas_mitya_text.value

def chance(x):
   # генератор вероятности
   chance = random.randint(1, 100) in range(1, x)
   return chance

def bleeding():
   # проверка игрока на кровотечение и отсутствие иммунитета к нему, применение кровотечения, вывод сообщения
   if Characters.player.bleeding == True and Characters.player.immunity == False:
      Characters.player.health_down(Characters.Pers.bleeding_damage)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.bleeding_message(Characters.player.icon, MyStrings.Text.player_health.value))
      
   # проверка босса на кровотечение, его применение и вывод сообщения
   if Characters.boss.bleeding == True:
      Characters.boss.health_down(Characters.Pers.bleeding_damage)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.bleeding_message(Characters.boss.icon, MyStrings.Text.boss_health.value))

def poison():
   # проверка игрока на отравление и отсутствие иммунитета к нему, применение, вывод сообщения
   if Characters.player.poison == True and Characters.player.immunity == False:
      Characters.player.health_down_procent(Characters.Pers.poison_damage)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.poison_message(Characters.player.icon, MyStrings.Text.player_health.value))

   # проверка босса на отравление, применение, вывод сообщения
   if Characters.boss.poison == True:
      Characters.boss.health_down_procent(Characters.Pers.poison_damage)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.poison_message(Characters.boss.icon, MyStrings.Text.boss_health.value))

   # увеличение на 10% урона отравления на время боя
   Characters.Pers.poison_damage += 10

def regeneration():
   # проверка игрока на регенерацию, применение, вывод сообщения
   if Characters.player.regeneration > 0:
      Characters.player.health_up(Characters.Pers.regeneration_value)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.regeneration_message(Characters.player.icon, MyStrings.Text.player_health.value))

   # проверка босса на регенерацию, применение, вывод сообщения   
   if Characters.boss.regeneration > 0:
      Characters.boss.health_up(Characters.Pers.regeneration_value)
      Attack_messages.attack_messages_list.append(BotMessages.Message_text.regeneration_message(Characters.boss.icon, MyStrings.Text.boss_health.value))
