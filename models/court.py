class Court:

    def __init__(self, court_no, surface, id = None):
        self.court_no = court_no
        self.surface = surface
        self.capacity = 4
        self.id = id