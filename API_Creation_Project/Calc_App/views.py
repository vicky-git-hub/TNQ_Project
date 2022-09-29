from django.shortcuts import render
from Calc_App.models import api_creation_db
from datetime import datetime


def get_ip(request):
    ip = request.META.get("HTTP_X_FORWARDED_FOR")
    if ip is None:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def home(request):
    return render(request, 'home.html')


def JSON_view(request):
    num1 = int(request.POST['inputA'])
    num2 = int(request.POST['inputB'])

    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2

    try:
        division = num1 / num2
        div = round(division, 4)
    except ZeroDivisionError:
        div = 0

    # Getting request(user) ip address
    ip_address = get_ip(request)

    # getting request time
    request_time = datetime.now().strftime("%d-%m-%y, %I:%M:%S %p")

    result = [
        {'inputA': num1,
         'inputB': num2,
         'Addition': add,
         'Subtraction': sub,
         'Multiplication': mul,
         'Division': div,
         'IP_Address': ip_address,
         'request_time': request_time}
    ]

    # storing data into db
    sd = api_creation_db()

    sd.request_time = request_time
    sd.ip_address = ip_address
    sd.inputA = num1
    sd.inputB = num2
    sd.sum = add
    sd.subtraction = sub
    sd.multiplication = mul
    sd.division = div
    sd.save()

    return render(request, 'JSON_result.html', {'Result': result})
