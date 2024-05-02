from django.shortcuts import render 
from django.conf import settings

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, "pages/feed.html")

def tweets_list_view(request, *args, **kwargs):
    return render(request, "tweets/list.html", context={}, status=200)

def tweets_detail_view(request, tweet_id, *args, **kwargs):
    return render(request, "tweets/detail.html", context={"tweet_id": tweet_id}, status=200)


