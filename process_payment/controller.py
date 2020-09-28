from process_payment.externalpaymentproviders import PaymentGateway
class BusinessLogic(object):
    def decidingPaymentGateway(self,creditcard_obj):
        payment_gateway_obj = PaymentGateway()
        amount = creditcard_obj.Amount
        if int(amount) < 20:
            if (payment_gateway_obj.CheapPaymentGateway(amount)):
                return True
            return False
        elif 21 <int(amount)<500:
            if (payment_gateway_obj.PremiumPaymentGateway(amount)):
                return True
            return False
        elif int(amount)>500:
            if (payment_gateway_obj.ExpensivePaymentGateway(amount)):
                return True
            return False
