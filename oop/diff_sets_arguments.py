class Contact:
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email

class AddressHolder:
    def __init__(self, street='', city='', code='', **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone



