class PaymentGateway(object):
    def CheapPaymentGateway(self, amount):
        if int(amount) < 20:
            return True
        return False
    def PremiumPaymentGateway(self,amount):
        if 21 < int(amount) < 500:
            return True
        return False
    def ExpensivePaymentGateway(self,amount):
        if int(amount) >500:
            return True
        return False
