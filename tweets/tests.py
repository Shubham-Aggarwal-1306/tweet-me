from django.test import TestCase
from .models import Tweet
# Create your tests here.
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()

class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cfe', password='somepassword')
        self.user2 = User.objects.create_user(username='cfe-2', password='somepassword2')
        Tweet.objects.create(content="my first tweet", user=self.user)
        Tweet.objects.create(content="my second tweet", user=self.user)
        Tweet.objects.create(content="my third tweet", user=self.user2)
        
    def test_user_created(self):
        self.assertEqual(self.user.username, "cfe")
        
    def test_tweet_created(self):
        tweet = Tweet.objects.create(content="my fourth tweet", user=self.user)
        self.assertEqual(tweet.id, 4)
        self.assertEqual(tweet.user, self.user)
        self.assertEqual(tweet.content, "my fourth tweet")
        self.assertEqual(tweet.is_retweet, False)
        
    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client
        
    def test_tweet_list(self):
        client = self.get_client()
        response = client.get("/api/tweets/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)
        self.assertEqual(response.json()[0]['content'], "my first tweet")
    
    def test_tweet_action_like(self):
        client = self.get_client()
        response = client.post("/api/tweets/action/", {"id": 1, "action": "like"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get('likes')
        self.assertEqual(like_count, 1)
        user = self.user
        my_like_instances_count = user.tweet_user.count()
        self.assertEqual(my_like_instances_count, 1)
    
    def test_tweet_action_unlike(self):
        client = self.get_client()
        response = client.post("/api/tweets/action/", {"id": 1, "action": "like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/tweets/action/", {"id": 1, "action": "unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get('likes')
        self.assertEqual(like_count, 0)
        user = self.user
        my_like_instances_count = user.tweet_user.count()
        self.assertEqual(my_like_instances_count, 0)
    
    def test_tweet_action_retweet(self):
        client = self.get_client()
        response = client.post("/api/tweets/action/", {"id": 2, "action": "retweet"})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_tweet_id = data.get("id")
        self.assertNotEqual(2, new_tweet_id)
        
    def test_tweet_create_view(self):
        client = self.get_client()
        response = client.post("/api/tweets/create/", {"content": "This is my tweet"})
        self.assertEqual(response.status_code, 201)
        response_data = response.json()
        new_tweet_id = response_data.get("id")
        self.assertEqual(new_tweet_id, 4)
        self.assertEqual(Tweet.objects.all().count(), 4)
    
    def test_tweet_detail_view(self):
        client = self.get_client()
        response = client.get("/api/tweets/1/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        _id = data.get("id")
        self.assertEqual(_id, 1)
    
    def test_tweet_delete_view(self):
        client = self.get_client()
        response = client.delete("/api/tweets/1/delete/")
        self.assertEqual(response.status_code, 200)
        response = client.delete("/api/tweets/1/delete/")
        self.assertEqual(response.status_code, 404)
        response_incorrect_owner = client.delete("/api/tweets/3/delete/")
        self.assertEqual(response_incorrect_owner.status_code, 401)
    
        
    
        
        