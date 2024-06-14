from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime,math
# Create your views here.

class Myclass(APIView):
    def get(self,request):
        return Response({'Message':'Introduction to DRF'})

class Newclass(APIView):
    def get(self,request):
        return Response({'Message':'Ente manakeleke swagatham'})
class Greetings(APIView):
    def get(self,request):

        msg = ''
        now = datetime.datetime.now()
        current_hour = now.hour
        if current_hour <= 11:
            msg = 'GOOD MORNING'
        elif current_hour < 15:
            msg = 'GOOD AFTERNOON'
        elif current_hour < 19:
            msg = 'GOOD EVENING'
        else:
            msg = 'GOOD NIGHT'

        return Response({'Hello,':msg})

class SumClass(APIView):
    def post(self,request):
        print(request.data)
        x = request.data.get('num1')
        y = request.data.get('num2')
        sum = x + y
        deff = x - y
        pro = x * y
        quo = x / y
        return Response({'Sum':sum,'Difference':deff,'Product':pro,'Quotient':quo})

class FactorialClass(APIView):
    def post(self,request):
        x = request.data.get('num')
        fact = math.factorial(x)
        return Response({'Factorial':fact})