import cv2
import os
from ultralytics import YOLO

def load_image(image_path):
    """Загружает изображение по указанному пути."""
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Image at {image_path} could not be loaded.")
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def process_images_in_folder(folder_path, model):
    """Обрабатывает все изображения в указанной папке."""
    # Получаем список всех файлов в папке
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

    for image_file in image_files:
        # Полный путь к изображению
        image_path = os.path.join(folder_path, image_file)
        print(f"Processing image: {image_path}")

        # Загружаем изображение
        image = load_image(image_path)
        if image is None:
            continue  # Пропускаем изображение, если оно не загрузилось

        # Выполняем предсказание на изображении
        results = model.predict(source=image_path, save=True, save_txt=True)

        # Выводим результаты
        for result in results:
            print(result.boxes)  # Координаты обнаруженных объектов
            print(result.names)  # Названия классов объектов

        # Отображаем изображение с аннотациями
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cls_id = int(box.cls[0])  # Преобразуем тензор в целое число
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(image, result.names[cls_id], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Уменьшаем изображение до нужного размера
            resized_image = cv2.resize(image, (1300, 1000))

            # Показываем уменьшенное изображение с аннотациями
            cv2.imshow("YOLOv8 Inference (Resized)", resized_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == '__main__':
    # Загрузите обученную модель
    model = YOLO("runs/detect/train/weights/best.pt")  # Путь к файлу с весами модели / Также можно train заменить на train2 Для того чтобы проверить ещё одну обученную модель

    # Путь к папке с изображениями для тестирования
    folder_path = "testik"

    # Обрабатываем все изображения в папке
    process_images_in_folder(folder_path, model)
