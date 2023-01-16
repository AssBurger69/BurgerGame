# модуль создания объектов баффов

import DropStrings
import Drop
import CharactersGenerator

def bratishki_enter(buff_name):
   # создание экземпляра баффа с данными характеристиками:
   # влияние на здоровье, влияние на урон, 
   # влияние на шанс критической атаки, влияние на шанс уклонения, 
   # влияние на вампиризм, описание баффа

   global buff

   # удаление выбранного баффа из общего пула баффов
   DropStrings.Buffs.buff_list.remove(buff_name)
   
   # Сочник со сгущенкой
   if buff_name == DropStrings.Buffs.sochnik_name:
      buff = Drop.Buff(20, 0, 0, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.sochnik_description()
      CharactersGenerator.player.health_up_procent(buff.health)
   
   # Дубайский шаурмец
   elif buff_name == DropStrings.Buffs.dubai_name:
      buff = Drop.Buff(30, 0, 0, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.dubai_description()
      CharactersGenerator.player.health_up_procent(buff.health)

   # Мясо Андрея
   elif buff_name == DropStrings.Buffs.dron_meat_name:
      buff = Drop.Buff(40, 0, 0, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.dron_meat_description()
      CharactersGenerator.player.health_up_procent(buff.health)

   # 5 пицц
   elif buff_name == DropStrings.Buffs.pizza5_name:
      buff = Drop.Buff(50, 0, 0, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.pizza5_description()
      CharactersGenerator.player.health_up_procent(buff.health)

   # Гитара
   elif buff_name == DropStrings.Buffs.guitar_name:
      buff = Drop.Buff(0, 15, 0, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.guitar__description()
      CharactersGenerator.player.damage_up_procent(buff.damage)

   # Башкерме взрывай
   elif buff_name == DropStrings.Buffs.bashkerme_name:
      buff = Drop.Buff(0, 25, 0, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.bashkerme_description()
      CharactersGenerator.player.damage_up_procent(buff.damage)

   # Пика точеная
   elif buff_name == DropStrings.Buffs.pika_name:
      buff = Drop.Buff(0, 30, 0, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.pika_description()
      CharactersGenerator.player.damage_up_procent(buff.damage)

   # Огромный дилдак
   elif buff_name == DropStrings.Buffs.dildo_name:
      buff = Drop.Buff(0, 50, 0, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.dildo_description()
      CharactersGenerator.player.damage_up_procent(buff.damage)
   
   # Костюм Эверласт
   elif buff_name == DropStrings.Buffs.everlast_name:
      buff = Drop.Buff(10, 10, 0, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.everlast_description()
      CharactersGenerator.player.health_up_procent(buff.health)
      CharactersGenerator.player.damage_up_procent(buff.damage)

   # Почтовые марки
   elif buff_name == DropStrings.Buffs.marki_name:
      buff = Drop.Buff(20, 20, 0, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.marki_description()
      CharactersGenerator.player.health_up_procent(buff.health)
      CharactersGenerator.player.damage_up_procent(buff.damage)

   # Лимонная голодовочка
   elif buff_name == DropStrings.Buffs.limon_name:
      buff = Drop.Buff(30, 50, 5, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.limon_description()
      CharactersGenerator.player.health_down_procent(buff.health)
      CharactersGenerator.player.damage_up_procent(buff.damage)
      CharactersGenerator.player.critical_chance_up(buff.critical_chance)

   # Поиграть в шахматы
   elif buff_name == DropStrings.Buffs.chess_name:
      buff = Drop.Buff(0, 0, 5, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.chess_description()
      CharactersGenerator.player.critical_chance_up(buff.critical_chance)
   
   # Поиграть на варгане
   elif buff_name == DropStrings.Buffs.vargan_name:
      buff = Drop.Buff(0, 0, 10, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.vargan_description()
      CharactersGenerator.player.critical_chance_up(buff.critical_chance)

   # Черный чупа-чупс
   elif buff_name == DropStrings.Buffs.choops_name:
      buff = Drop.Buff(0, 0, 0, 0, 10)
      Drop.Buff.description = DropStrings.Buffs.choops_description()
      CharactersGenerator.player.lifesteal_up(buff.lifesteal)

   # Благословение Шивы
   elif buff_name == DropStrings.Buffs.shiva_bless_name:
      buff = Drop.Buff(0, 50, 15, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.shiva_bless_description()
      CharactersGenerator.player.damage_up_procent(buff.damage)
      CharactersGenerator.player.critical_chance_up(buff.critical_chance)

   # Благословение Макара
   elif buff_name == DropStrings.Buffs.makar_bless_name:
      buff = Drop.Buff(30, 30, 10, 0, 0)
      Drop.Buff.description = DropStrings.Buffs.makar_bless_description()
      CharactersGenerator.player.health_up_procent(buff.health)
      CharactersGenerator.player.damage_up_procent(buff.damage)
      CharactersGenerator.player.critical_chance_up(buff.critical_chance)

   # добавление имени баффа в список набранных баффов игроком за время игры
   if buff_name not in CharactersGenerator.player.all_items:
      CharactersGenerator.player.all_items.append(buff_name)
