import re
from typing import Callable, Dict, Set, Tuple, List


def get_named_entities(
    prompt: str, response: str, pipe: Callable[[str], List[Dict[str, str]]]
) -> Tuple[Set[str], Set[str]]:
    """
    Extract named entities from the prompt and response using the pipe function.

    Args:
        prompt (str): The prompt text.
        response (str): The response text.
        pipe (Callable[[str], List[Dict[str, str]]): The pipeline function.

    Returns:
        Tuple[Set[str], Set[str]]: The set of named entities in the prompt and response.
    """
    prompt_NE = pipe(prompt)
    response_NE = pipe(response)

    # create a sets of named entities
    prompt_setNE = {x["word"] for x in prompt_NE}
    response_setNE = {x["word"] for x in response_NE}

    return prompt_setNE, response_setNE


def get_NER_score(
    prompt_setNE: Set[str], response_setNE: Set[str], creativeness: float = 0.3
) -> float:
    """
    Calculate the Named Entity Recognition (NER) score between the prompt and response.

    Args:
        prompt_setNE (Set[str]): The set of named entities in the prompt.
        response_setNE (Set[str]): The set of named entities in the response.
        creativeness (float): The weight of the importance of new named entities.

    Returns:
        float: The NER score.
    """
    # calculate how many named entities are repeated in the continuation
    repeated_NE = len(prompt_setNE & response_setNE)
    new_NE = len(response_setNE - prompt_setNE)

    if len(prompt_setNE) == 0:
        # TODO: improve this
        score = min(1, new_NE * creativeness)

    else:
        repeated = repeated_NE / len(prompt_setNE)
        new = max(0, 1 - abs(creativeness - new_NE / len(prompt_setNE)))

        score = (1 - creativeness) * repeated + creativeness * new

    return score


def get_avg_std(text: str) -> Tuple[float, float]:
    """
    Calculate the average and standard deviation of the sentence lengths in the text.

    Args:
        text (str): The text to evaluate.

    Returns:
        Tuple[float, float]: The mean and standard deviation of the sentence lengths.
    """
    # split the text into sentences
    sentences = re.split(r"\. |\! |\? ", text)
    # calculate the mean and std of the sentence lengths
    mean = sum([len(x) for x in sentences]) / len(sentences)
    std = sum([(len(x) - mean) ** 2 for x in sentences]) / len(sentences)
    std = std**0.5
    return mean, std


def evaluate_text(
    prompt: str,
    response: str,
    pipe: Callable[[str], List[Dict[str, str]]],
    creativeness: float = 0.3,
) -> Tuple[Dict[str, float], Set[str], Set[str]]:
    """
    Evaluate the prompt and response text using Named Entity Recognition (NER) and sentence length.

    Args:
        prompt (str): The prompt text.
        response (str): The response text.
        pipe (Callable[[str], List[Dict[str, str]]): The pipeline function.
        creativeness (float): The weight of the importance of new named entities.

    Returns:
        Tuple[Dict[str, float], Set[str], Set[str]]: The evaluation results, the set of named entities in the prompt and response.
    """
    prompt_setNE, response_setNE = get_named_entities(prompt, response, pipe)
    NERscore = get_NER_score(prompt_setNE, response_setNE, creativeness=creativeness)

    prompt_mean, prompt_std = get_avg_std(prompt)
    response_mean, response_std = get_avg_std(response)

    prompt_num_dialogues = prompt.count('"') / 2
    response_num_dialogues = response.count('"') / 2

    output_dict = {
        "NER_score": NERscore,
        "prompt_mean": prompt_mean,
        "prompt_std": prompt_std,
        "response_mean": response_mean,
        "response_std": response_std,
        "prompt_num_dialogues": prompt_num_dialogues,
        "response_num_dialogues": response_num_dialogues,
    }

    return output_dict, prompt_setNE, response_setNE
