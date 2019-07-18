from numstranslate.alg import dec_to_bin, bin_to_dec
from random import randint
from tqdm import tqdm


def random_binary_number():
    """
    Возвращает случайное двоичное число
    Это число будет номером пробирки с ядом
    """
    return dec_to_bin(randint(1, 1000), bit_depth=10)


binary_numbers_vial = []
print('1) Вычисляем номера пробирок в двоичном коде')
for num in tqdm(range(1, 1001)):
    binary_numbers_vial.append(dec_to_bin(num, bit_depth=10))

print('\n2) Даём по капле из пробирки мышам.\nЕдиницы - клетки с мышами, которым нужно дать каплю из пробирки')
number_vial_poison = random_binary_number()


dead_mouse = []
for i in range(10):
    if number_vial_poison[i] == '1':
        dead_mouse.append(i + 1)

print('\n3) Умерли мыши в клетках №{}'.format(' №'.join([str(number_mouse) for number_mouse in dead_mouse])))
print('Отмечаем номера погибших мышей единицей справа налево, получается {}'.format(number_vial_poison))
print('\n4) Переводим {} в десятичное число.\nПолучается {}, это номер пробирки с ядом'.format(number_vial_poison,
                                                                                               bin_to_dec(number_vial_poison)))
print('Разбор задачи в журнале "Код" - https://thecode.media/binary-mouse/')
