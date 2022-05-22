from src.podcast_recommendation.algorithm import PodcastRecommendation
import unittest

class TestAlg(unittest.TestCase):
    def testBuild(self):
        uri = 'bolt://localhost:7687'
        user = 'neo4j'
        psw = 'password'
        pr = PodcastRecommendation(uri, (user, psw), verbose=True)
        pr.build_graph(verbose=True)
        print(pr.recommend('6C561484AED5C02'))
        pr.delete_user('6C561484AED5C02')
        pr.delete_all()
        pr.close()
        