from sikuli import *
# Область экрана, на которой выполняется поиск элементов
area = Region(1925,100,1913,937)
# Путь к файлу изображений, которые нужно найти
bet_delete = Pattern("bet_delete.png").targetOffset(0,6)
reason_field = Pattern("reason_field.png").targetOffset(0,12)
cancel_button = Pattern("cancel_button.png").targetOffset(0,6)
# Кликаем изображение в указанной области
click(area.find(bet_delete))
wait(1)
type(area.find(reason_field), "Peredumal")
click(area.find(cancel_button))