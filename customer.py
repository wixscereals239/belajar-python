#Sebagai Nasabah
from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin = 1234, custSaldo = 100000):
        self.id = id
        self.custPin = custPin
        self.custSaldo = custSaldo
    
    def cekId(self):
        return self.id

    def cekPin(self):
        return self.custPin

    def cekSaldo(self):
        return self.custSaldo

    def tarikSaldo(self, nominal):
        self.custSaldo -= nominal

    def setorSaldo(self, nominal):
        self.custSaldo += nominal