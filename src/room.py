# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items


def __str__(self):
    output = ""
    output += f'Room: {self.name} \n'
    output += f'{self.description} \n\n'
    output += 'Items: \n'

    for index, item in enumerate(self.items):
        output += str(index+1) + '. ' + str(item.name) + \
            ' - ' + str(item.description) + '\n'

    return output
