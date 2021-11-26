"""
границы и разделители таблицы
"""
tlc = top_left_corner = chr(9556)
trc = top_right_corner = chr(9559)
blc = bottom_left_corner = chr(9562)
brc = bottom_right_corner = chr(9565)
thb = top_horizontal_border = chr(9574)
bhb = bottom_horizontal_border = chr(9577)
lvb = left_vertical_border = chr(9568)
rvb = right_vertical_border = chr(9571)
cr = cross = chr(9580)
v = vertical = chr(9553)
h = horizontal = chr(9552)
f = field = chr(9617)

b = blank = ''
s = space = ' '
mcl = max_column_len = []
top = []
bottom = []
cross_ = []

tab = [
    ['Прізвище', 'Ім’я', 'по-Батькові', 'дата народження', 'хобi'],
    ['Геррінгтон', 'Біллі', 'Глен Гарольд', '14 липня 1969', 'SUCK SOME DICK'],
    ['Даркхольм', 'Ван', 'Некстдоровіч', '24 жовтня 1972 року', 'dungeon master & performance artist'],
    ['Мілос', 'Рікардо', 'Фістович', '', 'FLEX']]

"""
builtins def chr(__i: int) -> str"
Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
for more symbol code https://unicode-table.com/ru/
"""
