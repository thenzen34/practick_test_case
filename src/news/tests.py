from builtins import super
from datetime import datetime, timedelta

from django.test import TestCase
from rest_framework.utils.serializer_helpers import ReturnList

from news.models import News


class EndpointTests(TestCase):
    def setUp(self):
        super(EndpointTests, self).setUp()

        today = datetime.now()

        News.objects.create(date=today + timedelta(days=1), content="future test", subject="future test")
        News.objects.create(date=today + timedelta(days=-1), content="past test", subject="past test")
        News.objects.create(date=today + timedelta(days=-7), content="past test", subject="past test")
        News.objects.create(date=None, content="None test", subject="None test")

    def test_news_add(self):
        today = datetime.now()

        client = self.client
        input_data = {
            "date": today.date(),
            "content": "post test",
            "subject": "post test",
        }
        classifier_url = "/news"
        response = client.post(classifier_url, input_data, format='json')
        self.assertTrue(response.status_code in [200, 201])
        self.assertTrue("date" in response.data)
        self.assertTrue("content" in response.data)
        self.assertTrue("subject" in response.data)

    def test_news_list(self):
        client = self.client
        input_data = {
        }
        classifier_url = "/news"
        response = client.get(classifier_url, input_data, format='json')
        self.assertTrue(response.status_code in [200, 201])
        self.assertTrue(type(response.data) is ReturnList)
        t: ReturnList = response.data
        self.assertTrue(len(t) == 2)
