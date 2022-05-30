class event:
    def __init__(self, id, name, description, event_type, return_type, args):
        self.id = id
        self.name = name
        self.description = description
        self.event_type = event_type
        self.return_type = return_type
        self.args = args