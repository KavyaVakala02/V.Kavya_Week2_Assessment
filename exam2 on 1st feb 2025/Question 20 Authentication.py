from abc import ABC, abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self, username, password):
        pass
    @abstractmethod
    def logout(self):
        pass
# Implement the GoogleAuth class
class GoogleAuth(UserAuthentication):
    def login(self, username, password):
        return f"Google login successful for {username}."
    def logout(self):
        return "Logged out from Google."
# Implement the FacebookAuth class
class FacebookAuth(UserAuthentication):
    def login(self, username, password):
        return f"Facebook login successful for {username}."
    def logout(self):
        return "Logged out from Facebook."
google_auth = GoogleAuth()
facebook_auth = FacebookAuth()
print(google_auth.login("user1", "password123"))  # Google login
print(google_auth.logout())  # Google logout
print(facebook_auth.login("user2", "password456"))  # Facebook login
print(facebook_auth.logout())  # Facebook logout
