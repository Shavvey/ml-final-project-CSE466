from eye_type import EyeType


class DataFrame:
    """This class is meant to encapsulate all the features the resenet model will train with"""

    type: EyeType  # either left (OS) or right (OD) eye

    image_data: bytearray  # images as bytes (normalize this later)

    def __init__(self, image_data: bytearray, type: EyeType):
        self.type = type
        self.image_data = image_data
