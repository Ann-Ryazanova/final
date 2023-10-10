from django.urls import path

from client.apps import ClientConfig
from client.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = ClientConfig.name

urlpatterns = [
    path('create/', ClientCreateView.as_view(), name='create_client'),
    path('', ClientListView.as_view(), name='list'),
    path('view/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('edit/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
]
