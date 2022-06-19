from django.test import TestCase
from .models import *

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='morces', password='hdbhdvdyd')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class PostTest(TestCase):
    def setUp(self):
        self.user = Profile.objects.create(id=1, name='morces')
        self.post = Post.objects.create(id=1, title='test post', post='post', user=self.user)

    def test_instance(self):
        self.assertFalse(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post)>0)

class Neighborhood(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Morces')

    def test_instance(self):
        self.assertFalse(isinstance(self.user, Neighborhood))

    def test_save_neighborhood(self):
        self.neighborhood.save_neighborhood()
        hood = Neighborhood.objects.all()
        self.assertTrue(len(hood)>0)

class Business(TestCase):
    def setUp(self):
        self.user = User.objects.all()

    def test_save_business(self):
        self.business.save_business()
        bus = Business.objects.all()
        self.assertTrue(len(bus)>0)
