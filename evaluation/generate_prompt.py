from typing import List, Union


def generate_prompt(
    text: str, prompt_max_len: int, RAW_TEXT: bool = False
) -> Union[str, List[dict]]:
    """
    Generate a prompt for the user to continue the story.

    Args:
        text (str): The text to generate the prompt from.
        prompt_max_len (int): The maximum length of the prompt.
        RAW_TEXT (bool): If True, return raw text only.

    Returns:
        Union[str, List[dict]]: The generated prompt.
    """
    # truncate the text to the first "." before the prompt_max_length
    truncated_text = text[:prompt_max_len]
    # find last "." in the text
    last_dot_idx = truncated_text.rfind(".")
    # truncate the string to the last "."
    raw_text = truncated_text[: last_dot_idx + 1]

    if RAW_TEXT:
        return raw_text

    prompt = [
        {
            "role": "system",
            "content": "You are a skilled writer crafting an engaging story.",
        },
        {"role": "assistant", "content": "The story starts as follows: " + raw_text},
        {
            "role": "user",
            "content": "Continue the story from where it left off. The story should include previous characters but also introduce few new characters.",
        },
    ]

    return prompt
