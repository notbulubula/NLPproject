import unittest
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline


from evaluation.evaluate import (
    get_named_entities,
    get_NER_score,
    get_avg_std,
    evaluate_text,
)


class TestCalculateScores(unittest.TestCase):
    """
    Unit tests for the calculate_scores_df
    and calculate_scores_df_tuned functions.
    """

    tokenizer: AutoTokenizer
    model: AutoModelForTokenClassification
    pipe: pipeline
    prompt = "The Tom visited the Manhattan. The Jerry visited the Brooklyn."
    response = "The Tom visited the Manhattan. The Jerry visited the Brooklyn."

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up the tokenizer and model before any tests are run.
        """
        cls.tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
        cls.model = AutoModelForTokenClassification.from_pretrained(
            "dbmdz/bert-large-cased-finetuned-conll03-english"
        )
        cls.pipe = pipeline("ner", model=cls.model, tokenizer=cls.tokenizer)

    def test_get_named_entities(self) -> None:
        """
        Test the get_named_entities function.
        """
        prompt_NE, response_NE = get_named_entities(
            self.prompt, self.response, self.pipe
        )

        self.assertIn("Tom", prompt_NE)
        self.assertIn("Manhattan", prompt_NE)
        self.assertIn("Jerry", prompt_NE)
        self.assertIn("Brooklyn", prompt_NE)
        self.assertIn("Tom", response_NE)
        self.assertIn("Manhattan", response_NE)
        self.assertIn("Jerry", response_NE)
        self.assertIn("Brooklyn", response_NE)

    def test_get_NER_score(self) -> None:
        """
        Test the get_NER_score function.
        """
        prompt_setNE = {
            "Tom",
            "Manhattan",
            "Jerry",
            "Brooklyn",
            "New York",
            "California",
            "Florida",
            "Texas",
            "Washington",
            "Oregon",
        }
        response_setNE = {
            "Tom",
            "Manhattan",
            "Jerry",
            "Brooklyn",
            "New York",
            "California",
            "Florida",
            "Texas",
            "Washington",
            "Oregon",
            "Nevada",
            "Arizona",
            "Utah",
        }

        score = get_NER_score(prompt_setNE, response_setNE)

        self.assertEqual(score, 1.0)

    def test_get_avg_std(self) -> None:
        """
        Test the get_avg_std function.
        """
        mean, std = get_avg_std(self.prompt)

        self.assertEqual(mean, 30.0)
        self.assertEqual(std, 1.0)

    def test_evaluate_text(self) -> None:
        """
        Test the evaluate_text function.
        """
        results_dict, prompt_NE, response_NE = evaluate_text(
            self.prompt, self.response, self.pipe
        )

        self.assertEqual(prompt_NE, {"Tom", "Manhattan", "Jerry", "Brooklyn"})
        self.assertEqual(response_NE, {"Tom", "Manhattan", "Jerry", "Brooklyn"})
        self.assertEqual(round(results_dict["NER_score"], 2), 0.91)
        self.assertEqual(results_dict["prompt_mean"], 30.0)
        self.assertEqual(results_dict["prompt_std"], 1.0)
        self.assertEqual(results_dict["response_mean"], 30.0)
        self.assertEqual(results_dict["response_std"], 1.0)
        self.assertEqual(results_dict["prompt_num_dialogues"], 0)
        self.assertEqual(results_dict["response_num_dialogues"], 0)


if __name__ == "__main__":
    unittest.main()
