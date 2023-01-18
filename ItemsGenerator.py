import Drop
import CharactersGenerator
import DropStrings
import BossStrings

def stas_enter(item_name):
   # если игрок выбрал магазин Серого Стаса, итем добавляется в список итемов игрока
   # и удаляется из общего списка итемов, предотвращая повторение во время игры
   CharactersGenerator.player.item = item_name
   DropStrings.Items.item_list.remove(item_name)

def item_activation(item_name):
   global item

   # Жигули
   if item_name == DropStrings.Items.zhiguli_name:

      item = Drop.Item(150, DropStrings.Items.zhiguli_description)

      # интерактив с боссом Донер Кебаб
      if CharactersGenerator.boss.name == BossStrings.Doner.name:
         item.boss_iteraction_message = BossStrings.Doner.booze_interaction()
         CharactersGenerator.boss.health_up(item.value)
      
      # применение эффекта итема для других персонажей
      else:
         CharactersGenerator.player.health_up(item.value)


   elif item_name == DropStrings.Items.sidr_name:
      item = Drop.Item(300, DropStrings.Items.sidr_description)
      if CharactersGenerator.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_booze_text.value
         CharactersGenerator.boss.health_up(item.value)
      else:
         CharactersGenerator.player.health_up(item.value)

   elif item_name == DropStrings.Items.bagbeer_name:
      item = Drop.Item(500, DropStrings.Items.bagbeer_description)
      if CharactersGenerator.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_booze_text.value
         CharactersGenerator.boss.health_up(item.value)
      else:
         CharactersGenerator.player.health_up(item.value)

   elif item_name == DropStrings.Items.mineralka_name:
      item = Drop.Item(100, DropStrings.Items.mineralka_description)
      CharactersGenerator.player.regeneration_up(item.value)

   elif item_name == MyStrings.Text.lezvie_name.value:
      item = Drop.Item(150, MyStrings.Text.lezvie_description.value)
      CharactersGenerator.boss.health_down(item.value)
      CharactersGenerator.boss.bleeding = True

   elif item_name == MyStrings.Text.travmat_name.value:
      item = Drop.Item(300, MyStrings.Text.travmat_description.value)
      if CharactersGenerator.boss.name == MyStrings.Text.viv_name.value:
         CharactersGenerator.player.health_down(item.value)
         CharactersGenerator.player.bleeding = True
         item.boss_iteraction_message = MyStrings.Text.viv_travmat_text.value
      else:
         CharactersGenerator.boss.health_down(item.value)
         CharactersGenerator.boss.bleeding = True

   elif item_name == MyStrings.Text.cola_name.value:
      item = Drop.Item(500, MyStrings.Text.cola_description.value)
      if CharactersGenerator.boss.name == MyStrings.Text.doner_name.value:
         CharactersGenerator.player.health_down(item.value)
         CharactersGenerator.boss.health_down(item.value)
         item.boss_iteraction_message = MyStrings.Text.doner_cola_text.value
      else:
         CharactersGenerator.boss.health_down(item.value)

   elif item_name == MyStrings.Text.sick_sock_name.value:
      item = Drop.Item(100, MyStrings.Text.sick_sock_description.value)
      if CharactersGenerator.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_sock_text.value
         CharactersGenerator.boss.health_up(item.value)
         CharactersGenerator.boss.regeneration_up(item.value)
      else:
         CharactersGenerator.boss.health_down(item.value)
         CharactersGenerator.boss.poison = True

   elif item_name == MyStrings.Text.harchok_name.value:
      item = Drop.Item(200, MyStrings.Text.harchok_description.value)
      if CharactersGenerator.boss.name == MyStrings.Text.doner_name.value:
         CharactersGenerator.boss.health_up(item.value)
         CharactersGenerator.boss.regeneration_up(item.value)
      else:
         CharactersGenerator.boss.health_down(item.value)
         CharactersGenerator.boss.poison = True

   elif item_name == MyStrings.Text.rampag_name.value:
      item = Drop.Item(1, MyStrings.Text.rampag_description.value)
      if CharactersGenerator.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_rampag_text.value
         CharactersGenerator.boss.health = 0
      else:
         CharactersGenerator.boss.stan_timer = 1

   elif item_name == MyStrings.Text.rolex_name.value:
      item = Drop.Item(0, MyStrings.Text.rolex_description.value)
      CharactersGenerator.player.cooldown = item.value

   elif item_name == MyStrings.Text.vaccine_name.value:
      item = Drop.Item(0, MyStrings.Text.vaccine_description.value)
      CharactersGenerator.player.poison = False
      CharactersGenerator.player.bleeding = False

   elif item_name == DropStrings.Items.shiga_name:

      item = Drop.Item(30, False)

      shiga_items_interaction_list = [DropStrings.Buffs.sochnik_name, DropStrings.Buffs.dubai_name, 
                              DropStrings.Buffs.dron_meat_name, DropStrings.Buffs.pizza5_name]

      cross_check = [x for x in shiga_items_interaction_list if x in CharactersGenerator.player.all_items]

      if len(cross_check) == 0:
         CharactersGenerator.player.health_down_procent(item.value)
         CharactersGenerator.player.damage_up_procent(item.value)
         item.description = DropStrings.Items.shiga_bad_effect_description
         
      elif len(cross_check) > 0:
         CharactersGenerator.player.health_up_procent(item.value)
         CharactersGenerator.player.damage_up_procent(item.value)
         item.description = DropStrings.Items.shiga_good_effect_description

   elif item_name == MyStrings.Text.madam_name.value:
      item = Drop.Item(50, MyStrings.Text.madam_description.value)
      CharactersGenerator.boss.damage_down_procent(item.value)