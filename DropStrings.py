import Drop
import GameStrings
import BuffsGenerator

class Buffs():
   
   def bratishki_hello():
      return '{0}\n+{1}{2}'.format('Сядь браток, попей улун молочный, он тебя подъюлит', 
                                    Drop.Buff.bratishki_health_up_value, GameStrings.Icons.player_health)
   
   sochnik_name = 'Сочник со сгухой'
   def sochnik_description():
      return '{0}\n+{1}%{2}'.format('Сгущено-вареное блаженство', 
                                    BuffsGenerator.buff.health, GameStrings.Icons.player_health)

   dubai_name = 'Дубайский шаурмец'
   dubai_description = 'Неизменная классика\n+30%❤️'
   dron_meat_name = 'Мясо Андрея'
   dron_meat_description = 'Держи его по-дальше от Дрона\n+40%❤️'
   pizza5_name = '5 пицц'
   pizza5_description = 'Промкод на 5 пицц со скидкой 50%\n+50%❤️'
   guitar_name = 'Гитара'
   guitar__description = 'Теперь ты - Рокер\n+15%⚔️'
   bashkerme_name = 'Башкерме взрывай'
   bashkerme_description = 'Баааашкермееее!\n+25%⚔️'
   pika_name = 'Пика точеная'
   pika_description = 'Ну хоть не хуй дроченый\n+30%⚔️'
   dildo_name = 'Огромный дилдак'
   dildo_description = 'В умелых руках дает\n+50%⚔️'
   everlast_name = 'Костюм Эверласт'
   everlast_description = 'Костюм Дани Эверласта, легенды миксфайта!\n+10%❤️\n+10%⚔️'
   marki_name = 'Почтовые марки'
   marki_description = 'Ты смог уломать ребят на почтовые отправления!\n+20%❤️\n+20%⚔️'
   limon_name = 'Лимонная голодовочка'
   limon_description = '24-часовая голодовка с братишками!\n-30%❤️\n+50%⚔️\n+5%💥'
   chess_name = 'Сыграть в шахматы'
   chess_description = 'Не важно проиграл ты или да\n+5%💥'
   vargan_name = 'Поиграть на варгане'
   vargan_description = 'Хорошая работа ртом и языком, дружище\n+10%💥'
   choops_name = 'Черный чупа чупс'
   choops_description = 'Навык отсоса повышен!\n+10%🦇'
   shiva_bless_name = 'Благословение Шивы'
   shiva_bless_description = 'Великая Шива благоволит тебе воин!\n+50%⚔️\n+15%💥'
   makar_bless_name = 'Благословение Макара'
   makar_bless_description = 'Святейший Король Макар снизошел на тебя!\n+30%❤️\n+30%⚔️\n+5%💥'

   buff_list = [sochnik_name, dubai_name, dron_meat_name, pizza5_name, guitar_name, bashkerme_name, pika_name,
               dildo_name, everlast_name, marki_name, limon_name, chess_name, shiva_bless_name, makar_bless_name,
               vargan_name, choops_name]



class Items():
   stas_shop_description = 'Стас тебя угостил чем-то мощным, чувствуешь себя сильнее! Давай глянем что он там еще наворовал\n+50⚔️'

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