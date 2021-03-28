import unittest
from translator import Translator
from languages import orcish, common, debug


class LanguageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.orcish_translator = Translator(orcish)
        self.common_translator = Translator(common)
        self.debug_translator = Translator(debug)
        self.message = "ABCDefЙцук1234іІєї!#\""

    def test_orcish_to_orcish(self):
        encoder_tr = self.orcish_translator
        decoder_tr = self.orcish_translator

        self.assertTrue(
            decoder_tr.decode(
                encoder_tr.encode(self.message)
            ) == self.message
        )

    def test_orcish_to_common(self):
        encoder_tr = self.orcish_translator
        decoder_tr = self.common_translator

        self.assertTrue(
            decoder_tr.decode(
                encoder_tr.encode(self.message)
            ) == self.message
        )

    def test_common_to_orcish(self):
        encoder_tr = self.common_translator
        decoder_tr = self.orcish_translator

        self.assertTrue(
            decoder_tr.decode(
                encoder_tr.encode(self.message)
            ) == self.message
        )

    def test_debug_to_orcish(self):
        encoder_tr = self.debug_translator
        decoder_tr = self.orcish_translator

        self.assertTrue(
            decoder_tr.decode(
                encoder_tr.encode(self.message)
            ) == self.message
        )

    def test_orcish_to_debug(self):
        encoder_tr = self.orcish_translator
        decoder_tr = self.debug_translator

        self.assertTrue(
            decoder_tr.decode(
                encoder_tr.encode(self.message)
            ) == self.message
        )


class MessageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.translator = Translator(common)

    def test_message_without_head(self):
        msg = "1 2 3 6 0 й 6 0 6 0 6 3 й 6 0 3 й й 1"
        self.assertFalse(
            self.translator.is_encoded(msg)
        )

    def test_valid_message(self):
        msg = "й й 2 1 2 3 6 0 й 1 1 1 3 3 3 6 6 6 й й й й й 1"
        self.assertTrue(
            self.translator.is_encoded(msg)
        )

    def test_invalid_len_message(self):
        msg = "й й 2 1 2 3 6 0 й 6 0 6 0 6 3 й 6 й й 1"
        self.assertFalse(
            self.translator.is_encoded(msg)
        )

    def test_message_without_tail(self):
        msg = "й й 2 1 2 3 6 0 й 6 0 6 0 6 3 й 6 0"
        self.assertFalse(
            self.translator.is_encoded(msg)
        )
