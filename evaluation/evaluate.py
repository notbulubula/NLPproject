import re


def get_named_entities(prompt, response, pipe):
    prompt_NE = pipe(prompt)
    response_NE = pipe(response)

    # create a sets of named entities
    prompt_setNE = {x["word"] for x in prompt_NE}
    response_setNE = {x["word"] for x in response_NE}

    return prompt_setNE, response_setNE


def get_NER_score(prompt_setNE, response_setNE, creativeness=0.3):
    # (1 - creativeness) is the weight of the importance of repeated named entities
    # creativeness is the weight of the importance of new named entities

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


def get_avg_std(text):
    # split the text into sentences
    sentences = re.split(r"\. |\! |\? ", text)
    # calculate the mean and std of the sentence lengths
    mean = sum([len(x) for x in sentences]) / len(sentences)
    std = sum([(len(x) - mean) ** 2 for x in sentences]) / len(sentences)
    return mean, std


def evaluate_text(prompt, response, pipe, creativeness=0.3):
    prompt_setNE, response_setNE = get_named_entities(prompt, response, pipe)
    NERscore = get_NER_score(prompt_setNE, response_setNE, creativeness=creativeness)

    prompt_mean, prompt_std = get_avg_std(prompt)
    response_mean, response_std = get_avg_std(response)

    prompt_num_dialogues = prompt.count('"') / 2
    response_num_dialogues = response.count('"') / 2

    return {
        "prompt_NE": prompt_setNE,
        "response_NE": response_setNE,
        "NER_score": NERscore,
        "prompt_mean": prompt_mean,
        "prompt_std": prompt_std,
        "response_mean": response_mean,
        "response_std": response_std,
        "prompt_num_dialogues": prompt_num_dialogues,
        "response_num_dialogues": response_num_dialogues,
    }
