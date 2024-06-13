from typing import Callable


def generate_chapter(prompt: str, max_new_tokens: int, pipe: Callable[..., list]) -> str:
    """
    Generate a new chapter based on the prompt.

    Args:
        prompt (str): The prompt text.
        max_new_tokens (int): The maximum number of tokens to generate.
        pipe (Callable[..., list]): The pipeline function.

    Returns:
        str: The generated chapter.
    """
    generation_args = {
        "max_new_tokens": max_new_tokens,
        "return_full_text": False,
        "temperature": 0.3,
        "do_sample": True,
    }

    generated_chapter = pipe(prompt, **generation_args)[0]["generated_text"]

    return generated_chapter
