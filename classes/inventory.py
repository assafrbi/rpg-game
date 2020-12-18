class Item:
    def __init__(self, name, item_type, description, prop):
        self.name = name
        self.type = item_type
        self.description = description
        self.prop = prop
        self.amount = 1

    def get_prop(self):
        return self.prop

    def get_amount(self):
        return self.amount

    def set_amount(self):
        self.amount -= 1

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_description(self):
        return self.description
