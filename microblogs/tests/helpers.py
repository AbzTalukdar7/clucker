class LogInTester():
    def isLoggedIn(self):
        return '_auth_user_id' in self.client.session.keys()
