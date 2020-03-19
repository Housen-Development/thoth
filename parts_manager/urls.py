from django.urls import path

from . import views

app_name = 'parts_manager'
urlpatterns = [
    path('', views.parts_list, name='parts_list'),
    path('<int:parts_id>/', views.parts_detail, name='parts_detail')
]
