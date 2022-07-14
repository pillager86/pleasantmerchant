from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items', views.item_list_view, name='items'),
    path('logout', views.logout_view, name='logout'),
    path('permission', views.permission_denied_view, name='permissiondenied'),
]