from django.test import TestCase
from django.urls import reverse
from microblogs.models import User
from .helpers import LogInTester

class logOutViewTestCase(TestCase, LogInTester):
    def setUp(self):
        self.url = reverse('log_out')
        self.user = User.objects.create_user('@bobby9',
        first_name = 'bobby',
        last_name = 'dazzla',
        email = 'ournumber9@lfc.com',
        password = 'Whiteteeth123',
        bio = 'give the ball to bobby and he`ll score.',
        is_active = True
        )

    def testLogOutURL(self):
        self.assertEqual(self.url,'/log_out/')

    def testGetLogOut(self):
        self.client.login(username = '@bobby9', password= 'Whiteteeth123')
        self.assertTrue(self.isLoggedIn())
        response = self.client.get(self.url, follow=True)
        response_url = reverse('home')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertFalse(self.isLoggedIn())
