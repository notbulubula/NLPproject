import unittest

from evaluate.generate_prompt import generate_prompt

class TestGeneratePrompt(unittest.TestCase):
    """
    Unit tests for the generate_prompt function.
    """
    text = "Hye was waiting for her usual bus at the usual bus stop near her work place . It was late at night , almost 10pm . She was all alone . But , what she didn 't realize was that she wasn 't exactly all alone ."
    prompt_max_len = 200

    def test_generate_prompt(self) -> None:
        raw_text = generate_prompt(self.text, self.prompt_max_len, RAW_TEXT = True)
        self.assertEqual(raw_text, "Hye was waiting for her usual bus at the usual bus stop near her work place . It was late at night , almost 10pm . She was all alone .")

if __name__ == '__main__':
    unittest.main()