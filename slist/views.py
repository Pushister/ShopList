from django.shortcuts import render
from django.http import HttpResponse
from .models import ShoppingList, UserList, MallList, Item

# Create your views here.


def index(request):
    user_list = UserList.objects.filter(user_id=1).first()

    if request.method == 'POST':
        item_name = request.POST.get('item')
        amount = request.POST.get('amount')
        shop_id = request.POST.get('shop')
        shop_obj = MallList.objects.filter(pk=int(shop_id)).first()
        item_obj = Item(name=item_name, shop_id=shop_obj)
        item_obj.save()

        new_item = ShoppingList(list_id=user_list.list_id, item_id=item_obj, quantity=amount)
        new_item.save()

    result = list(ShoppingList.objects.filter(list_id=user_list.list_id).all())

    return render(request, 'item_form.html', {'shopping_list_data': result,
                                              "shops": MallList.objects.all()})


def add_item(request):
    return render(request, 'add.html')


def buy_item(request, item_id):
    return render(request, 'add.html')


def remove_item(request, item_id):
    return HttpResponse("Remove item")


def add_shop(request):
    return HttpResponse("Add shop")


def add_user(request):
    return HttpResponse("Add shop")


def analytics(request):
    return HttpResponse("Analytics")
