# модуль со всеми строками касательно магазинов и предметов

import Drop
import GameStrings
import BuffsGenerator
import ItemsGenerator
import CharactersGenerator

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
                                                      BuffsGenerator.buff.critical_chance, 
                                                      GameStrings.Icons.critical_chance)
      
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
                                                      BuffsGenerator.buff.critical_chance, 
                                                      GameStrings.Icons.critical_chance)

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
   def zhiguli_description():
      return '{0}\n+{1}{2}'.format('Для истинных ценителей',
                                    ItemsGenerator.item.value, 
                                    GameStrings.Icons.player_health)
   
   sidr_name = 'Сидр'
   def sidr_description():
      return '{0}\n+{1}{2}'.format('Питерская эстетика',
                                    ItemsGenerator.item.value, 
                                    GameStrings.Icons.player_health)
   
   bagbeer_name = 'Балабаха Багбира'
   def bagbeer_description():
      return '{0}\n+{1}{2}'.format('Со вкусом молодости',
                                    ItemsGenerator.item.value, 
                                    GameStrings.Icons.player_health)
   
   mineralka_name = 'Святая минералочка'
   def mineralka_description():
      return '{0}\n+{1}{2}{3}'.format('Освежающий глоток придал тебе сил', 
                                       ItemsGenerator.item.value, 
                                       GameStrings.Icons.player_health, 
                                       GameStrings.Icons.regeneration)
   
   lezvie_name = 'Лезвия бритвы'
   def lezvie_description():
      return '{0}\n-{1}{2}{3}'.format('Бросок в глаз! Враг травмирован', 
                                       ItemsGenerator.item.value, 
                                       GameStrings.Icons.boss_health, 
                                       GameStrings.Icons.bleeding)
   
   travmat_name = 'Травмат Володи'
   def travmat_description():
      return '{0}\n-{1}{2}{3}'.format('Документы должны быть всегда с собой', 
                                       ItemsGenerator.item.value, 
                                       GameStrings.Icons.boss_health, 
                                       GameStrings.Icons.bleeding)
   
   cola_name = '2.5-литровка Колы'
   def cola_description():
      return '{0}\n{1}-{2}{3}'.format('Грозное оружие судного нового года',
                                       GameStrings.Icons.boss,
                                       ItemsGenerator.item.value,
                                       GameStrings.Icons.boss_health)
   
   sick_sock_name = 'Потный носок'
   def sick_sock_description():
      return '{0}\n-{1}{2}{3}'.format('Противник поймал твой носок лицом',
                                       ItemsGenerator.item.value,
                                       GameStrings.Icons.boss_health,
                                       GameStrings.Icons.poison)
   
   harchok_name = 'Блевотный харчок'
   def harchok_description():
      return '{0}\n-{1}{2}{3}'.format('Такого и врагу не пожелаешь',
                                       ItemsGenerator.item.value,
                                       GameStrings.Icons.boss_health,
                                       GameStrings.Icons.poison)
   
   rampag_name = 'Рампаг'
   def rampag_description():
      return '{0}\n{1}+{2}'.format('Удар Рампагом! Враг в отрубе', 
                                    CharactersGenerator.boss.icon, 
                                    GameStrings.Icons.stan)

   rolex_name = 'Золотые Ролексы'
   rolex_description = 'Дороговаты, зато кулдаун скилла сбросили'

   vaccine_name = 'Вакцина'
   def vaccine_description():
      return '{0}\n{1}{2}'.format('Лечит от всех твоих недугов', 
                                 GameStrings.Icons.bleeding, 
                                 GameStrings.Icons.poison)

   shiga_name = 'Шига'
   def shiga_bad_effect_description():
      return '{0}\n-{1}%{2}\n+{3}%{4}'.format('Душисто залетела, но теперь ты голоден', 
                                                ItemsGenerator.item.value, 
                                                GameStrings.Icons.player_health, 
                                                GameStrings.Icons.damage)
   def shiga_good_effect_description():
      return '{0}\n+{1}%{2}\n+{3}%{4}'.format('Душисто залетела, а еда спасла тебя от голода', 
                                                ItemsGenerator.item.value, 
                                                GameStrings.Icons.player_health, 
                                                GameStrings.Icons.damage)                                

   madam_name = 'Мадам'
   def madam_description():
      return '{0}\n-{1}%{2}'.format('Мадам умиротворяет всех вокруг тебя', 
                                    ItemsGenerator.item.value, 
                                    GameStrings.Icons.damage)

   item_list = [zhiguli_name, sidr_name, bagbeer_name, mineralka_name, 
               lezvie_name, travmat_name, cola_name, sick_sock_name, 
               harchok_name, rampag_name, rolex_name, vaccine_name, 
               shiga_name, madam_name]