import os
from ultralytics import YOLO
import yaml

class TrainModel():
    def __init__(self):
        self.yaml_file_name = ''
        self.user_model_name = ''

    def create_yaml_file(self):
        dataset_root = input("Path to dataset root dir (example, '../datasets/coco8'): ")
        train_path = input("Relative path to train images(example, 'images/train'): ")
        val_path = input("Relative path to validation images(example, 'images/val'): ")
        test_path = input("Relative path to test images(optional, leave it blank if not exist): ")

        num_classes = int(input("Number of classes: "))

        names = {}
        for _class in range(num_classes):
            class_name = input(f"Name of class {_class+1}: ")
            names[_class] = class_name

        yaml_content = {
            'path': dataset_root,
            'train': train_path,
            'val': val_path,
            'test': test_path if test_path else '',
            'names': names
        }

        self.yaml_file_name = input("Name of YAML file to be created (example, 'custom_dataset.yaml'): ")

        with open(f'../UserYaml/{self.yaml_file_name}', 'w') as yaml_file:
            yaml.dump(yaml_content, yaml_file, sort_keys=False, default_flow_style=False)

        print(f"File {self.yaml_file_name} created success!")


    def create_model(self):
        if os.path.exists(f'../UserYaml/{self.yaml_file_name}'):
            model = YOLO("yolov8s.pt") 
            model.train(data=f'../UserYaml/{self.yaml_file_name}', epochs=10, imgsz=640)
            model.save(f'UserModels/{self.user_model_name}') 
            if os.path.exists("yolov8s.pt"):
                os.remove("yolov8s.pt")
        else:
            raise Exception("Create yaml file first")


    def predict(self, path):
        if os.path.exists(path):
            model = YOLO(f'UserModels/{self.user_model_name}')
            results = model.predict(source=path)   
            print(results)
        else:
            raise Exception("Path to image does not exist")
        

    

