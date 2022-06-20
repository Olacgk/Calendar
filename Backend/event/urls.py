from django.urls import URLPattern, path
from . import views

urlpatterns =[
    path('',views.HelloEventView.as_view(),name='hello_event'),
]