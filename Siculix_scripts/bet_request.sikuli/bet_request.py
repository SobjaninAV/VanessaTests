from sikuli import *
# Область экрана, на которой выполняется поиск элементов
area = Region(1925,100,1913,937)
# Путь к файлу изображений, которые нужно найти
bet_request_field = Pattern("bet_request_field.png").targetOffset(-39,2)
reason_field = Pattern("reason_field.png").targetOffset(0,18)
# Кликаем изображение в указанной области
click(area.find(bet_request_field))
wait(1)
type(area.find(bet_request_field), "100500")