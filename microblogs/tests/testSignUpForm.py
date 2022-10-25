from django.test import TestCase
from microblogs.forms import signUpForm
from microblogs.models import User
from django import forms
from django.contrib.auth.hashers import check_password

class signUpTestCase(TestCase):
    def setUp(self):
        self.formInput = {
            'first_name': 'mommy',
            'last_name': 'sej',
            'username': '@frejlordsFinest',
            'email': 'SejuaniBiryani@frejlord.com',
            'bio': 'bristles <3',
            'new_password': 'Bristles123',
            'password_confirmation': 'Bristles123'
        }
    def testValidSignUpForm(self):
        form = signUpForm(data=self.formInput)
        self.assertTrue(form.is_valid())

    def testFormHasNecessaryFields(self):
        form = signUpForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('username', form.fields)
        self.assertIn('bio', form.fields)
        self.assertIn('email', form.fields)
        self.assertIn('new_password', form.fields)
        self.assertIn('password_confirmation', form.fields)
        emailField = form.fields['email']
        self.assertTrue(isinstance(emailField, forms.EmailField))
        newPasswordWidget = form.fields['new_password'].widget
        self.assertTrue(isinstance(newPasswordWidget, forms.PasswordInput))
        passwordConfirmationWidget = form.fields['password_confirmation'].widget
        self.assertTrue(isinstance(passwordConfirmationWidget, forms.PasswordInput))

    def testModelValidation(self):
        self.formInput['username'] = 'frejlordsFinest'
        form = signUpForm(data=self.formInput)
        self.assertFalse(form.is_valid())

    def testPasswordContainsUpperCase(self):
        self.formInput['new_password'] = 'bristles123'
        self.formInput['new_password'] = 'bristles123'
        form = signUpForm(data=self.formInput)
        self.assertFalse(form.is_valid())

    def testPasswordContainslowerCase(self):
        self.formInput['new_password'] = 'BRISTLES123'
        self.formInput['new_password'] = 'BRISTLES123'
        form = signUpForm(data=self.formInput)
        self.assertFalse(form.is_valid())

    def testPasswordContainsNumber(self):
        self.formInput['new_password'] = 'Bristles'
        self.formInput['new_password'] = 'Bristles'
        form = signUpForm(data=self.formInput)
        self.assertFalse(form.is_valid())

    def testPasswordInputsAreIdentical(self):
        self.formInput['password_confirmation'] = 'Bristles12'
        form = signUpForm(data=self.formInput)
        self.assertFalse(form.is_valid())

    def testFormMustSaveCorrectly(self):
        form = signUpForm(data=self.formInput)
        beforeCount = User.objects.count()
        form.save()
        afterCount = User.objects.count()
        self.assertEqual(afterCount, beforeCount+1)
        user = User.objects.get(username = '@frejlordsFinest')
        self.assertEqual(user.last_name, 'sej')
        self.assertEqual(user.email, 'SejuaniBiryani@frejlord.com')
        self.assertEqual(user.first_name, 'mommy')
        self.assertEqual(user.bio, 'bristles <3')
        isPasswordCorrect = check_password('Bristles123', user.password)
        self.assertTrue(isPasswordCorrect)
