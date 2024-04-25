from django.shortcuts import render, redirect
from django.http import Http404, JsonResponse
from .models import Tweet
from .serializers import TweetSerializer
from .forms import TweetForm
from django.utils.http import is_safe_url
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "pages/home.html", context={}, status=200)

@api_view(['POST']) 
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data , status=201)
    return Response({}, status=400)
    
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

@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data, status=200)
    
    
def tweet_list_view_pure_django(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status=200)

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