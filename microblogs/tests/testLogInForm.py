from django.test import TestCase
from django import forms
from microblogs.forms import logInForm

class logInFormTestCase(TestCase):
    def setUp(self):
        self.form_input = {'username': '@frejlordsFinest', 'password': 'Bristles123'}

    def testFormContainsRequiredFields(self):
        form = logInForm()
        self.assertIn('username', form.fields)
        self.assertIn('password', form.fields)
        password_field = form.fields['password']
        self.assertTrue(isinstance(password_field.widget, forms.PasswordInput))

    def testFormAcceptsValidInput(self):
        form = logInForm(data = self.form_input)
        self.assertTrue(form.is_valid())

    def testFormRejectsBlankUsername(self):
        self.form_input['username'] = ''
        form = logInForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    def testFormRejectsBlankPassword(self):
        self.form_input['password'] = ''
        form = logInForm(data = self.form_input)
        self.assertFalse(form.is_valid())

    def testFormAcceptsIncorrectUsername(self):
        self.form_input['username'] = 'frejlordsFinest'
        form = logInForm(data = self.form_input)
        self.assertTrue(form.is_valid())

    def testFormAcceptsIncorrectPassword(self):
        self.form_input['username'] = 'jdkshdksaj'
        form = logInForm(data = self.form_input)
        self.assertTrue(form.is_valid())
