from django.test import TestCase
from microblogs.forms import logInForm
from django.urls import reverse
from microblogs.models import User
from .helpers import LogInTester
from django.contrib import messages

class logInViewTestCase(TestCase, LogInTester):
    def setUp(self):
        self.url = reverse('log_in')
        self.user = User.objects.create_user('@bobby9',
        first_name = 'bobby',
        last_name = 'dazzla',
        email = 'ournumber9@lfc.com',
        password = 'Whiteteeth123',
        bio = 'give the ball to bobby and he`ll score.',
        is_active = True
        )

    def testLogInURL(self):
        self.assertEqual(self.url,'/log_in/')

    def testGetLogIn(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,logInForm))
        self.assertFalse(form.is_bound)
        messagesList = list(response.context['messages'])
        self.assertEqual(len(messagesList),0)

    def testUnsuccessfulLogIn(self):
        form_input = {'username': '@bobby9', 'password': 'Wrongpass12'}
        response = self.client.post(self.url, form_input)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,logInForm))
        self.assertFalse(form.is_bound)
        self.assertFalse(self.isLoggedIn())
        messagesList = list(response.context['messages'])
        self.assertEqual(len(messagesList),1)
        self.assertEqual(messagesList[0].level, messages.ERROR)

    def testSuccessfulLogIn(self):
        form_input = {'username': '@bobby9', 'password': 'Whiteteeth123'}
        response = self.client.post(self.url, form_input, follow = True)
        self.assertTrue(self.isLoggedIn())
        response_url = reverse('feed')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'feed.html')
        messagesList = list(response.context['messages'])
        self.assertEqual(len(messagesList),0)

    def testValidLogInByInactiveUser(self):
        self.user.is_active = False
        self.user.save()
        form_input = {'username': '@bobby9', 'password': 'Whiteteeth123'}
        response = self.client.post(self.url, form_input, follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,logInForm))
        self.assertFalse(form.is_bound)
        self.assertFalse(self.isLoggedIn())
        messagesList = list(response.context['messages'])
        self.assertEqual(len(messagesList),1)
        self.assertEqual(messagesList[0].level, messages.ERROR)
