from UseCases.object_recognition import main as object_recognition
from UseCases.object_tracking import main as object_tracking
from UseCases.object_reconstruct import main as object_reconstruction
from UseCases.image_segmentation import main as image_segmentation
from UseCases.train_model import create_model, select_model


options = {
    "object tracking": object_tracking,
    "object recognition": object_recognition,
    "object_reconstruction": object_reconstruction,
    "image_segmentation": image_segmentation,
    "train model": create_model,
    "predict": select_model,
}

