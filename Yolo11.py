from ultralytics import YOLO

if __name__ == '__main__':
    # Load a COCO-pretrained YOLO11n model
    model = YOLO("yolo11n.pt")

    # Train the model on the COCO8 example dataset for ~ epochs
    results = model.train(data="config.yaml", epochs=150, imgsz=640)

    # Run inference with the YOLO11n model on the 'bus.jpg' image
    results = model("D:/LabelProject/LabelPRoj/garbage_dataset_yolo")