class Member:

    def __init__(self, name, address, postcode, tel_no, email, dob, premium=None, win = None, loss = None, id = None):
        self.name = name
        self.address = address
        self.postcode = postcode
        self.tel_no = tel_no
        self.email = email
        self.dob = dob
        self.premium = premium
        self.win = win
        self.loss = loss
        self.id = id