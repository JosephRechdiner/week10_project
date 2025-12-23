class Contact:
    def __init__(self, id: int, first_name: str, last_name: str, phone_number: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def as_dict(self):
        return self.__dict__