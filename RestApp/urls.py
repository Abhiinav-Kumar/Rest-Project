from django.urls import path
from RestApp import views

urlpatterns = [
    path('hello/',views.Myclass.as_view()),
    path('new/',views.Newclass.as_view()),
    path('greetings/',views.Greetings.as_view()),
    path('sum/',views.SumClass.as_view()),
    path('fact/',views.FactorialClass.as_view()),

]