import unittest
from my_project import log2


class TestMyProj(unittest.TestCase):
    def test_valid_login_and_password_passes(self):
        ok, mess = log2("Test_user1", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, True)
        self.assertEqual(mess, "")
        print('\n')

    def test_shortLogin(self):
        ok, mess = log2("abc", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, "Login too short")
        print('\n')

    def test_blacklistLogin(self):
        ok, mess = log2("89999999999", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, "Login is bad(blacklist)")
        print('\n')

    def test_passwSize(self):
        ok, mess = log2("89999999991", "", "")
        self.assertEqual(ok, False)
        self.assertEqual(mess, "Password too short")
        print('\n')

    def test_passwLatin(self):
        ok, mess = log2("89999999919", "Passw123!", "passw123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, "Password with Latin letter")
        print('\n')

    def test_paswBig(self):
        ok, mess = log2("89999999919", "пароль123!", "пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, "Password not big letter")
        print('\n')

    def test_paswSmall(self):
        ok, mess = log2("89999999919", "ПАРОЛЬ123!", "ПАРОЛЬ123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, "Password not small letter")
        print('\n')

    def test_paswNum(self):
        ok, mess = log2("89999999919", "Пароль!", "Пароль!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, "Password not numbers")
        print('\n')

    def test_paswSimv(self):
        ok, mess = log2("89999999919", "Пароль123", "Пароль123")
        self.assertEqual(ok, False)
        self.assertEqual(mess, "Password not special simbols")
        print('\n')

    def test_paswSecond(self):
        ok, mess = log2("89999999919", "Пароль123!", "Парольь123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, "Second password not matched")
        print('\n')

    def test_lForm1(self):
        ok, mess = log2("899999991901", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, 'Non correct number format "8xxxxxxxxxx"')
        print('\n')

    def test_lForm2(self):
        ok, mess = log2("+79199999999", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, 'Non correct number format "+7-xxx-xxx-xxxx"')
        print('\n')

    def test_lForm3(self):
        ok, mess = log2("asdasd@afsasfasf", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, 'Non correct email format "exsample@exampl.com"')
        print('\n')

    def test_lForm4(self):
        ok, mess = log2("12342353_", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, 'Login without letter')
        print('\n')

    def test_lForm5(self):
        ok, mess = log2("lolo12lolo", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, 'Login without "_" simbols')
        print('\n')

    def test_lForm6(self):
        ok, mess = log2("hihihihi_", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, "Login without numbers")
        print('\n')

    def test_lForm7(self):
        ok, mess = log2("Яlogin_1233", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, False)
        self.assertEqual(mess, 'Login with cirilic letter')
        print('\n')

    def test_valid_phone8(self):
        ok, mess = log2("89999999919", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, True)
        self.assertEqual(mess, "")

    def test_valid_phoneDashed(self):
        ok, mess = log2("+7-123-456-7890", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, True)
        self.assertEqual(mess, "")

    def test_valid_email(self):
        ok, mess = log2("user@mail.ru", "Пароль123!", "Пароль123!")
        self.assertEqual(ok, True)
        self.assertEqual(mess, "")
if __name__ == "__main__":
    unittest.main()