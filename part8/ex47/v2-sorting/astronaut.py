

class Astronaut:
    def __init__(self, firstname, lastname, craft):
      self.firstname = firstname
      self.lastname = lastname
      self.craft = craft

    def to_dict(self):
      data = {}
      data['firstname'] = self.firstname
      data['lastname'] = self.lastname
      data['craft'] = self.craft
      return data