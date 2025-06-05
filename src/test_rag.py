import unittest
import chromadb
from rag import main
from deepeval import assert_test
from deepeval import evaluate
from deepeval import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import AnswerRelevancyMetric





class TestRag(unittest.TestCase):
	def test_main(self):
		query = "stick figure"
		query_results_text = main(query)
		key = os.getenv('OPENAI_KEY')
		answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.7, model="gpt-4o")
		test_case = LLMTestCase(
			input=query,
			actual_output=query_results_text
		)
		print(f"\n--- Running Answer Relevancy Test for: '{query}' ---")
		assert_test(test_case, [answer_relevancy_metric])
		print(f"Test Passed: {answer_relevancy_metric.is_successful}")
		print(f"Score: {answer_relevancy_metric.score}")
		print(f"Reason: {answer_relevancy_metric.reason}")



if __name__ == '__main__':
	unittest.main()
