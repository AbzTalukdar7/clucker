from django.test import TestCase
from .models import User
from django.core.exceptions import ValidationError

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@bobby9',
            first_name = 'bobby',
            last_name = 'dazzla',
            email = 'ournumber9@lfc.com',
            password = 'whiteteeth123',
            bio = 'give the ball to bobby and he`ll score.'
        )
#------------Username Tests------------------------------------
    def testValidUser(self):
        self.assertUserIsValid()

    def testBlankUsername(self):
        self.user.username = ''
        self.assertUserIsInvalid()

    def testUsernameCanBe30CharsLong(self):
        self.user.username = '@' + 'a' *29
        self.assertUserIsValid()

    def testUsernameCantBe31CharsLong(self):
        self.user.username = '@' + 'a' *30
        self.assertUserIsInvalid()

    def testUsernameIsUnique(self):
        secondUser = self.CreatSecondUser()
        self.user.username = secondUser.username
        self.assertUserIsInvalid()

    def testUsernameStartsWithAT(self):
        self.user.username = 'johndoe'
        self.assertUserIsInvalid()

    def testUsernameContainsOnlyAlphaNumericals(self):
        self.user.username = '@john!doe'
        self.assertUserIsInvalid()

    def testUsernameContainsAtleast3Alphanumericals(self):
        self.user.username = '@jo'
        self.assertUserIsInvalid()

    def testUsernameCanContainNumbers(self):
        self.user.username = '@jo2ee3'
        self.assertUserIsValid()

    def testUsernameCanContainOnly1AT(self):
        self.user.username = '@@jo2ee3'
        self.assertUserIsInvalid()

#------------first name Tests------------------------------------
    def testBlankFirstName(self):
        self.user.first_name = ''
        self.assertUserIsInvalid()

    def testFirstNameCanBe50CharsLong(self):
        self.user.first_name = 'a' *50
        self.assertUserIsValid()

    def testFirstNameCanBe51CharsLong(self):
        self.user.first_name = 'a' *51
        self.assertUserIsInvalid()

    def testFirstNameCanContainSpecialChars(self):
        self.user.first_name = 'monkey@#$%^'
        self.assertUserIsInvalid()

    def testAllowedSameFirstName(self):
        secondUser = self.CreatSecondUser()
        self.user.first_name = secondUser.first_name
        self.assertUserIsValid()

#------------last name Tests------------------------------------
    def testBlankLastName(self):
        self.user.last_name = ''
        self.assertUserIsInvalid()

    def testLastNameCanBe50CharsLong(self):
        self.user.last_name = 'a' *50
        self.assertUserIsValid()

    def testLastNameCanBe51CharsLong(self):
        self.user.last_name = 'a' *51
        self.assertUserIsInvalid()

    def testLastNameCanContainSpecialChars(self):
        self.user.last_name = 'monkey@#$%^'
        self.assertUserIsInvalid()

    def testAllowedSameLastName(self):
        secondUser = self.CreatSecondUser()
        self.user.last_name = secondUser.last_name
        self.assertUserIsValid()

#------------email Tests------------------------------------
    def testBlankEmail(self):
        self.user.email = ''
        self.assertUserIsInvalid()

    def testEmailCanHave2ATs(self):
        self.user.email = 'hi@@domain.com'
        self.assertUserIsInvalid()

    def testEmailCanHaveNoDomain(self):
        self.user.email = 'test@.com'
        self.assertUserIsInvalid()

    def testEmailCanHaveNoDot(self):
        self.user.email = 'test@domain'
        self.assertUserIsInvalid()

    def testEmailCanHaveNothingBeforeAT(self):
        self.user.email = '@domain.com'
        self.assertUserIsInvalid()

    def testAllowedSameEmail(self):
        secondUser = self.CreatSecondUser()
        self.user.email = secondUser.email
        self.assertUserIsInvalid()

#------------bio Tests------------------------------------
    def testBlankBio(self):
        self.user.bio = ''
        self.assertUserIsValid()

    def testSameBio(self):
        secondUser = self.CreatSecondUser()
        self.user.bio = secondUser.bio
        self.assertUserIsValid()

    def testBioWith520Chars(self):
        self.user.bio = 'a' * 520
        self.assertUserIsValid()

    def testBioWith521Chars(self):
        self.user.bio = 'a' * 521
        self.assertUserIsInvalid()

#---------------------------------------------------------
    def assertUserIsValid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')

    def assertUserIsInvalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def CreatSecondUser(self):
        user = User.objects.create_user(
            '@dn27',
            first_name = 'darwin',
            last_name = 'nunyeyyyz',
            email = 'clumsy27@lfc.com',
            password = 'waffleboy27',
            bio = 'noooooonez, nooooooonez'
        )
        return user
