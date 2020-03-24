from django.urls import path

from . import views

app_name = 'parts_manager'
urlpatterns = [
    path('', views.PartsListView.as_view(), name='parts_list'),
    path('<int:pk>/', views.PartsDetailView.as_view(), name='detail'),
    path('inout_history/', views.PartsInOutHistoryView.as_view(), name='inout_history'),
    path('inout_history/<int:pk>/', views.EditPartsInOutFormView.as_view(), name='edit_inout_history'),
]
