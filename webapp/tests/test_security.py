import unittest
from webapp.api.security import SecurityManager

class TestSecurity(unittest.TestCase):

    def setUp(self):
        self.security_manager = SecurityManager()

    def test_password_encryption(self):
        password = "test_password"
        encrypted_password = self.security_manager.encrypt_password(password)
        self.assertNotEqual(password, encrypted_password, "Password encryption failed")

    def test_password_decryption(self):
        password = "test_password"
        encrypted_password = self.security_manager.encrypt_password(password)
        decrypted_password = self.security_manager.decrypt_password(encrypted_password)
        self.assertEqual(password, decrypted_password, "Password decryption failed")

    def test_user_authentication(self):
        username = "test_user"
        password = "test_password"
        self.security_manager.create_user(username, password)
        is_authenticated = self.security_manager.authenticate_user(username, password)
        self.assertTrue(is_authenticated, "User authentication failed")

    def test_invalid_user_authentication(self):
        username = "invalid_user"
        password = "invalid_password"
        is_authenticated = self.security_manager.authenticate_user(username, password)
        self.assertFalse(is_authenticated, "Invalid user was authenticated")

if __name__ == "__main__":
    unittest.main()