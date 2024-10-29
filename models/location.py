class Location():

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
        self.employees = None
        self.animals = None

    def serialized(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
        }
