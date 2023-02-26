from django.shortcuts import render
from django.http import HttpResponse
from .models import ShoppingList, UserList, MallList, Item

# Create your views here.


def index(request):
    user_list = UserList.objects.filter(user_id=1).first()
    result = ShoppingList.objects.filter(list_id=user_list.list_id)

    new_result = [itm.__dict__ for itm in result]
    return HttpResponse(str(new_result))


def add_item(request):
    return HttpResponse("Add item")


def buy_item(request, item_id):
    return HttpResponse("Buy item")


def remove_item(request, item_id):
    return HttpResponse("Remove item")


def add_shop(request):
    return HttpResponse("Add shop")


def add_user(request):
    return HttpResponse("Add shop")


def analytics(request):
    return HttpResponse("Analytics")
