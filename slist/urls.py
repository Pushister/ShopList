from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<item_id>/buy', views.add_item, name='buy item'),
    path('<item_id>/remove', views.add_item, name='remove item'),
    #path('add_shop', views.add_shop, name='add shop'),
    #path('add_user', views.add_user, name='add user'),
    #path('analytics', views.analytics, name='analytics'),
]