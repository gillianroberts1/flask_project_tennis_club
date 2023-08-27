class Slot:
    def __init__(self, court, start_time, end_time, available=True, id=None):
        self.court = court
        self.start_time = start_time
        self.end_time = end_time
        
        self.available = available
        self.id = id
