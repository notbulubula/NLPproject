<div style="text-align: justify">

# NLP project - Storyteller

## Description

The project is a simple NLP project that uses the Hugging Face library to generate stories and evaluate them. <br>
The project uses Phi-3 model from Microsoft to generate stories. The decision to use this model was made because it is a model which is relatively small but what is more important it has a large context window (128K tokens), which in case of providing large text input such as chapters, can be useful. <br>

The project consists of the following modules:
- `generate_chapter.py` - module that generates stories using the Phi-3 model.
- `generate_prompt.py` - module that generates prompts for the Phi-3 model.
- `evaluate.py` - module that evaluates the generated stories.
- `tests` - directory that contains unit tests for the project.
- `data_fetch.py` - module that fetches the dataset from the Hugging Face library.
- `project.ipynb` - Jupyter notebook where You can try to generate stories Yourself.

For the generational part of the project the Phi-3 model was used after prepering prompts and generation arguments which yeladed the best results. <br>
Main focus of the project was am evaluation of the generated stories. The evaluation is based on the following metrics and heuristics:
- Named Entity Recognition
- heuristics based NER score (incentivizing the model to generate new named entities)
- avreage sentence length and standard deviation
- number of dialogues

## Used dataset

The dataset used in the project is the STORIES dataset from the Hugging Face library. The dataset consists of almost 1M chapter-long stories presented in simple text format. Additionaly due to the large number of them the dataset is very versatile and we can observe if the modle can generate stories in different writing styles. <br>

https://huggingface.co/datasets/lucadiliello/STORIES


## Testing

Check the project with flake8:
```bash
flake8 NLPproject
```

Check the project with mypy:
```bash
mypy NLPproject
```

Run the unit tests (inside the project directory):
```bash
python -m unittest discover tests
```
</div>