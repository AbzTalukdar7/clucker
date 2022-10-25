from django.test import TestCase
from microblogs.forms import signUpForm
from django.urls import reverse
from microblogs.models import User
from django.contrib.auth.hashers import check_password
from .helpers import LogInTester

class signUpViewTestCase(TestCase, LogInTester):

    def setUp(self):
        self.url = reverse('sign_up')
        self.formInput = {
            'first_name': 'mommy',
            'last_name': 'sej',
            'username': '@frejlordsFinest',
            'email': 'SejuaniBiryani@frejlord.com',
            'bio': 'bristles <3',
            'new_password': 'Bristles123',
            'password_confirmation': 'Bristles123'
        }

    def testSignUpURL(self):
        self.assertEqual(self.url,'/sign_up/')

    def testGetSignUp(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,signUpForm))
        self.assertFalse(form.is_bound)

    def testUnsuccessfulSignUp(self):
        self.formInput['username'] = 'BAD_USERNAME'
        beforeCount = User.objects.count()
        response = self.client.post(self.url, self.formInput)
        afterCount = User.objects.count()
        self.assertEqual(afterCount, beforeCount)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign_up.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,signUpForm))
        self.assertTrue(form.is_bound)
        self.assertFalse(self.isLoggedIn())

    def testSuccessfulSignUp(self):
        beforeCount = User.objects.count()
        response = self.client.post(self.url, self.formInput, follow = True)
        afterCount = User.objects.count()
        self.assertEqual(afterCount, beforeCount+1)
        response_url = reverse('feed')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'feed.html')
        user = User.objects.get(username = '@frejlordsFinest')
        self.assertEqual(user.last_name, 'sej')
        self.assertEqual(user.email, 'SejuaniBiryani@frejlord.com')
        self.assertEqual(user.first_name, 'mommy')
        self.assertEqual(user.bio, 'bristles <3')
        isPasswordCorrect = check_password('Bristles123', user.password)
        self.assertTrue(isPasswordCorrect)
        self.assertTrue(self.isLoggedIn())
