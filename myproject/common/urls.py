from django.urls import path
from . import views

urlpatterns=[
    path('add_budget',views.add_budget),
    path('add_debit',views.add_debit),
    path('add_credit',views.add_credit),
    path('card_detail/', views.card_detail),
    path('total_income/', views.total_income),
    path('total_expense/', views.total_expense),
    path('list_expense',views.list_expense),
    path('list_income',views.list_income)

]