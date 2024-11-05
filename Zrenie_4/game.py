import pyautogui
import cv2
import numpy as np
import time
import math

# Задаем параметры для фильтрации по количеству черных пикселей
min_black_pixels1 = 200   # Минимальное количество черных пикселей для препятствия
max_black_pixels1 = 1300  # Максимальное количество черных пикселей для препятствия

# Координаты области экрана, где находится динозавр (определите заранее)
dino_x, dino_y = 57, 207           # Примерные координаты динозавра
jump_threshold = 250    # Пороговое расстояние для прыжка

while True:
    # Захват скриншота всего экрана с помощью PyAutoGUI
    screenshot = pyautogui.screenshot()

    # Преобразуем скриншот в формат, поддерживаемый OpenCV
    img = np.array(screenshot)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

    # Обрезка изображения по заданным отступам (укажите нужные отступы)
    top = 250
    bottom = 520
    left = 980
    right = 50
    img = img[top:img.shape[0] - bottom, left:img.shape[1] - right]

    # Преобразование в оттенки серого для упрощения порогового преобразования
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Пороговое преобразование для выделения черных областей (препятствий)
    _, binary_img = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY_INV)

    # Поиск контуров на бинарном изображении
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Создаем маску для текущего контура и подсчитываем черные пиксели внутри
        mask = np.zeros_like(gray_img)
        cv2.drawContours(mask, [contour], -1, 255, thickness=cv2.FILLED)
        
        # Подсчет черных пикселей внутри маски
        black_pixel_count = cv2.countNonZero(cv2.bitwise_and(binary_img, binary_img, mask=mask))
        
        # Фильтрация контуров по количеству черных пикселей для выделения препятствий
        if min_black_pixels1 <= black_pixel_count <= max_black_pixels1:
            # Вычисление центра препятствия
            M = cv2.moments(contour)
            if M["m00"] != 0:
                obstacle_x = int(M["m10"] / M["m00"])
                obstacle_y = int(M["m01"] / M["m00"])
                
                # Проверка расстояния между динозавром и препятствием
                distance = math.sqrt((obstacle_x - dino_x) ** 2 + (obstacle_y - dino_y) ** 2)
                print(distance ,jump_threshold)
                if distance < jump_threshold:
                    # Имитируем нажатие "Пробела" для прыжка
                    pyautogui.press("space")
                    print("Jump triggered!")

    # Отображение обработанного изображения (опционально)
    cv2.imshow("Game Screen", img)

    # Условие выхода: Нажатие клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
    # Добавляем задержку для снижения нагрузки на процессор
    time.sleep(0.2)

# Освобождаем ресурсы
cv2.destroyAllWindows()
