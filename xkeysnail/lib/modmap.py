class Modmap:
    def __init__(self, name, mappings):
        self.name = name
        self.mappings = mappings
        self.conditional = None

    def __contains__(self, key):
        return key in self.mappings

    def __getitem__(self, item):
        return self.mappings[item]
    