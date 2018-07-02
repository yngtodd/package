from datetime import date


class TimeCapsule:

    def __init__(self, location):
        self.location = location
        self.today = date.today().strftime('%y-%m-%d')

    def __repr__(self):
        return f'Time capsule buried at {self.location} on {self.today}'
