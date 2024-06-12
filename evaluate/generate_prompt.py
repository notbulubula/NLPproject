# prepering the prompts for the model
def generate_prompt(text, prompt_max_len):
    # truncate the text to the first "." before the prompt_max_length
    truncated_text = text[:prompt_max_len]
    # find last "." in the text
    last_dot_idx = truncated_text.rfind(".")
    # truncate the string to the last "."
    output = truncated_text[:last_dot_idx+1]

    return output