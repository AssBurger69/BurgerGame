import enum

class Text(enum.Enum):
   hello_text = 'Приветствую в моем Бургерном рогалике, друг! Играй лучше на телефоне'
   char_choice_text = 'Выбери персонажа'
   give_answer_text = 'Напиши мне что-нибудь'
   ready_key_text = 'Я готов!'
   victory_button_text = 'Я молодец'
   another_char_key_text = 'Давай другого'
   char_choice_question = 'Берешь его?'
   shop_choice_text = 'Выбирай куда пойдешь'
   item_choice_text = 'Бери что-то одно'
   boss_choice_question = 'А с кем деремся?'
   location_choice_question = 'А где это я?'
   go_to_jail_button_text = 'Отсидеть'
   jail_effect_text = 'Тюрьма кардиАнально преобразила тебя! Теперь у тебя есть воровской карман'
   jail_reply_button_text = 'Спасибо'
   run_away_button_text = 'Сбежать'
   run_away_effect_text = 'Побег дело святое, но теперь ты в розыске'
   run_away_reply_button_text = 'Сам ты в розыске'
   get_fight_button_text = 'ПОГНАЛИ'
   busted_text = 'Воу воу парень, ты доигрался, милости прошу в автозак'
   attack_button_text = 'Атака'
   start_turn_text = 'Ходи, друг'
   char_stan_text = 'Не прокатит бро, ты в стане'
   char_silence_text = 'Сорян, но ты забанен'
   cooldown_text = 'Обломись, там перезарядка'
   empty_text = 'Пусто'
   empty_click_text = 'Не прокатит, друг'
   miss_text = '🛡Уворотка🛡\n'
   boss_miss_text = 'Босс пропустил твой урон\n'
   end_turn_button_text = 'Закончить ход'
   boss_police_upgrade_text = 'Босс был усилен стражами порядка'
   restart_button_text = 'ДАВАЙ ЕЩЕ РАЗОК'
   victory_game_text = '🥳Похоже ты победил. Круто🥳'
   game_over_text = '👻Увы, но ты проебал, старина👻\nНапиши мне что-нибудь и начнем сначала'
   victory_fight_text = 'Ты победил, слабина'
   stan_text = 'недееспособен'
   critical_text = 'Критический урон!'
   lifesteal_text = 'Вампирик'
   returnal_text = 'Обратка'
   char_miss_text = ' скользкий тип\n'
   ressurection_text = 'Произошла воскресуха!'
   stan_banner = '        💤Стан💤'
   bleeding_text = '🩸Кровотечение🩸'
   poison_text = '🦠Отравление🦠'
   regeneration_text = '💕Регенерация💕'
   stan_icon = '💤'
   char_health_icon = '❤️'
   boss_health_icon = '🖤'
   damage_icon = '⚔️'
   critical_chance_icon = '💥'
   regeneration_icon = '💕'
   bleeding_icon = '🩸'
   poison_icon = '🦠'
   chains_icon = '⛓'
   obida_icon = '🤬'
   boss_icon = '👿'
   lifesteal_icon = '🦇'
   returnal_icon = '🤕'
   plus = '+'
   minus = '-'

   mitya_name = 'Митя'
   mitya_skill_effect_text = '-100❤️\n+200⚔️\n🕒1 ход'
   mitya_stage25_text = 'Митя тут, как рыба в воде\n+20%❤️'
   mitya_inkvisizia_text = 'Вместо урона Митя в инквизиции становится сильнее, она не может причинить ему урон!\n+50%❤️'
   mitya_skill_button_text = 'Бахнуть элексир'
   mitya_description_text = '❤️800\n⚔️100\n💥0\nМастер отсоса жизни\nЛюбитель губительно-усиливающих эликсиров, будь с ними осторожен'
   mitya_icon = '👨‍🔬'
   sanya_name = 'Саня'
   sanya_skill_effect_text = '🖤\n🕒3 хода'
   sanya_drochilnya_text = 'Да, Саша?\n+10%💥'
   sanya_sasha_text = 'Победа над собой возвысила тебя!\n+20%❤️\n+20%⚔️\n+5%💥'
   sanya_skill_button_text = 'Кинуть ножницы'
   sanya_description_text = '❤️1000\n⚔️200\n💥30\nЭзотерический парикмахер\nМастер чистого белого неделимого броска ножницами'
   sanya_icon = '💇'
   toshik_name = 'Тошик'
   toshik_skill_effect_text = '+20%❤️\n🕒2 хода'
   toshik_molebka_text = 'Но Тошика так просто не измотаешь\n+20%❤️\n+10%⚔️'
   toshik_passive_text = 'Твое здоровье - твоя сила\n⚔️+5%❤️'
   toshik_skill_button_text = 'Сесть медитировать'
   toshik_description_text = '❤️1500\n⚔️100\n💥0\nПсайтанковый медитатор\nБольше здоровья - больше силы'
   toshik_icon = '🦹‍♂️'
   kolya_name = 'Коля'
   kolya_skill_effect_text = '⚔️\n🕒3 хода'
   kolya_bad_trip_text = 'Коля любит бэд трипы\n+300❤️\n+100⚔️'
   kolya_stage25_text = 'Коле здесь явно не место\n-20%❤️'
   kolya_skill_button_text = 'Хакнуть урон'
   kolya_description_text = '❤️1200\n⚔️100\n💥0\nХипстерский программист\nПадок на разочарование'
   kolya_icon = '👨‍💻'
   temich_name = 'Темыч'
   temich_skill_effect_text = '❤️🔄🖤\n🕒1 ход'
   temich_skill_deffect_text = 'Ой ой, Темыч запутался в своей суете\n'
   temich_bad_trip_text = 'Темыч так и не понял что был в бэде, а значит этого не было!'
   temich_skill_button_text = 'Навести суету'
   temich_description_text = '❤️800\n⚔️150\n💥0\nНетикающий суетолог\nЕсли не поймет что понес урон - значит этого не было'
   temich_icon = '🤷‍♂️'

   stas_shop_name = 'Лавка Серого Стаса'
   stas_shop_description = 'Стас тебя угостил чем-то мощным, чувствуешь себя сильнее! Давай глянем что он там еще наворовал\n+50⚔️'
   stas_bye_text = 'Хороший выбор, батя'
   bratishki_shop_name = 'Братишкино логово'
   bratishki_shop_description = 'Братишки приветсвуют тебя в своем логове! Сядь браток, попей улун молочный, он тебя подлечит\n+200❤️'
   
   sochnik_name = 'Сочник со сгухой'
   sochnik_description = 'Сгущено-вареное блаженство\n+20%❤️'
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

   palich_name = 'Палыч'
   palich_prelude_text = 'Палыч завалил твой ебалыч - скиллы и предметы не поюзать'
   palich_description = 'Раздает перманентные баны'
   chaikovskii_name = 'Чайковский'
   chaikovskii_god_city_text = 'Чайковский здесь чувствует приток самопиздатости\n+100🖤\n+50⚔️\n+10💥'
   chaikovskii_description = 'Одна святая песня воскрешает его перед порогом смерти'
   chaikovskii_ressurection_text = 'Брат! Не засыпай!'
   viv_name = 'Вив'
   viv_travmat_text = 'Володя забрал свой травмат!\n-300❤️🩸'
   viv_description = 'В конце хода наваливает бассов повышая свой урон'
   viv_end_skill_text = 'Бассы подъехали!'
   sasha_name = 'Саша Шлякин'
   sasha_bye_text = 'Саша Шлякин нападает только на самого себя, подберем тебе другого'
   sasha_description = 'Убей его и возвысь себя'
   tvar_name = 'Качаловская Тварь'
   tvar_description = 'Бить ее больно и крайне неприятно, себе хуже только сделаешь'
   randomich_name = 'Рандом Рандомыч'
   randomich_description = 'Может быть лох, а может и бог'
   kitty_name = 'Котенок-тролль'
   kitty_description = 'Вислоухий и пузатый, мурчанием вызывает бессилие, еще может закогтить тебя'
   kitty_stan_text = 'Мурлы-сна!'
   kitty_bleeding_text = 'Зацепка когтями!'
   inkvisizia_name = 'Инквизиция'
   inkvisizia_description = 'Неопытных юзеров может моментально умертвить, тут уж как повезет'
   doc_leha_name = 'Доктор Леха'
   doc_leha_description = 'Может провести вихревой удар джаггернаута своей сумкой'
   doc_leha_skill_text = 'Джагернаааааут!'
   drunk_leha_name = 'Пьяный Леха'
   drunk_leha_description = 'В конце хода накидывает еще коктейльчик, становясь опаснее'
   drunk_leha_skill_text = 'Леха бухает! Остановите его!'
   mel_name = 'Мел'
   mel_miss_text = 'Мелу похуй на твой урон'
   mel_description = 'Отсутвие гордости делает его не восприимчивым к урону, замешкаешься - зальет блазуху тебе в ухо'
   mel_end_skill_text = 'Мел залил тебе блазуху в ухо!'
   redhead_name = 'Рыжий'
   redhead_prelude_text = '🦠Рыжий потравил тебя в душу🦠'
   redhead_description = 'Находясь с ним рядом ты травишь свою жизнь, живучая падла'
   sledovatel_name = 'Следователь'
   sledovatel_drugcheck_text = '👮‍♂️: Употребляли? Тогда быстрее вас упакуем\nСтепень упаковки +50%'
   sledovatel_damage_prelude_text = 'Злоупотребление дамагом карается по закону!\n-50%⚔️'
   sledovatel_description = 'Если успеет заполнить на тебя доки - будешь упакован в тюрьму'
   sledovatel_skill_meter_text = 'Степень упаковки'
   doner_name = 'Донер Кебаб'
   doner_kolbas_text = 'Ой ой, Донер у Колбаса стал крепче\n+500🖤'
   doner_everlast_text = 'Донер спиздил твой костюм!\n+10%🖤\n+10%⚔️'
   doner_cola_text = 'Открывая твою Колу, Донер захуярил и себя, и тебя, и обои!\n-500❤️\n-500🖤'
   doner_rampag_text = 'Рампаг заходит сзади! Моментальная смерть для Донера!'
   doner_booze_text = 'Пизда твоему бухлу, Донер его выпил\n+150🖤'
   doner_sock_text = 'Не стоило травить Донера\n+100🖤💕'
   doner_harchok_text = 'Не стоило травить Донера\n+200🖤💕'
   doner_description = 'При нем лучше не бухать, травля эту мразь делает сильнее'
   black_stas_name = 'Черный Стас'
   black_stas_mitya_text = 'Стас, по-справедливости, бахает столько же эликсиров, что и Митя'
   black_stas_description = 'Правильно выбирай слова для его осадки - закинет за всю хуйню обратно'
   black_stas_returnal_text = 'Стас отразил твою хуйню'
   dron_name = 'Дрон'
   dron_bratishki_text = 'За каждый поход к братишкам\n🤬+5%'
   dron_dron_meat_text = 'А за то что ты ел мясо Андрея\n🤬+10%'
   dron_skill_text = '☠️Дрон затаил лютую обиду!☠️'
   dron_description = 'Доведешь Андрея до обиды - умрешь в его глазах'
   dron_skill_meter_text = 'Риск обиды'
   glad_name = 'Валера Гладиатор'
   glad_damage_skill_text = 'Твин-турбо гадза на минус уши'
   glad_health_up_skill_text = 'Церковная целебная гадза'
   glad_critical_up_skill_text = 'Кошачья критическая гадза'
   glad_damage_down_skill_text = 'Эльфийская гадза с эффектом попускания'
   glad_poison_skill_text = 'Ядовитая гадза по-киевски'
   glad_description = 'Владеет арсеналом фирменных гадз'
   shiva_name = 'Великая Шива'
   shiva_critical_up_skill_text = 'Криты завезли!'
   shiva_damage_up_skill_text = 'Урон завезли!'
   shiva_description = 'Божественность дает ей шанс на уворот, с каждым ходом становится критичнее'
   makar_name = 'Король Макар'
   makar_description = 'Пока что финальный, твои статы - его статы'
   gomozeki_name = 'Гомогомозеки'
   gomozeki_description = 'Голые, рельефные и агрессивно-активно настроенные'

   kolbas_name = 'Хата Колбаса'
   kolbas_description = 'Нахождение здесь насыщает тебя благовонием помойки!\n-10%❤️'
   kolbas_icon = '📚'
   polazna_name = 'Полазна'
   polazna_description = 'Палаточные осознанки повысили твою духовность и снизили враждебность\n+20%❤️\n-10%⚔️'
   polazna_icon = '⛺️'
   god_city_name = 'Город Богов'
   god_city_description = 'Прогулка по нему разносторонне возвышает тебя\n+10%❤️\n+10%⚔️\n+10%💥'
   god_city_icon = '⚓️'
   bad_trip_name = 'Бэд Трип'
   bad_trip_effect_text = '-20%❤️\n-20%⚔️'
   bad_trip_description = 'Тебя занесло в Бэд Трип! Вот незадача!\n'
   bad_trip_icon = '😵'
   molebka_name = 'Молебка'
   molebka_effect_text = '-20%❤️\n+10%⚔️'
   molebka_description = 'Медитативный псайденс измотал тебя, но в итоге ты стал сильнее\n'
   molebka_icon = '🎇'
   army_name = 'Армия'
   army_description = 'Военкомат добрался до вас, сэр! Армия забрала год твоей жизни, но ты неплохо так подкачался\n-50%❤️\n+30%⚔️'
   army_icon = '🧨'
   drochilnya_name = 'Дрочильня'
   drochilnya_description = 'Тренировка в тесном мужском кругу лишней не бывает, да?\n+10%⚔️\n+10%💥\n'
   drochilnya_icon = '💦'
   stage25_name = '25й этаж'
   stage25_description = 'Святое место, где настоящие убийцы смотрят в пол\n-50%⚔️\n-10%💥'
   stage25_icon = '💀'

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
   cola_description = 'Грозное оружие судного нового года\n-500🖤'
   sick_sock_name = 'Потный носок'
   sick_sock_description = 'Противник поймал твой носок лицом\n-50🖤🦠'
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