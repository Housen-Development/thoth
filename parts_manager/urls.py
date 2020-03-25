from django.urls import path

from . import views

app_name = 'parts_manager'
urlpatterns = [
    path('', views.PartsListView.as_view(), name='parts_list'),
    path('<int:pk>/', views.PartsDetailView.as_view(), name='detail'),
    path('inout_history/', views.PartsInOutHistoryView.as_view(), name='inout_history'),
    path('inout_history/new/', views.PartsInOutCreateView.as_view(), name='new_inout_history'),
    path('inout_history/<int:pk>/', views.PartsInOutUpdateView.as_view(), name='edit_inout_history'),
    path('inout_history/<int:pk>/delete/', views.PartsInOutDeleteView.as_view(), name='delete_inout_history'),
]
