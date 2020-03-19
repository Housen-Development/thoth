from django.urls import path

from . import views

app_name = 'parts_manager'
urlpatterns = [
    path('', views.PartsListView.as_view(), name='parts_list'),
    path('<int:pk>/', views.PartsDetailView.as_view(), name='parts_detail')
]
