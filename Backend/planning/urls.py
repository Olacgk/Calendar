from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('',views.HelloPlanView.as_view(),name='hello_plan'),
]