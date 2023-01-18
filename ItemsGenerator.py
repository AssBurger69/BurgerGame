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

      item = Drop.Item(150)
      Drop.Item.description = DropStrings.Items.zhiguli_description()

      # интерактив с боссом Донер Кебаб
      if CharactersGenerator.boss.name == BossStrings.Doner.name:
         item.boss_iteraction_message = BossStrings.Doner.booze_interaction()
         CharactersGenerator.boss.health_up(item.value)
      
      # применение эффекта итема для других персонажей
      else:
         CharactersGenerator.player.health_up(item.value)

      
   # Сидр
   elif item_name == DropStrings.Items.sidr_name:

      item = Drop.Item(300)
      Drop.Item.description = DropStrings.Items.sidr_description()

      if CharactersGenerator.boss.name == BossStrings.Doner.name:
         item.boss_iteraction_message = BossStrings.Doner.booze_interaction()
         CharactersGenerator.boss.health_up(item.value)
      else:
         CharactersGenerator.player.health_up(item.value)
   
   
   # Балабаха Багбира
   elif item_name == DropStrings.Items.bagbeer_name:

      item = Drop.Item(500)
      Drop.Item.description = DropStrings.Items.bagbeer_description()

      if CharactersGenerator.boss.name == BossStrings.Doner.name:
         item.boss_iteraction_message = BossStrings.Doner.booze_interaction()
         CharactersGenerator.boss.health_up(item.value)
      else:
         CharactersGenerator.player.health_up(item.value)
   
   
   # Святая минералочка
   elif item_name == DropStrings.Items.mineralka_name:

      item = Drop.Item(100)
      Drop.Item.description = DropStrings.Items.mineralka_description()

      CharactersGenerator.player.regeneration_up(item.value)
   
   
   # Лезвие бритвы
   elif item_name == DropStrings.Items.lezvie_name:

      item = Drop.Item(150)
      Drop.Item.description = DropStrings.Items.lezvie_description()

      CharactersGenerator.boss.health_down(item.value)
      CharactersGenerator.boss.bleeding = True

   
   # Травмат Володи
   elif item_name == DropStrings.Items.travmat_name:

      item = Drop.Item(300)
      Drop.Item.description = DropStrings.Items.travmat_description()

      if CharactersGenerator.boss.name == BossStrings.Viv.name:
         CharactersGenerator.player.health_down(item.value)
         CharactersGenerator.player.bleeding = True
         item.boss_iteraction_message = BossStrings.Viv.travmat_interaction()

      else:
         CharactersGenerator.boss.health_down(item.value)
         CharactersGenerator.boss.bleeding = True

   
   # 2.5 литровка кока-колы
   elif item_name == DropStrings.Items.cola_name:

      item = Drop.Item(500)
      Drop.Item.description = DropStrings.Items.cola_description()

      if CharactersGenerator.boss.name == BossStrings.Doner.name:
         CharactersGenerator.player.health_down(item.value)
         CharactersGenerator.boss.health_down(item.value)
         item.boss_iteraction_message = BossStrings.Doner.cola_interaction()

      else:
         CharactersGenerator.boss.health_down(item.value)

   
   # Потный носок
   elif item_name == DropStrings.Items.sick_sock_name:

      item = Drop.Item(100)
      Drop.Item.description = DropStrings.Items.sick_sock_description()

      if CharactersGenerator.boss.name == BossStrings.Doner.name:
         item.boss_iteraction_message = BossStrings.Doner.sock_interaction()
         CharactersGenerator.boss.health_up(item.value)
         CharactersGenerator.boss.regeneration_up(item.value)

      else:
         CharactersGenerator.boss.health_down(item.value)
         CharactersGenerator.boss.poison = True


   # Блевотный харчок
   elif item_name == DropStrings.Items.harchok_name:

      item = Drop.Item(200)
      Drop.Item.description = DropStrings.Items.harchok_description()

      if CharactersGenerator.boss.name == BossStrings.Doner.name:
         CharactersGenerator.boss.health_up(item.value)
         CharactersGenerator.boss.regeneration_up(item.value)

      else:
         CharactersGenerator.boss.health_down(item.value)
         CharactersGenerator.boss.poison = True


   # Рампаг
   elif item_name == DropStrings.Items.rampag_name:

      item = Drop.Item(1)
      Drop.Item.description = DropStrings.Items.rampag_description()

      if CharactersGenerator.boss.name == BossStrings.Doner.name:
         item.boss_iteraction_message = BossStrings.Doner.rampag_interaction
         CharactersGenerator.boss.health = 0

      else:
         CharactersGenerator.boss.stan_timer = 1


   # Золотые ролексы
   elif item_name == DropStrings.Items.rolex_name:

      item = Drop.Item(0)
      Drop.Item.description = DropStrings.Items.rolex_description

      CharactersGenerator.player.cooldown = item.value


   # Вакцина
   elif item_name == DropStrings.Items.vaccine_name:

      item = Drop.Item(0)
      Drop.Item.description = DropStrings.Items.vaccine_description()

      CharactersGenerator.player.poison = False
      CharactersGenerator.player.bleeding = False


   # Шига
   elif item_name == DropStrings.Items.shiga_name:

      item = Drop.Item(30)

      shiga_items_interaction_list = [DropStrings.Buffs.sochnik_name, DropStrings.Buffs.dubai_name, 
                                    DropStrings.Buffs.dron_meat_name, DropStrings.Buffs.pizza5_name]

      cross_check = [x for x in shiga_items_interaction_list if x in CharactersGenerator.player.all_items]

      if len(cross_check) == 0:
         CharactersGenerator.player.health_down_procent(item.value)
         CharactersGenerator.player.damage_up_procent(item.value)
         Drop.Item.description = DropStrings.Items.shiga_bad_effect_description()
         
      elif len(cross_check) > 0:
         CharactersGenerator.player.health_up_procent(item.value)
         CharactersGenerator.player.damage_up_procent(item.value)
         Drop.Item.description = DropStrings.Items.shiga_good_effect_description()


   # Мадам
   elif item_name == DropStrings.Items.madam_name:

      item = Drop.Item(50)
      Drop.Item.description = DropStrings.Items.madam_description()

      CharactersGenerator.boss.damage_down_procent(item.value)