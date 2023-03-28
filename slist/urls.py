from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<item_id>/buy', views.add_item, name='add item'),
    path('<item_id>/remove', views.remove_item, name='remove item'),
]