from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.ticket_promedio, name='ticket_promedio'),

]
