def generate_chapter(prompt, pipe):
    generation_args = {
        "max_new_tokens": 500,
        "temperature": 0.9,
        "do_sample": True
    }

    generated_chapter = pipe(prompt, **generation_args)[0]["generated_text"]

    return generated_chapter
