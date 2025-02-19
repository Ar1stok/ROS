# ROS Competition
![image](https://github.com/user-attachments/assets/e36f4896-0aa0-41d3-ab44-b3f7bc313921)

## Обработка светофора
![image](https://github.com/user-attachments/assets/bef6706e-4089-4abe-bc7f-8f3d7677daf4)
Для выявления зеленого цвета на светофоре мы используем цветовую маску, выделяя только зеленый цвет. Как только у нас появляется зеленый цвет - изменяем статус ботика и поехали.

## Движение
![image](https://github.com/user-attachments/assets/0edd17ea-17be-42df-8afd-ea1ac940c0f5)
Движение реализовано как поиск и детекция полос (белая и желтая) и удержание некоторого отступа от этих полос. Красная точка - нужное расстояние, зеленая точка - позиция машинки в момент времени, по итогу мы пытаемся создать сходимость красной и зеленой точек. Детектим цвета тем же методом что и раньше - маской. Угловую скорость регулируем с помощью PID регулятора.

## Перекресток
![image](https://github.com/user-attachments/assets/0d38c1bc-92ee-4571-a471-699f4e80f1e3)
Подъезжая к перекрестку, находим знак на изображении, выделяем цвета маской, разделяем изображение на 2 части, и там, где больше синего цвета, в ту сторону и поворачиваем. Решение о повороте принимаем, когда подъезжаем к перекрестку. 

## Запуск
Для запуска используйте последовательно это команды:

```bash
colcon build

. install/setup.bash

ros2 launch robot_bringup autorace_2023.launch.py &

ros2 launch autorace_detect autorace_detect.launch.py &

ros2 run referee_console mission_autorace_2023_referee
```
