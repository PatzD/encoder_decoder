import unittest
import functions_for_testing as functions


class TestFunctions(unittest.TestCase):

    # test word for special character, returns True if special character found returns bool
    def test_check_special_character(
        self,
    ):  
        self.assertEqual(functions.check_special_character("hello"), True)
        self.assertEqual(functions.check_special_character("hello!@"), False)
        self.assertEqual(functions.check_special_character("hello world"), True)

    #randomize characters in word if possible, returns scrambled or original word
    def test_scramble_word(self):
        self.assertEqual(functions.scramble_word("heo"), "heo")
        self.assertEqual(functions.scramble_word("hello!@"), "hello!@")
        self.assertEqual(functions.scramble_word("ds"), "ds")
        self.assertNotEqual(functions.scramble_word("hello"), "hello")

    #encode sentence, takes in sentence returns encoded sentence and original sentence
    def test_encode_sentence(self):
        self.assertEqual(
            functions.encode_sentance("hey how are you"),
            ("\n-weird-\n", "hey how are you", "\n-weird-\n", "are hey how you"),
        )
        self.assertEqual(
            functions.encode_sentance("hey how# are you"),
            ("\n-weird-\n", "hey how# are you", "\n-weird-\n", "are hey how# you"),
        )
        self.assertEqual(
            functions.encode_sentance("asd #das dad"),
            ("\n-weird-\n", "asd #das dad", "\n-weird-\n", "#das asd dad"),
        )
        self.assertNotEqual(
            functions.encode_sentance("This is a test"),
            ("\n-weird-\n", "This is a test", "\n-weird-\n", "a is test This"),
        )
    
    #decode sentence, takes in encoded and original ordered alphabeticall sentence returns decoded sentence
    def test_decoder(self):
        self.assertEqual(functions.decoder("Abc abc ab", "ab abc Abc"), "Abc abc ab")
        self.assertEqual(functions.decoder("hlleo how are you dinog", "are doing hello how you"), "hello how are you doing")
        self.assertEqual(functions.decoder("asd #das dad", "#das asd dad"), "asd #das dad")
        self.assertNotEqual(functions.decoder("This is a test", "a is test This"), "Thes is a test")


if __name__ == "__main__":
    unittest.main()  # run all tests
