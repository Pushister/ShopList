from django.shortcuts import render
from django.http import HttpResponse
from slist.models import ShoppingList, UserList, MallList, Item
from django.shortcuts import redirect
from django.conf import settings


# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
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

    result = list(ShoppingList.objects.filter(list_id=user_list.list_id,
                                              status='available').all())

    return render(request, 'item_form.html', {'shopping_list_data': result,
                                              "shops": MallList.objects.all()})


def add_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    if request.method == 'POST':
        user_list = UserList.objects.filter(user_id=1).first()
        price = request.POST.get('price')
        status = 'bought'
        buy_date = request.POST.get('date')
        quantity_obj = ShoppingList.objects.filter(item_id=item_id).first()
        shop_obj = ShoppingList(list_id=user_list.list_id,
                                item_id_id=item_id,
                                quantity=quantity_obj.quantity,
                                price=price,
                                status=status,
                                buy_date=buy_date,
                                )
        shop_obj.save()

    return render(request, 'success.html')


def remove_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    if request.method == 'POST':
        item_obj = ShoppingList.objects.filter(item_id_id=item_id)
        item_obj.delete()

    return redirect('/shopping_list/')


def add_shop(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    return HttpResponse("Add shop")


def add_user(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    return HttpResponse("Add shop")


def analytics(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    return HttpResponse("Analytics")
