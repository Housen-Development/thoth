from django.urls import path

from . import views

app_name = 'parts-manager'
urlpatterns = [
    path('', views.PartsListView.as_view(), name='parts_list'),
    path('<int:pk>/', views.PartsDetailView.as_view(), name='detail'),
    path('inout-history/', views.PartsInOutHistoryView.as_view(), name='inout-history'),
    path('inout-history/new/', views.PartsInOutCreateView.as_view(), name='new-inout-history'),
    path('inout-history/<int:pk>/', views.PartsInOutUpdateView.as_view(), name='edit-inout-history'),
    path('inout-history/<int:pk>/delete/', views.PartsInOutDeleteView.as_view(), name='delete-inout-history'),
]
