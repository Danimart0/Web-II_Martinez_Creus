# polls/views.py
from django.shortcuts import render
from .models import Question
from .models import Choice
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def indexOrders(request):
    data = {
        "titulo" : "Id de las orders",
        "total_orders" : 100,
        "total_payments" : 200,
        "orders":[
            {
                "id": 1 , "total" : 100
            },
            {
                "id" : 2 , "total" : 200
            },
            {
                "id" : 3 , "total" : 300
            },
            {
                "id" : 4 , "total" : 400
            }
        ]
    }
    return render(request, 'polls/index.html', data)

def choice_list(request):
    choices = Choice.objects.all()
    return render(request, "polls/choices.html", {"choices": choices})