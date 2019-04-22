class Field:

    def __init__(self, name, byte_size, field_type, value=None):
        self.name = name
        self.byte_size = byte_size
        self.type = field_type
