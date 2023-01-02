#Sebagai Kartu ATM

class ATMCard:
    def __init__ (self, defaultPin, defaultSaldo):
        self.defaultPin = defaultPin
        self.defaultSaldo = defaultSaldo
    
    #mengembalikan nilai defaultPin
    def cekPinAwal(self):
        return self.defaultPin

    #mengembalikan nilai defaultSaldo
    def cekSaldoAwal(self):
        return self.defaultSaldo