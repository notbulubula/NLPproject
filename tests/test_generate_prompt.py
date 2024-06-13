import unittest

from evaluation.generate_prompt import generate_prompt


class TestGeneratePrompt(unittest.TestCase):
    """
    Unit tests for the generate_prompt function.
    """

    text = "Hye was waiting for her usual bus at the usual bus stop near her work place . It was late at night , almost 10pm . She was all alone . But , what she didn 't realize was that she wasn 't exactly all alone ."
    prompt_max_len = 200

    def test_generate_prompt_raw(self) -> None:
        raw_text = generate_prompt(self.text, self.prompt_max_len, RAW_TEXT=True)
        self.assertEqual(
            raw_text,
            "Hye was waiting for her usual bus at the usual bus stop near her work place . It was late at night , almost 10pm . She was all alone .",
        )

    def test_generate_prompt(self) -> None:
        prompt = generate_prompt(self.text, self.prompt_max_len)
        self.assertEqual(
            prompt,
            [
                {
                    "role": "system",
                    "content": "You are a skilled writer crafting an engaging story.",
                },
                {
                    "role": "assistant",
                    "content": "The story starts as follows: Hye was waiting for her usual bus at the usual bus stop near her work place . It was late at night , almost 10pm . She was all alone .",
                },
                {
                    "role": "user",
                    "content": "Continue the story from where it left off. The story should include previous characters but also introduce few new characters.",
                },
            ],
        )


if __name__ == "__main__":
    unittest.main()
