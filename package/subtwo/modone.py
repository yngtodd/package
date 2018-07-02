class Letter:

    def __init__(self, addressee, address):
        self.addressee = addressee 
        self.address = address

    def __repr__(self):
        return f'Letter addressed to {self.addressee}'
