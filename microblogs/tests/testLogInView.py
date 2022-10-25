from django.test import TestCase
from microblogs.forms import logInForm
from django.urls import reverse

class logInViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('log_in')

    def testLogInURL(self):
        self.assertEqual(self.url,'/log_in/')

    def testGetLogIn(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'log_in.html')
        form = response.context['form']
        self.assertTrue(isinstance(form,logInForm))
        self.assertFalse(form.is_bound)
