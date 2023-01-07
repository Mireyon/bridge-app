class Database:
    data_first = []
    data_second = []
    
    def add_data(data):
        if(data.id==1):
            Database.data_first.append(python2json(data))
        else:
            Database.data_second.append(python2json(data))

    def get_data(id):
        if(id==1):
            return {"data": Database.data_second}
        return {"data":Database.data_first}

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

def add_db(payload):

    data = json2python(payload)
    Database.add_data(data)
    return 'OK', 200

def get_db(id):
    return Database.get_data(id)