import unittest

from ciphers.caesar import Caesar


class TestCaesar(unittest.TestCase):

    def test_encrypt(self):
        text = "ABCDEF"
        decrypts = [
            "ABCDEF",  # 0
            "BCDEFG",  # 1
            "FGHIJK",  # 5
            "ZABCDE",  # 25

        ]

        for i, key in enumerate([0, 1, 5, 25]):
            self.assertEqual(Caesar(key).encrypt(text), decrypts[i])

    def test_decrypt(self):
        text2 = "ZABCDE"
        encrypts2 = [
            "ZABCDE",  # 0
            "YZABCD",  # 1
            "UVWXYZ",  # 5
            "ABCDEF",  # 25

        ]

        for i, key in enumerate([0, 1, 5, 25]):
            self.assertEqual(Caesar(key).decrypt(text2), encrypts2[i])


if __name__ == "__main__":
    unittest.main()
