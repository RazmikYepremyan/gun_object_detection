
🔫 Gun Detection Using YOLOv8

This project implements a firearm detection model using [YOLOv8](https://github.com/ultralytics/ultralytics), a state-of-the-art object detection architecture developed by Ultralytics. The model is capable of identifying and localizing guns in images with high accuracy and speed, making it suitable for research in surveillance, threat detection, and safety systems.

📂 Dataset

The model was trained on the [Guns Object Detection Dataset](https://www.kaggle.com/datasets/issaisasank/guns-object-detection/data) from Kaggle. The dataset contains thousands of real-world images with labeled bounding boxes indicating the location of firearms. All annotations were preprocessed and converted into YOLO-compatible format for training.

🧠 Model Overview

* **Architecture**: YOLOv8 (Nano variant)
* **Framework**: Ultralytics Python SDK
* **Classes**: 1 (`weapon`)
* **Training Format**: YOLO bounding box format — normalized `[class x_center y_center width height]`
* **Output**: Bounding boxes with confidence scores for weapon detections

💡 Project Goals

* Develop a lightweight and efficient object detector for gun identification
* Evaluate detection performance using YOLOv8 on a single-class problem
* Provide a baseline for further research in real-time threat detection systems

🚨 Potential Applications

* Real-time surveillance system enhancement
* Automated video monitoring for law enforcement
* Smart camera systems in public venues (schools, airports, malls)
* Research in violence prevention and safety AI

⚠️ Disclaimer

This project is intended for **educational and research purposes only**. Use of weapon detection systems in real-world applications should always comply with local laws, regulations, and ethical standards. The model is not guaranteed to perform reliably in critical safety scenarios without extensive testing and validation.
