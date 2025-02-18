from ultralytics import YOLO
import cv2

if __name__ == '__main__':
    # Загрузите обученную модель
    model = YOLO("runs/detect/train/weights/best.pt")  # Путь к файлу с весами модели

    # Путь к изображению для тестирования
    image_path = "testik/p1.jpg"

    # Выполните предсказание на изображении
    results = model.predict(source=image_path, save=True, save_txt=True)

    # Выведите результаты
    for result in results:
        print(result.boxes)  # Координаты обнаруженных объектов
        print(result.names)  # Названия классов объектов

    # Отобразить изображение с аннотациями
    for result in results:
        image = cv2.imread(image_path)
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cls_id = int(box.cls[0])  # Преобразуйте тензор в целое число
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, result.names[cls_id], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow("YOLOv11 Inference", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()