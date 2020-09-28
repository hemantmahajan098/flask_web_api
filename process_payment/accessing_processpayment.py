import urllib
from urllib import request

payment = {'CreditCardNumber' : '9999888877776666','CardHolder':'abc','ExpirationDate':'25/10/2025','SecurityCode':'123','Amount':40.0}
data = urllib.parse.urlencode(payment)
data = data.encode('ascii')

request1 = request.Request('http://127.0.0.1:5000/ProcessPayment/1', data=data, method='POST')
try:
    response1 = request.urlopen(request1)
    print(response1.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())


payment = {'CreditCardNumber' : '9999888877776666','CardHolder':'abc','ExpirationDate':'25/09/2020','SecurityCode':'123','Amount':510.0}
data = urllib.parse.urlencode(payment)
data = data.encode('ascii')

request2 = request.Request('http://127.0.0.1:5000/ProcessPayment/1', data=data, method='POST')
try:
    response2 = request.urlopen(request2)
    print(response2.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())


payment = {'CreditCardNumber' : '','CardHolder':'abc','ExpirationDate':'25/09/2020','SecurityCode':'123','Amount':510.0}
data = urllib.parse.urlencode(payment)
data = data.encode('ascii')

request3 = request.Request('http://127.0.0.1:5000/ProcessPayment/1', data=data, method='POST')
try:
    response3 = request.urlopen(request3)
    print(response3.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())