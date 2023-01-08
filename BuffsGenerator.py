import DropStrings
import Drop
import CharactersGenerator

def bratishki_enter(buff_name):
   global buff
   DropStrings.Buffs.buff_list.remove(buff_name)
   
   if buff_name == DropStrings.Buffs.sochnik_name:
      buff = Drop.Buff(20, 0, 0, 0, 0, DropStrings.Buffs.sochnik_description())
      CharactersGenerator.player.health_up_procent(buff.health)
   
   elif buff_name == DropStrings.Buffs.dubai_name:
      buff = Drop.Buff(30, 0, 0, 0, 0, DropStrings.Buffs.dubai_description())
      CharactersGenerator.player.health_up_procent(buff.health)

   elif buff_name == DropStrings.Buffs.dron_meat_name:
      buff = Drop.Buff(40, 0, 0, 0, 0, DropStrings.Buffs.dron_meat_description())
      CharactersGenerator.player.health_up_procent(buff.health)

   elif buff_name == DropStrings.Buffs.pizza5_name:
      buff = Drop.Buff(50, 0, 0, 0, 0, DropStrings.Buffs.pizza5_description())
      CharactersGenerator.player.health_up_procent(buff.health)

   elif buff_name == DropStrings.Buffs.guitar_name:
      buff = Drop.Buff(0, 15, 0, 0, 0, DropStrings.Buffs.guitar__description())
      CharactersGenerator.player.damage_up_procent(buff.damage)

   elif buff_name == DropStrings.Buffs.bashkerme_name:
      buff = Drop.Buff(0, 25, 0, 0, 0, DropStrings.Buffs.bashkerme_description())
      CharactersGenerator.player.damage_up_procent(buff.damage)

   elif buff_name == DropStrings.Buffs.pika_name:
      buff = Drop.Buff(0, 30, 0, 0, 0, DropStrings.Buffs.pika_description())
      CharactersGenerator.player.damage_up_procent(buff.damage)

   elif buff_name == DropStrings.Buffs.dildo_name:
      buff = Drop.Buff(0, 50, 0, 0, 0, DropStrings.Buffs.dildo_description())
      CharactersGenerator.player.damage_up_procent(buff.damage)
   
   elif buff_name == DropStrings.Buffs.everlast_name:
      buff = Drop.Buff(10, 10, 0, 0, 0, DropStrings.Buffs.everlast_description())
      CharactersGenerator.player.health_up_procent(buff.health)
      CharactersGenerator.player.damage_up_procent(buff.damage)

   elif buff_name == DropStrings.Buffs.marki_name:
      buff = Drop.Buff(20, 20, 0, 0, 0, DropStrings.Buffs.marki_description())
      CharactersGenerator.player.health_up_procent(buff.health)
      CharactersGenerator.player.damage_up_procent(buff.damage)

   elif buff_name == DropStrings.Buffs.limon_name:
      buff = Drop.Buff(30, 50, 5, 0, 0, DropStrings.Buffs.limon_description())
      CharactersGenerator.player.health_down_procent(buff.health)
      CharactersGenerator.player.damage_up_procent(buff.damage)
      CharactersGenerator.player.critical_chance_up(buff.critical_chance)

   elif buff_name == DropStrings.Buffs.chess_name:
      buff = Drop.Buff(0, 0, 5, 0, 0, DropStrings.Buffs.chess_description())
      CharactersGenerator.player.critical_chance_up(buff.critical_chance)
   
   elif buff_name == DropStrings.Buffs.vargan_name:
      buff = Drop.Buff(0, 0, 10, 0, 0, DropStrings.Buffs.vargan_description())
      CharactersGenerator.player.critical_chance_up(buff.critical_chance)

   elif buff_name == DropStrings.Buffs.choops_name:
      buff = Drop.Buff(0, 0, 0, 0, 10, DropStrings.Buffs.choops_description())
      CharactersGenerator.player.lifesteal_up(buff.lifesteal)

   elif buff_name == DropStrings.Buffs.shiva_bless_name:
      buff = Drop.Buff(0, 50, 15, 0, 0, DropStrings.Buffs.shiva_bless_description())
      CharactersGenerator.player.damage_up_procent(buff.damage)
      CharactersGenerator.player.critical_chance_up(buff.critical_chance)

   elif buff_name == DropStrings.Buffs.makar_bless_name:
      buff = Drop.Buff(30, 30, 10, 0, 0, DropStrings.Buffs.makar_bless_description())
      CharactersGenerator.player.health_up_procent(buff.health)
      CharactersGenerator.player.damage_up_procent(buff.damage)
      CharactersGenerator.player.critical_chance_up(buff.critical_chance)

   if buff_name not in CharactersGenerator.player.all_items:
      CharactersGenerator.player.all_items.append(buff_name)
