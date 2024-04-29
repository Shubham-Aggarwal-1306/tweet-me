from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from tweets.models import Tweet
from tweets.serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer
from tweets.forms import TweetForm
from django.utils.http import is_safe_url
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


@api_view(['POST']) 
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetCreateSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data , status=201)
    return Response({}, status=400)



@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    username = request.GET.get("username") # ?username=Justin
    if username != None:
        qs = qs.filter(user__username__iexact=username)
    
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data, status=200)
    
    


@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status=200)

@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({"message": "Tweet not found"}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({"message": "You cannot delete this tweet"}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Tweet removed"}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action_view(request, *args, **kwargs):
    '''
    id is required.
    Action options are: like, unlike, retweet
    '''
    serializer = TweetActionSerializer(data=request.data)
    data = {}
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
    tweet_id = data.get("id")
    action = data.get("action")
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({"message": "Tweet not found"}, status=404)
    obj = qs.first()
    if action == "like":
        obj.likes.add(request.user)
        serializer = TweetSerializer(obj)
        return Response(serializer.data, status=200)
    elif action == "unlike":
        obj.likes.remove(request.user)
        serializer = TweetSerializer(obj)
        return Response(serializer.data, status=200)
    elif action == "retweet":
        parent_obj = obj
        new_tweet = Tweet.objects.create(
            user=request.user,
            parent=parent_obj,
            content=serializer.data.get("content")
        )
        return Response(TweetSerializer(new_tweet).data, status=201)
        
    obj.delete()
    return Response({"message": "Tweet removed"}, status=200)


def tweet_create_view_pure_django(request, *args, **kwargs):
    '''
    REST API CRUD VIEW
    '''
    if not request.user.is_authenticated:
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None  
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user or None # Anonymous user handling
        obj.save()
        form = TweetForm()
        
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/forms.html', context={"form": form})

def tweet_list_view_pure_django(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view_pure_Django(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
    }
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        raise Http404

    return JsonResponse(data) # json.dumps content type = 'application/json'