from io import BytesIO
from data.make_data import make_data
from PIL import Image
import base64

def main():
    data = make_data()
    image_bytes = base64.b64decode(data[0].image_data)
    image = Image.open(BytesIO(image_bytes))
    image.show()
    print(len(data))
    NUM_CLOSED = 0
    NUM_OPEN = 0
    for d in data:
        if d.label == "OAG":
            NUM_OPEN += 1
        else:
            NUM_CLOSED += 1
    print(f"Open: {NUM_OPEN}\nClosed: {NUM_CLOSED}")


if __name__ == "__main__":
    main()
