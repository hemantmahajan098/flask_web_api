from datetime import datetime
from flask import Flask,request,json,Response
from flask_restful import Resource, Api, abort
from process_payment.creditcardinfo import CreditCardInfo
from process_payment.controller import BusinessLogic

app = Flask(__name__)
api = Api(app)

class ProcessPayment(Resource):
    def post(self,payment_id):
        CreditCardNumber = str(request.form['CreditCardNumber'])
        CardHolder = str(request.form['CardHolder'])
        ExpirationDate = datetime.strptime(request.form['ExpirationDate'], '%d/%m/%Y')
        Amount = float(request.form['Amount'])
        SecurityCode = str(request.form['SecurityCode'])
        try:
            credit_card_info = CreditCardInfo(CreditCardNumber, CardHolder, ExpirationDate, Amount,
                                          SecurityCode=SecurityCode)
        except (ValueError,TypeError) as e :
            return {'The request is invalid': '400 bad request'}
        bll_obj = BusinessLogic()
        res = bll_obj.decidingPaymentGateway(credit_card_info)
        if res == True:
            return {'Payment for payment id = {} is processed'.format(payment_id): '200 ok'}
        return {'message': 'fail'}


api.add_resource(ProcessPayment, '/ProcessPayment/<int:payment_id>')

if __name__ == '__main__':
    app.run()
