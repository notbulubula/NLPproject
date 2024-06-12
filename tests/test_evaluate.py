# import unittest

# from evaluate.evaluate import get_named_entities, get_NER_score, get_avg_std, evaluate_text



# # TODO:  add pipe somehow
# pipe = None

# def test_get_named_entities():
#     prompt = "The Tom visited the Manhattan. The Jerry visited the Brooklyn."
#     response = "The Tom visited the Manhattan. The Jerry visited the Brooklyn."
#     prompt_NE, response_NE = get_named_entities(prompt, response, pipe)
#     assert prompt_NE == {"Tom", "Manhattan", "Jerry", "Brooklyn"}
#     assert response_NE == {"Tom", "Manhattan", "Jerry", "Brooklyn"}

# # def test_get_NER_score():
# #     prompt_setNE = {"Tom", "Manhattan", "Jerry", "Brooklyn"}
# #     response_setNE = {"Tom", "Manhattan", "Jerry", "Brooklyn"}
# #     score = get_NER_score(prompt_setNE, response_setNE)
# #     assert score == 1.0

# def test_get_avg_std():
#     text = "The Tom visited the Manhattan. The Jerry visited the Brooklyn."
#     mean, std = get_avg_std(text)
#     assert mean == 30.0
#     assert std == 1.0 

# def test_evaluate_text():
#     prompt = "The Tom visited the Manhattan. The Jerry visited the Brooklyn."
#     response = "The Tom visited the Manhattan. The Jerry visited the Brooklyn."
#     results = evaluate_text(prompt, response, pipe)
#     # assert results[0]["NER_score"] == 1.0
#     assert results[0]["prompt_mean"] == 30.0
#     assert results[0]["prompt_std"] == 1.0
#     assert results[0]["response_mean"] == 30.0
#     assert results[0]["response_std"] == 1.0
#     assert results[0]["prompt_num_dialogues"] == 0
#     assert results[0]["response_num_dialogues"] == 0

# if __name__ == '__main__':
#     unittest.main()