import sys
from eval import Evaluator

words1 = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs1 = [1.0, 2.0, 1.0, 4.0, 0.5]

words2 = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
coefs2 = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]


print(Evaluator.zip_evaluate(coefs1, words1))
print(Evaluator.zip_evaluate(coefs2, words2))
print(Evaluator.enumerate_evaluate(coefs1, words1))
print(Evaluator.enumerate_evaluate(coefs2, words2))
