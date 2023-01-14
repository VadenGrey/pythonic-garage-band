class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []

    def __str__(self):
        return self.name

    def play_solos(self):
        solos = []
        i = 0
        for x in self.members:
            solos.append(self.members[i].solo)
            i += 1

        return solos


class Musician(Band):

    instrument = ''

    solo = ''

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo


class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    instrument = 'guitar'

    solo = "face melting guitar solo"


class Bassist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    instrument = 'bass'

    solo = "bom bom buh bom"


class Drummer(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    instrument = 'drums'

    solo = "rattle boom crash"


