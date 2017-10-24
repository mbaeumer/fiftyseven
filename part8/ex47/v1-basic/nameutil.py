from astronaut import Astronaut

def handle_name(name):
    firstname = ""
    lastname = ""
    parts = name.split(" ")
    if len(parts) == 2:
        firstname = parts[0]
        lastname = parts[1]
    elif len(parts) > 2:
        firstname = parts[0]
        index = 1
        while index < len(parts):
            lastname += parts[index]
            lastname += " "
            index = index + 1
        lastname = lastname[:-1]
        #lastname = " ".join(xrange(2, len(parts)))
    astronaut = Astronaut(firstname, lastname, None)
    return astronaut
