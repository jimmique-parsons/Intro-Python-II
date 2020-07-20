class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'Name: {self.name}, Description: {self.description}'

    def on_take(self):
        return f'\n You have picked up {self.name} \n'

    def on_drop(self):
        return f'\n You have dropped {self.name} \n'
