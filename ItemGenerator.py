def item_activation(item_name):
   global item

   if item_name == MyStrings.Text.zhiguli_name.value:
      item = Item(150, MyStrings.Text.zhiguli_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_booze_text.value
         Characters.boss.health_up(item.value)
      else:
         Characters.player.health_up(item.value)

   elif item_name == MyStrings.Text.sidr_name.value:
      item = Item(300, MyStrings.Text.sidr_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_booze_text.value
         Characters.boss.health_up(item.value)
      else:
         Characters.player.health_up(item.value)

   elif item_name == MyStrings.Text.bagbeer_name.value:
      item = Item(500, MyStrings.Text.bagbeer_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_booze_text.value
         Characters.boss.health_up(item.value)
      else:
         Characters.player.health_up(item.value)

   elif item_name == MyStrings.Text.mineralka_name.value:
      item - Item(100, MyStrings.Text.mineralka_description.value)
      Characters.player.regeneration_up(item.value)

   elif item_name == MyStrings.Text.lezvie_name.value:
      item = Item(150, MyStrings.Text.lezvie_description.value)
      Characters.boss.health_down(item.value)
      Characters.boss.bleeding = True

   elif item_name == MyStrings.Text.travmat_name.value:
      item = Item(300, MyStrings.Text.travmat_description.value)
      if Characters.boss.name == MyStrings.Text.viv_name.value:
         Characters.player.health_down(item.value)
         Characters.player.bleeding = True
         item.boss_iteraction_message = MyStrings.Text.viv_travmat_text.value
      else:
         Characters.boss.health_down(item.value)
         Characters.boss.bleeding = True

   elif item_name == MyStrings.Text.cola_name.value:
      item = Item(500, MyStrings.Text.cola_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         Characters.player.health_down(item.value)
         Characters.boss.health_down(item.value)
         item.boss_iteraction_message = MyStrings.Text.doner_cola_text.value
      else:
         Characters.boss.health_down(item.value)

   elif item_name == MyStrings.Text.sick_sock_name.value:
      item = Item(100, MyStrings.Text.sick_sock_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_sock_text.value
         Characters.boss.health_up(item.value)
         Characters.boss.regeneration_up(item.value)
      else:
         Characters.boss.health_down(item.value)
         Characters.boss.poison = True

   elif item_name == MyStrings.Text.harchok_name.value:
      item = Item(200, MyStrings.Text.harchok_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         Characters.boss.health_up(item.value)
         Characters.boss.regeneration_up(item.value)
      else:
         Characters.boss.health_down(item.value)
         Characters.boss.poison = True

   elif item_name == MyStrings.Text.rampag_name.value:
      item = Item(1, MyStrings.Text.rampag_description.value)
      if Characters.boss.name == MyStrings.Text.doner_name.value:
         item.boss_iteraction_message = MyStrings.Text.doner_rampag_text.value
         Characters.boss.health = 0
      else:
         Characters.boss.stan_timer = 1

   elif item_name == MyStrings.Text.rolex_name.value:
      item = Item(0, MyStrings.Text.rolex_description.value)
      Characters.player.cooldown = item.value

   elif item_name == MyStrings.Text.vaccine_name.value:
      item = Item(0, MyStrings.Text.vaccine_description.value)
      Characters.player.poison = False
      Characters.player.bleeding = False

   elif item_name == MyStrings.Text.shiga_name.value:
      item = Item(30, False)
      foods = MyStrings.Text.sochnik_name.value, MyStrings.Text.dubai_name.value, MyStrings.Text.dron_meat_name.value, MyStrings.Text.pizza5_name.value
      cross_check = [x for x in foods if x in Characters.player.all_items]
      if len(cross_check) == 0:
         Characters.player.health_down_procent(item.value)
         Characters.player.damage_up_procent(item.value)
         item.description = MyStrings.Text.shiga_debuff_description.value
      elif len(cross_check) > 0:
         Characters.player.health_up_procent(item.value)
         Characters.player.damage_up_procent(item.value)
         item.description = MyStrings.Text.shiga_buff_description.value

   elif item_name == MyStrings.Text.madam_name.value:
      item = Item(50, MyStrings.Text.madam_description.value)
      Characters.boss.damage_down_procent(item.value)