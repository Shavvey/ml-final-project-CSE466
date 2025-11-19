from data.eyetype import EyeType
from dataclasses import dataclass

@dataclass
class DataFrame:
    """This class is meant to encapsulate all the features the resnet model will train with"""

    type: EyeType  # either left (OS) or right (OD) eye
    image_data: bytearray  # images as bytes (normalize this later)
    label: str

    def __init__(self, image_data: bytearray, type: EyeType, label: str):
        self.type = type
        self.image_data = image_data
        self.label = label

    def __str__(self) -> str:
        return f"Label: {self.label}, Image Data: {self.image_data}"
