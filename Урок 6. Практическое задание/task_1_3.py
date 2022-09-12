"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для третьего скрипта
"""
# Основы. Урок 9. Задание 1
# 1. Создать класс TrafficLight (светофор).
# Определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
from time import sleep
from recordclass import recordclass
from memory_profiler import profile
from pympler.asizeof import asizeof


class TrafficLight:
    __color = 'красный'

    @profile
    def running(self):
        correct_job = (('красный', 7), ('желтый', 2), ('зеленый', 7))
        for color, delay in correct_job:
            reaction = {
                'красный': '(стой, не газуй)',
                'желтый': '(втыкай передачу)',
                'зеленый': f'(газ в палас, у тебя {delay} секунд)'
            }
            print(color, reaction[color], end=' ')
            for sec in range(delay, 0, -1):
                print(sec, end=' ')
                sleep(1)
            print()
        print('вы добрались до места')


a = TrafficLight()
a.running()
print(asizeof(a))


class TrafficLight:
    __slots__ = []
    __custom = recordclass('traffic_light', 'color timer')

    @profile
    def running(self):
        correct_job = (
            self.__custom(color='красный', timer=2),
            self.__custom(color='желтый', timer=2),
            self.__custom(color='зеленый', timer=2)
        )
        for color, delay in correct_job:
            reaction = {
                'красный': '(стой, не газуй)',
                'желтый': '(втыкай передачу)',
                'зеленый': f'(газ в палас, у тебя {delay} секунд)'
            }
            print(color, reaction[color], end=' ')
            for sec in range(delay, 0, -1):
                print(sec, end=' ')
                sleep(1)
            print()
        print('вы добрались до места')


a = TrafficLight()
a.running()
print(asizeof(a))

"""
красный (стой, не газуй) 7 6 5 4 3 2 1 
желтый (втыкай передачу) 2 1 
зеленый (газ в палас, у тебя 7 секунд) 7 6 5 4 3 2 1 
вы добрались до места

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    43     36.1 MiB     36.1 MiB           1       @profile
    44                                             def running(self):
    45     36.1 MiB      0.0 MiB           1           correct_job = (('красный', 7), ('желтый', 2), ('зеленый', 7))
    46     36.1 MiB      0.0 MiB           4           for color, delay in correct_job:
    47     36.1 MiB      0.0 MiB           3               reaction = {
    48     36.1 MiB      0.0 MiB           3                   'красный': '(стой, не газуй)',
    49     36.1 MiB      0.0 MiB           3                   'желтый': '(втыкай передачу)',
    50     36.1 MiB      0.0 MiB           3                   'зеленый': f'(газ в палас, у тебя {delay} секунд)'
    51                                                     }
    52     36.1 MiB      0.0 MiB           3               print(color, reaction[color], end=' ')
    53     36.1 MiB      0.0 MiB          19               for sec in range(delay, 0, -1):
    54     36.1 MiB      0.0 MiB          16                   print(sec, end=' ')
    55     36.1 MiB      0.0 MiB          16                   sleep(1)
    56     36.1 MiB      0.0 MiB           3               print()
    57     36.1 MiB      0.0 MiB           1           print('вы добрались до места')


152


красный (стой, не газуй) 2 1 
желтый (втыкай передачу) 2 1 
зеленый (газ в палас, у тебя 2 секунд) 2 1 
вы добрались до места

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    70     36.1 MiB     36.1 MiB           1       @profile
    71                                             def running(self):
    72     36.1 MiB      0.0 MiB           1           correct_job = (
    73     36.1 MiB      0.0 MiB           1               self.__custom(color='красный', timer=2),
    74     36.1 MiB      0.0 MiB           1               self.__custom(color='желтый', timer=2),
    75     36.1 MiB      0.0 MiB           1               self.__custom(color='зеленый', timer=2)
    76                                                 )
    77     36.1 MiB      0.0 MiB           4           for color, delay in correct_job:
    78     36.1 MiB      0.0 MiB           3               reaction = {
    79     36.1 MiB      0.0 MiB           3                   'красный': '(стой, не газуй)',
    80     36.1 MiB      0.0 MiB           3                   'желтый': '(втыкай передачу)',
    81     36.1 MiB      0.0 MiB           3                   'зеленый': f'(газ в палас, у тебя {delay} секунд)'
    82                                                     }
    83     36.1 MiB      0.0 MiB           3               print(color, reaction[color], end=' ')
    84     36.1 MiB      0.0 MiB           9               for sec in range(delay, 0, -1):
    85     36.1 MiB      0.0 MiB           6                   print(sec, end=' ')
    86     36.1 MiB      0.0 MiB           6                   sleep(1)
    87     36.1 MiB      0.0 MiB           3               print()
    88     36.1 MiB      0.0 MiB           1           print('вы добрались до места')


32

Применение слотов в ООП снижает потребляемую память. Так как добавлены слоты, __dict__ больше не существует.
В этом примере экземпляр класса в оптимизированном решении занимает в 5 раз меньше места.
"""
