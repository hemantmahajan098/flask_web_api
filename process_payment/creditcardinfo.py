import datetime


class CreditCardInfo(object):
    def __init__(self, CreditCardNumber, CardHolder, ExpirationDate, Amount, SecurityCode='999'):
        self.CreditCardNumber = CreditCardNumber
        self.CardHolder = CardHolder
        self.ExpirationDate = ExpirationDate
        self.Amount = Amount
        self.SecurityCode = SecurityCode

    @property
    def CreditCardNumber(self):
        return self._CreditCardNumber
    @CreditCardNumber.setter
    def CreditCardNumber(self,val):
        if not isinstance(val,str):
            raise TypeError('Credit Card number should be of string type')
        elif  len(val) !=16:
            raise ValueError('Credit card number should contain 16 digits')
        else:
            self._CreditCardNumber = val

    @property
    def CardHolder(self):
        return self._CardHolder

    @CardHolder.setter
    def CardHolder(self, val):
        if not isinstance(val, str):
            raise TypeError('Card holder should be of string type')
        else:
            self._CardHolder = val

    @property
    def ExpirationDate(self):
        return self._ExpirationDate

    @ExpirationDate.setter
    def ExpirationDate(self, val):
        if not isinstance(val, datetime.datetime):
            raise TypeError('Expiration date should be in date format')
        elif val < datetime.datetime.today():
            raise ValueError('the value of expiration date should be in the future')
        else:
            self._ExpirationDate = val

    @property
    def SecurityCode(self):
        return self._SecurityCode

    @SecurityCode.setter
    def SecurityCode(self, val):
        if not isinstance(val, str):
            raise TypeError('Security Code should be of string type')
        elif len(val) != 3:
            raise ValueError('Security Code should contain 3 digits')
        else:
            self._SecurityCode = val

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, val):
        if not isinstance(val, float):
            raise TypeError('Amount should be of float type')
        elif val < 0:
            raise ValueError('Amount should be greater than or equal to zero')
        else:
            self._Amount = val

if __name__ =='__main__':
    dict1= {'CreditCardNumber': '9999888877776666', 'CardHolder': 'abc', 'ExpirationDate': '25/09/2025',
       'SecurityCode': '123', 'Amount': 40.0}
    obj1=CreditCardInfo(dict1['CreditCardNumber'],dict1['CardHolder'],datetime.datetime.strptime(dict1['ExpirationDate'],'%d/%m/%Y'),dict1['Amount'],SecurityCode=dict1['SecurityCode'])