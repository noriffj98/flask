import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        test_1 = sentiment_analyzer("I love working with Python")
        self.assertEqual(test_1['label'], "SENT_POSITIVE")

        test_2 = sentiment_analyzer("I hate working with Python")
        self.assertEqual(test_2['label'], "SENT_NEGATIVE")

        test_3 = sentiment_analyzer("I am neutral on Python")
        self.assertEqual(test_3['label'], "SENT_NEUTRAL")

unittest.main()