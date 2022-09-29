from django.urls import path
from .views import CompaniaView

urlpatterns=[
    path('empleados/',CompaniaView.as_view(), name='list'),
    path('empleados/<int:id>',CompaniaView.as_view(), name='empleados-process')
]