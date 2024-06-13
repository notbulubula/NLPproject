def generate_prompt(text, prompt_max_len, RAW_TEXT = False):
    # truncate the text to the first "." before the prompt_max_length
    truncated_text = text[:prompt_max_len]
    # find last "." in the text
    last_dot_idx = truncated_text.rfind(".")
    # truncate the string to the last "."
    raw_text = truncated_text[:last_dot_idx+1]

    if RAW_TEXT:
        return raw_text

    # prompt = [
    #     {"role": "system", "content": "Your are a wrighter of a story."},
    #     {"role": "system", "content": "Your story strats as folows: " + output},
    #     {"role": "user", "content": "Write the following part of your story and try to add new characters"}
    # ]

    prompt = [
        {"role": "system", "content": "You are a skilled writer crafting an engaging story."},
        {"role": "assistant", "content": "The story starts as follows: " + raw_text},
        {"role": "user", "content": "Continue the story from where it left off. The story should include previous characters but also introduce new characters."}
    ]

    return prompt