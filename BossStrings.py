# модуль со всеми строками и функциями вывода сообщений, 
# использующих динамические характеристики касательно босса 
# и его взаимодействия с игроком, локациями и предметами

import ItemsGenerator
import CharactersGenerator
import GameStrings

import Locations
import InteractionParameters

class Palich():
   name = 'Палыч'
   description = 'Раздает перманентные баны'
   # сообщение способности, применяемой до боя
   prelude_skill = 'Палыч завалил твой ебалыч - скиллы и предметы не поюзать'


class Chaikovskii():
   name = 'Чайковский'
   description = 'Одна святая песня воскрешает его перед порогом смерти'
   # сообщение при воскресании
   ressurection = 'Брат! Не засыпай!'

   # интерактив с локацией Город Богов
   def god_city_interaction():
      return '{0}\n+{1}{2}\n+{3}{4}\n+{5}{6}'.format('Чайковский здесь чувствует приток самопиздатости',
                                                      Locations.loc.health, GameStrings.Icons.boss_health,
                                                      Locations.loc.damage, GameStrings.Icons.damage,
                                                      Locations.loc.critical_chance, GameStrings.Icons.critical_chance)


class Viv():
   name = 'Вив'
   description = 'В конце хода наваливает бассов повышая свой урон'
   # сообщение способности, применяемой в конце раунда
   end_skill = 'Бассы подъехали!'
   
   # интерактив с предметом Травмат Володи
   def travmat_interaction():
      return '{0}\n-{1}{2}{3}'.format('Володя забрал свой травмат!',
                                       InteractionParameters.Boss.viv_travamat, 
                                       GameStrings.Icons.player_health,
                                       GameStrings.Icons.bleeding)


class Sasha():
   name = 'Саша Шлякин'
   description = 'Убей его и возвысь себя'
   # сообщение об замене босса, если игрок не является Саней
   cancel_fight = 'Саша Шлякин нападает только на самого себя, подберем тебе другого'
   victory_fight = 'Опять ты себя покусал, Саня'


class Tvar():
   name = 'Качаловская Тварь'
   description = 'Бить ее больно и крайне неприятно, себе хуже только сделаешь'


class Randomich():
   name = 'Рандом Рандомыч'
   description = 'Может быть лох, а может и бог'


class Kitty():
   name = 'Котенок-тролль'
   description = 'Вислоухий и пузатый, мурчанием вызывает бессилие, еще может закогтить тебя'
   # оглушающая способность
   stan_skill = 'Мурлы-сна!'
   # кровоточащая способность
   bleeding_skill = 'Зацепка когтями!'


class Inkvisizia():
   name = 'Инквизиция'
   description = 'Неопытных юзеров может моментально умертвить, тут уж как повезет'  


class DocLeha():
   name = 'Доктор Леха'
   description = 'Может провести вихревой удар джаггернаута своей сумкой'
   # сообщение способности, применяемой в конце раунда
   end_skill = 'Джагернаааааут!'


class DrunkLeha():
   name = 'Пьяный Леха'
   description = 'В конце хода накидывает еще коктейльчик, становясь опаснее'
   # сообщение способности, применяемой в конце раунда
   end_skill = 'Леха бухает! Остановите его!'


class Mel():
   name = 'Мел'
   description = 'Отсутвие гордости делает его почти не восприимчивым к урону'
   # особое сообщение при уклонении Мела
   miss = 'Мелу похуй на твой урон'
   # сообщение способности, применяемой в конце раунда
   end_skill = 'Мел залил тебе блазуху в ухо!'


class Redhead():
   name = 'Рыжий'
   description = 'Крайне неприятная и живучая падла'
   # сообщение способности, применяемой до боя
   prelude_skill = 'Рыжий потравил тебя в душу'


class Sledovatel():
   name = 'Следователь'
   description = 'Если успеет заполнить на тебя доки - будешь упакован в тюрьму'
   # интерактив с предметами игрока в локальной категории Drugs
   def drugs_check():
      return '{0}\n{1}+{2}%'.format('Употребляли? Тогда быстрее вас упакуем', 
                                    InteractionParameters.Boss.sledovatel_drugs, 
                                    GameStrings.Icons.chains)

   # интерактив с большим количеством урона игрока
   def damage_down_skill():
      return '{0}\n-{1}%{2}'.format('Злоупотребление дамагом карается по закону!', 
                                    InteractionParameters.Boss.sledovatel_damage_down, 
                                    GameStrings.Icons.damage)

   skill_meter = 'Степень упаковки'


class Doner():
   name = 'Донер Кебаб'
   description = 'При нем лучше не бухать, травля эту мразь делает сильнее'
   # интерактив с предметом Рампаг
   rampag_interaction = 'Рампаг заходит сзади! Моментальная смерть для Донера!'

   # интерактив с пердметом Костюм Эверласт
   def everlast_interaction():
      return '{0}\n+{1}%{2}\n+{1}%{3}'.format('Донер спиздил твой костюм!',
                                                InteractionParameters.Boss.doner_everlast, 
                                                GameStrings.Icons.boss_health,
                                                GameStrings.Icons.damage)

   # интерактив с пердметом 2.5-литровка Кока-Колы
   def cola_interaction():
      return '{0}\n-{1}{2}\n-{1}{3}'.format('Открывая твою Колу, Донер захуярил и себя, и тебя, и обои!',
                                             InteractionParameters.Boss.doner_cola, 
                                             GameStrings.Icons.player_health,
                                             GameStrings.Icons.boss_health)
   
      # интерактив с пердметом Потный носок
   def sock_interaction():
      return '{0}\n+{1}{2}{3}'.format('Да его носки куда уж жестче', 
                                       InteractionParameters.Boss.doner_sock, 
                                       GameStrings.Icons.boss_health, 
                                       GameStrings.Icons.regeneration)

   # интерактив с пердметом Блевотный харчок
   def harchok_interaction():
      return '{0}\n+{1}{2}{3}'.format('Он его ассимилировал!', 
                                       InteractionParameters.Boss.doner_harchok, 
                                       GameStrings.Icons.boss_health, 
                                       GameStrings.Icons.regeneration)

   # интерактив с пердметоми из категории Алкоголь
   def booze_interaction():
      return '{0}\n+{1}{2}'.format('Пизда твоему бухлу, Донер его выпил',
                                    ItemsGenerator.item.value, GameStrings.Icons.boss_health)

   # интерактив с локацией Хата Колбаса
   def kolbas_interaction():
      return '{0}\n+{1}{2}'.format('Ой ой, Донер у Колбаса стал крепче', 
                                    InteractionParameters.Boss.doner_kolbas, GameStrings.Icons.boss_health)                            


class BlackStas():
   name = 'Черный Стас'
   description = 'Правильно выбирай слова для его осадки - закинет за всю хуйню обратно'
   # интерактив с игроком Митя
   mitya_interaction = 'Стас, по-справедливости, бахает столько же эликсиров, что и Митя'
   # особое сообщение отражающей урон способности Стаса
   miss = 'Стас отразил твою хуйню'


class Dron():
   name = 'Дрон'
   description = 'Доведешь Андрея до обиды - умрешь в его глазах'
   
   # увеличение накопительной способности в зависимости
   # от количества походов в магазин Братишкино логово
   def bratishki_interaction():
      return '{0}\n{1}+{2}%'.format('За каждый поход к братишкам', 
                                    GameStrings.Icons.obida, 
                                    CharactersGenerator.boss.skill_meter_level_up)

   # интерактив с баффом Мясо Андрея
   def dron_meat_interaction():
      return '{0}\n{1}+{2}%'.format('За то что ты ел мясо Андрея', 
                                    GameStrings.Icons.obida, 
                                    CharactersGenerator.boss.skill_meter_level_up)  
                                                                   
   end_skill = 'Дрон затаил лютую обиду!'
   skill_meter = 'Риск обиды'


class Glad():
   name = 'Валера Гладиатор'
   description = 'Владеет арсеналом фирменных гадз'
   # наносящая урон способность
   damage_skill = 'Твин-турбо гадза на минус уши'
   # лечебная способность
   health_up_skill = 'Церковная целебная гадза'
   # повышающая шанс критической атаки способность
   critical_up_skill = 'Кошачья критическая гадза'
   # понижающая урон способность
   damage_down_skill = 'Эльфийская гадза с эффектом попускания'
   # отравляющая способность
   poison_skill = 'Ядовитая гадза по-киевски'
   

class Shiva():
   name = 'Великая Шива'
   description = 'Божественность дает ей шанс на уворот, с каждым ходом становится критичнее'
   # повышающая шанс критической атаки способность
   critical_up_skill = 'Криты завезли!'
   # повышающая урон способность
   damage_up_skill = 'Урон завезли!'
   

class Makar():
   name = 'Король Макар'
   description = 'Это финиш! Твои статы - его статы'


class Gomozeki():
   name = 'Гомогомозеки'
   description = 'Голые, рельефные и агрессивно-активно настроенные'


def boss_skill_meter_message(boss_name):

   if boss_name == Sledovatel.name:
         return '{0}{1} {2}%{0}'.format(GameStrings.Icons.chains, Sledovatel.skill_meter, 
                                          CharactersGenerator.player.police_wanted)
   elif boss_name == Dron.name:
         return '{0}{1} {2}%{0}'.format(GameStrings.Icons.obida, Dron.skill_meter, 
                                          CharactersGenerator.boss.skill_meter_level)
