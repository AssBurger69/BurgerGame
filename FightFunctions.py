import random
import Characters
import PlayerStrings
import BossStrings
import DropStrings
import CharactersGenerator
import InteractionParameters
import FightCycle
import FightStrings

class BossList():
   list_easy = [BossStrings.Palich.name, BossStrings.Chaikovskii.name, 
               BossStrings.Viv.name, BossStrings.Sasha.name, BossStrings.Tvar.name, 
               BossStrings.Randomich.name, BossStrings.Kitty.name]
   list_medium = [BossStrings.Inkvisizia.name, BossStrings.DocLeha.name, 
                  BossStrings.DrunkLeha.name, BossStrings.Mel.name, 
                  BossStrings.Redhead.name, BossStrings.Sledovatel.name]
   list_hard = [BossStrings.Doner.name, BossStrings.BlackStas.name, 
               BossStrings.Dron.name, BossStrings.Glad.name, BossStrings.Shiva.name]

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
   # активация способности босса до боя
   global prelude_skill_message
   
   prelude_skill_message = False

   # Палыч
   if boss_name == BossStrings.Palich.name:
      CharactersGenerator.player.silence = True
      prelude_skill_message = BossStrings.Palich.prelude_skill

   # Рыжий
   elif boss_name == BossStrings.Redhead.name:
      CharactersGenerator.player.poison = True
      prelude_skill_message = BossStrings.Redhead.prelude_skill

   # Следователь
   elif boss_name == BossStrings.Sledovatel.name:
      drugs = DropStrings.Buffs.marki_name, \
               DropStrings.Items.madam_name, \
                  DropStrings.Items.shiga_name

      cross_check = [x for x in drugs if x in CharactersGenerator.player.all_items]
      # снижение урона игрока, если его больше 500
      if CharactersGenerator.player.damage > 500:
         CharactersGenerator.player.damage_down_procent \
            (InteractionParameters.Boss.sledovatel_damage_down)
         prelude_skill_message = BossStrings.Sledovatel.damage_down_skill()

      # увеличение накопительной способности босса при заданных условиях
      if CharactersGenerator.player.mitya_elexir_count > 0 or len(cross_check) > 0:
         CharactersGenerator.player.police_wanted += \
            InteractionParameters.Boss.sledovatel_drugs
         prelude_skill_message += '\n' + BossStrings.Sledovatel.drugs_check()


   elif boss_name == BossStrings.Dron.name:
      CharactersGenerator.boss.skill_meter_level += \
         len(CharactersGenerator.player.all_items) * 5
      prelude_skill_message = BossStrings.Dron.bratishki_interaction()
      if DropStrings.Buffs.dron_meat_name in CharactersGenerator.player.all_items:
         CharactersGenerator.boss.skill_meter_level += \
            CharactersGenerator.boss.skill_meter_level_up
         prelude_skill_message += '\n' + BossStrings.Dron.dron_meat_interaction()

   elif boss_name == BossStrings.Doner.name and \
         DropStrings.Buffs.everlast_name in CharactersGenerator.player.all_items:
      CharactersGenerator.boss.health_up_procent(InteractionParameters.Boss.doner_everlast)
      CharactersGenerator.boss.damage_up_procent(InteractionParameters.Boss.doner_everlast)
      prelude_skill_message = BossStrings.Doner.everlast_interaction()

   elif boss_name == BossStrings.BlackStas.name and \
         CharactersGenerator.player.name == PlayerStrings.Mitya.name:
      CharactersGenerator.boss.damage_up(CharactersGenerator.player.mitya_elexir_count * 
                                          CharactersGenerator.player.mitya_damage_up_skill_value)
      prelude_skill_message = BossStrings.BlackStas.mitya_interaction

def chance(x):
   # генератор вероятности
   chance = random.randint(1, 100) in range(1, x)
   return chance

def bleeding():
   # проверка игрока на кровотечение и отсутствие иммунитета к нему, применение кровотечения
   if CharactersGenerator.player.bleeding == True and \
      CharactersGenerator.player.immunity == False:
      CharactersGenerator.player.health_down(Characters.Pers.bleeding_damage)
      FightCycle.Attack_messages.messages_pool.append(FightStrings.Banners.bleeding(True))
      
   # проверка босса на кровотечение, его применение и вывод сообщения
   if CharactersGenerator.boss.bleeding == True:
      CharactersGenerator.boss.health_down(Characters.Pers.bleeding_damage)
      FightCycle.Attack_messages.messages_pool.append(FightStrings.Banners.bleeding(False))

def poison():
   # проверка игрока на отравление и отсутствие иммунитета к нему, применение, вывод сообщения
   if CharactersGenerator.player.poison == True and \
      CharactersGenerator.player.immunity == False:
      CharactersGenerator.player.health_down_procent(Characters.Pers.poison_damage)
      FightCycle.Attack_messages.messages_pool.append(FightStrings.Banners.poison(True))

   # проверка босса на отравление, применение, вывод сообщения
   if CharactersGenerator.boss.poison == True:
      CharactersGenerator.boss.health_down_procent(Characters.Pers.poison_damage)
      FightCycle.Attack_messages.messages_pool.append(FightStrings.Banners.poison(False))

   # увеличение на 10% урона отравления на время боя
   Characters.Pers.poison_damage += 10

def regeneration():
   # проверка игрока на регенерацию, применение, вывод сообщения
   if CharactersGenerator.player.regeneration > 0:
      CharactersGenerator.player.health_up(Characters.Pers.regeneration_value)
      FightCycle.Attack_messages.messages_pool.append(FightStrings.Banners.regeneration(True))

   # проверка босса на регенерацию, применение, вывод сообщения   
   if CharactersGenerator.boss.regeneration > 0:
      CharactersGenerator.boss.health_up(Characters.Pers.regeneration_value)
      FightCycle.Attack_messages.messages_pool.append(FightStrings.Banners.regeneration(False))

def lifesteal():
   global lifesteal_heal
   # проверка на вампиризм игрока, применение эффекта
   if CharactersGenerator.player.lifesteal > 0:
      lifesteal_heal = FightCycle.player_attack_damage * \
                        CharactersGenerator.player.lifesteal // 100
      CharactersGenerator.player.health_up(lifesteal_heal)
      FightCycle.Attack_messages.messages_pool.append(FightStrings.Banners.lifesteal())

def boss_returnal():
   global returnal_damage
   # проверка на обратку босса, применение эффекта
   if CharactersGenerator.boss.returnal_value > 0:
      returnal_damage = FightCycle.player_attack_damage * \
                        CharactersGenerator.boss.returnal_value // 100
      CharactersGenerator.player.health_down(returnal_damage)
      FightCycle.Attack_messages.messages_pool.append(FightStrings.Banners.returnal(False))