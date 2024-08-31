import os
from ultralytics import YOLO
import yaml


current_dir = os.path.dirname(os.path.abspath(__file__))


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

        dataset_root = os.path.abspath(dataset_root)
        train_path = os.path.join(dataset_root, train_path)
        val_path = os.path.join(dataset_root, val_path)
        if test_path:
            test_path = os.path.join(dataset_root, test_path)

        yaml_content = {
            'path': dataset_root,
            'train': train_path,
            'val': val_path,
            'test': test_path if test_path else '',
            'names': names
        }

        self.yaml_file_name = input("Name of YAML file to be created (example, 'custom_dataset.yaml'): ")

        if not os.path.exists(os.path.join(current_dir, "..", "UserYaml")):
            os.mkdir(os.path.join(current_dir, "..", "UserYaml"))

        model_path = os.path.join(current_dir, "..", "UserYaml",
            self.yaml_file_name)
        with open(model_path, 'w') as yaml_file:
            yaml.dump(yaml_content, yaml_file, sort_keys=False, default_flow_style=False)

        print(f"File {self.yaml_file_name} created success!")


    def create_model(self):
        yaml_path = os.path.join(current_dir, "..", "UserYaml", self.yaml_file_name)
        model_path = os.path.join(current_dir, "..", "UserModels",
            self.user_model_name)
        if os.path.exists(yaml_path):
            model = YOLO("yolov8s.pt") 
            model.train(data=yaml_path, epochs=10, imgsz=640)
            model.save(model_path)
            if os.path.exists("yolov8s.pt"):
                os.remove("yolov8s.pt")
        else:
            raise Exception("Create yaml file first")


    def predict(self, path):
        if os.path.exists(path):
            model_path = os.path.join(current_dir, "..", "UserModels",
                self.user_model_name)
            model = YOLO(model_path)
            results = model.predict(source=path)
            image_index = 0   
            for img in results:
                image_path = os.path.join(current_dir, "..",
                    f"predicted_image_{image_index}.jpg")
                img.save(image_path)
                image_index+=1
        else:
            raise Exception("Path to image does not exist")

def create_model():
    model = TrainModel()
    model.create_yaml_file()
    model.create_model()

def select_model():
    user_models_dir = os.path.join(current_dir, "..", "UserModels")
    if not os.path.exists(user_models_dir):
        print("Nenhum modelo adicionado")
        return

    models = os.listdir(user_models_dir)
    for model in models:
        print(f"> {model}")

    while True:
        model_name = input("Selecione o modelo que deseja utilizar: ")
        if os.path.exists(os.path.join(user_models_dir, model_name)):
            break
        print("Este modelo nao existe")

    model = TrainModel()
    model.user_model_name = model_name

    path = input("Entre com o caminho das imagens que deseja fazer predicoes: ")
    model.predict(path)

