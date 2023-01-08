import base64
from PIL import Image
import io

class Database:
    data_first = []
    data_second = []
    data_manager = [data_first, data_second]
    
    def add_data(id, data):
        Database.data_manager[id].append(python2json(data))

    def get_data(id):
        return {"data": Database.data_manager[abs(id-1)]}

    def delete_data(id):
        data = Database.data_manager[abs(id-1)]
        if(len(data)!=0):
            data.pop(0)
            return "Last message deleted", 204
        return "There was no message", 204

class DataGroup:
    def __init__(self, data) -> None:
        self.id = data["id"]
        self.title = data["title"]
        self.text = data["text"]
        self.image = data["image"]

def json2python(data):
    return DataGroup(data)

def python2json(data):
    return {"title": data.title,
            "text": data.text,
            "image": data.image,}

def base64ToBMP(image_base64):
    # image_base64 = image_base64.split("base64,")[1]
    image_data = base64.b64decode(image_base64)
    img = Image.open(io.BytesIO(image_data))
    img = img.resize((64, 64))
    #Threshold
    # img = img.point( lambda p: 255 if p > 128 else 0 )
    img.show()

    output = io.BytesIO()
    img.save(output, 'BMP')

    # Get the resized image data
    image_data = output.getvalue()

    image_hex = image_data.hex()
    image_bmp = []
    for i in range(0, len(image_hex), 2):
        image_bmp.append(f'0x{image_hex[i:i+2]}')

    return image_bmp

def add_db(payload):
    data = json2python(payload)
    data.image = base64ToBMP(data.image)
    Database.add_data(id=data.id, data=data)
    return 'Message added', 200

def get_db(id):
    return Database.get_data(id=int(id))

def delete_db(id):
    return Database.delete_data(id=int(id))