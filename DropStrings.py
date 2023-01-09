import Drop
import GameStrings
import BuffsGenerator

class Buffs():

   bratishki_buff_offer = 'Для тебя ничего не жалко! Угощайся'
   bratishki_bye = 'Заходи еще, всегда тебе рады!'
   
   def bratishki_hello():
      return '{0}\n+{1}{2}'.format('Сядь браток, попей улун молочный, он тебя подъюлит', 
                                    Drop.Buff.bratishki_health_up_value, GameStrings.Icons.player_health)
   
   sochnik_name = 'Сочник со сгухой'
   def sochnik_description():
      return '{0}\n+{1}%{2}'.format('Сгущено-вареное блаженство', 
                                    BuffsGenerator.buff.health, GameStrings.Icons.player_health)

   dubai_name = 'Дубайский шаурмец'
   def dubai_description():
      return '{0}\n+{1}%{2}'.format('Неизменная классика', 
                                    BuffsGenerator.buff.health, GameStrings.Icons.player_health)
      
   dron_meat_name = 'Мясо Андрея'
   def dron_meat_description():
      return '{0}\n+{1}%{2}'.format('Держи его по-дальше от Дрона', 
                                    BuffsGenerator.buff.health, GameStrings.Icons.player_health)
      
   pizza5_name = '5 пицц'
   def pizza5_description():
      return '{0}\n+{1}%{2}'.format('Промкод на 5 пицц со скидкой 50%', 
                                    BuffsGenerator.buff.health, GameStrings.Icons.player_health)
      
   guitar_name = 'Гитара'
   def guitar__description():
      return '{0}\n+{1}%{2}'.format('Теперь ты - Рокер', 
                                    BuffsGenerator.buff.damage, GameStrings.Icons.damage)
      
   bashkerme_name = 'Башкерме взрывай'
   def bashkerme_description():
      return '{0}\n+{1}%{2}'.format('Баааашкермееее!', 
                                    BuffsGenerator.buff.damage, GameStrings.Icons.damage)
      
   pika_name = 'Пика точеная'
   def pika_description():
      return '{0}\n+{1}%{2}'.format('Ну хоть не хуй дроченый', 
                                    BuffsGenerator.buff.damage, GameStrings.Icons.damage)
      
   dildo_name = 'Огромный дилдак'
   def dildo_description():
      return '{0}\n+{1}%{2}'.format('В умелых руках дает', 
                                    BuffsGenerator.buff.damage, GameStrings.Icons.damage)
      
   everlast_name = 'Костюм Эверласт'
   def everlast_description():
      return '{0}\n+{1}%{2}\n+{3}%{4}'.format('Костюм Дани Эверласта, легенды миксфайта!', 
                                             BuffsGenerator.buff.health, GameStrings.Icons.player_health,
                                             BuffsGenerator.buff.damage, GameStrings.Icons.damage)
      
   marki_name = 'Почтовые марки'
   def marki_description():
      return '{0}\n+{1}%{2}\n+{3}%{4}'.format('Ты смог уломать ребят на почтовые отправления!', 
                                             BuffsGenerator.buff.health, GameStrings.Icons.player_health,
                                             BuffsGenerator.buff.damage, GameStrings.Icons.damage)
      
   limon_name = 'Лимонная голодовочка'
   def limon_description():
      return '{0}\n-{1}%{2}\n+{3}%{4}\n+{5}%{6}'.format('24-часовая голодовка с братишками!', 
                                                      BuffsGenerator.buff.health, GameStrings.Icons.player_health,
                                                      BuffsGenerator.buff.damage, GameStrings.Icons.damage,
                                                      BuffsGenerator.buff.critical_chance, GameStrings.Icons.critical_chance)
      
   chess_name = 'Сыграть в шахматы'
   def chess_description():
      return '{0}\n+{1}%{2}'.format('Не важно проиграл ты или да', 
                                    BuffsGenerator.buff.critical_chance, GameStrings.Icons.critical_chance)
      
   vargan_name = 'Поиграть на варгане'
   def vargan_description():
      return '{0}\n+{1}%{2}'.format('Хорошая работа ртом и языком, дружище', 
                                    BuffsGenerator.buff.critical_chance, GameStrings.Icons.critical_chance)

   choops_name = 'Черный чупа чупс'
   def choops_description():
      return '{0}\n+{1}%{2}'.format('Навык отсоса повышен!', 
                                    BuffsGenerator.buff.lifesteal, GameStrings.Icons.lifesteal)

   shiva_bless_name = 'Благословение Шивы'
   def shiva_bless_description():
      return '{0}\n+{1}%{2}\n+{3}%{4}'.format('Великая Шива благоволит тебе воин!', 
                                             BuffsGenerator.buff.damage, GameStrings.Icons.damage,
                                             BuffsGenerator.buff.critical_chance, GameStrings.Icons.critical_chance)

   makar_bless_name = 'Благословение Макара'
   def makar_bless_description():
      return '{0}\n+{1}%{2}\n+{3}%{4}\n+{5}%{6}'.format('Святейший Король Макар снизошел на тебя!', 
                                                      BuffsGenerator.buff.health, GameStrings.Icons.player_health,
                                                      BuffsGenerator.buff.damage, GameStrings.Icons.damage,
                                                      BuffsGenerator.buff.critical_chance, GameStrings.Icons.critical_chance)

   buff_list = [sochnik_name, dubai_name, dron_meat_name, pizza5_name, guitar_name, bashkerme_name, pika_name,
               dildo_name, everlast_name, marki_name, limon_name, chess_name, shiva_bless_name, makar_bless_name,
               vargan_name, choops_name]



class Items():

   stas_item_offer = 'Забирку делай быстрей, мразь'
   stas_bye = 'Купки! Купки!'

   def stas_hello():
      return '{0}\n+{1}{2}'.format('Здорова батя, будешь нет эту хуйню? На держи', 
                                    Drop.Item.stas_damage_up_value, GameStrings.Icons.damage)

   zhiguli_name = 'Жигули'
   zhiguli_description = 'Для истинных ценителей\n+150❤️'
   sidr_name = 'Сидр'
   sidr_description = 'Питерская эстетика\n+300❤️'
   bagbeer_name = 'Балабаха Багбира'
   bagbeer_description = 'Со вкусом молодости\n+500❤️'
   mineralka_name = 'Святая минералочка'
   mineralka_description = 'Освежающий глоток придал тебе сил\n+100❤️💕'
   lezvie_name = 'Лезвия бритвы'
   lezvie_description = 'Бросок в глаз! Враг травмирован\n-150🖤🩸'
   travmat_name = 'Травмат Володи'
   travmat_description = 'Документы должны быть всегда с собой\n-300🖤🩸'
   cola_name = '2.5-литровка Колы'
   cola_description = 'Грозное оружие судного нового года\n👿-500🖤'
   sick_sock_name = 'Потный носок'
   sick_sock_description = 'Противник поймал твой носок лицом\n-100🖤🦠'
   harchok_name = 'Блевотный харчок'
   harchok_description = 'Такого и врагу не пожелаешь\n-200🖤🦠'
   rampag_name = 'Рампаг'
   rampag_description = 'Удар Рампагом! Враг в отрубе\n👿 + 💤'
   rolex_name = 'Золотые Ролексы'
   rolex_description = 'Дороговаты, зато кулдаун скилла сбросили'
   vaccine_name = 'Вакцина'
   vaccine_description = 'Лечит от всех твоих недугов\n❌🩸🦠❌'
   shiga_name = 'Шига'
   shiga_debuff_description = 'Душисто залетела, но теперь ты голоден\n-20%❤️\n+20%⚔️'
   shiga_buff_description = 'Душисто залетела, а еда спасла тебя от голода\n+20%❤️\n+20%⚔️'
   madam_name = 'Мадам'
   madam_description = 'Мадам умиротворяет всех вокруг тебя\n-50%⚔️'

   item_list = ['Жигули', 'Лезвия бритвы', 'Потный носок', 'Шига', 'Святая минералочка', 'Золотые Ролексы', 'Сидр',
                  '2.5-литровка Колы', 'Блевотный харчок', 'Мадам', 'Рампаг', 'Вакцина', 'Балабаха Багбира', 'Травмат Володи']