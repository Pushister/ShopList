import uuid

from django.test import TestCase
from slist.models import UserList, ShoppingList
from django.contrib.auth.models import User
from django.test import Client


# Create your tests here.


class UserListTestCase(TestCase):
    def setUp(self):
        self.user1_email = 'test_user1@example.com'
        self.user1_name = 'test_user1'
        self.user2_email = 'test_user2@example.com'
        self.user2_name = 'test_user2'

        user1 = User.objects.create_user(self.user1_name, self.user1_email, 'password')
        user1.save()

        user2 = User.objects.create_user(self.user2_name, self.user2_email, 'password')
        user2.save()

        shop_user1_list = UserList(user_id=user1.id, list_id=uuid.uuid4())
        shop_user1_list.save()

        shop_user2_list = UserList(user_id=user2.id, list_id=uuid.uuid4())
        shop_user2_list.save()

        self.user1_id = user1.id
        self.user2_id = user2.id

    def test_user_list(self):
        c = Client()
        c.login(username=self.user1_name, password='password')
        response = c.post('/user/invite', {'email': self.user2_email})
        self.assertEqual(response.status_code, 200)
        shop_user1_list = UserList.objects.filter(user_id=self.user1_id).first()
        shop_user2_list = UserList.objects.filter(user_id=self.user2_id).first()
        self.assertEqual(shop_user2_list.list_id, shop_user1_list.list_id)

    def test_user_not_exist(self):
        c = Client()
        c.login(username=self.user1_name, password='password')
        response = c.post('/user/invite', {'email': 'user5example.com'})
        self.assertEqual(response.status_code, 404)


class UserRegister(TestCase):
    def test_create_user(self):
        c = Client()

        response = c.post('/user/register',
                          {'username': 'test3_user', 'email': 'user3@example.com', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        user3 = User.objects.filter(username='test3_user').first()
        self.assertIsNotNone(user3)
        user_list3 = UserList.objects.filter(user_id=user3.id).first()
        self.assertIsNotNone(user_list3)

        response = c.post('/user/register',
                          {'username': 'test4_user', 'email': 'user4@example.com', 'password': 'password'})
        self.assertEqual(response.status_code, 302)
        user4 = User.objects.filter(username='test4_user').first()
        self.assertIsNotNone(user3)
        user_list4 = UserList.objects.filter(user_id=user4.id).first()
        self.assertIsNotNone(user_list4)
        self.assertNotEqual(user_list3.list_id, user_list4.list_id)


class TestBuyItem(TestCase):
    fixtures = ['buy_item_fixture.json']

    def test_buy(self):
        shoppinglist = ShoppingList.objects.filter(list_id='6fb6e35d-d501-4cdc-ad69-dfb46e659bd1', item_id=10).all()
        self.assertEqual(len(shoppinglist), 1)
        c = Client()
        c.login(username='User2', password='1111')
        response = c.post('/shopping_list/10/buy', {'item_id': 10})
        shoppinglist2 = ShoppingList.objects.filter(list_id='6fb6e35d-d501-4cdc-ad69-dfb46e659bd1').all()
        self.assertEqual(len(shoppinglist), 1)
        self.assertEqual('bought', shoppinglist2[0].status)


