from random import randint

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from tweetme2.settings import ALLOWED_HOSTS, LOGIN_URL

from .forms import TweetForm
from .models import Tweet


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    is_ajax = request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"
    user = request.user
    if not request.user.is_authenticated:
        user = None

    if not request.user.is_authenticated:
        if is_ajax:
            return JsonResponse({}, status=401)
        return redirect(LOGIN_URL)

    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None

    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user or None
        obj.save()

        if is_ajax:
            return JsonResponse(obj.serialize(), status=201)
        if next_url and url_has_allowed_host_and_scheme(next_url, ALLOWED_HOSTS):
            return redirect(next_url)

        form = TweetForm()

    if form.errors and is_ajax:
        return JsonResponse(form.errors, status=400)

    return render(request, "components/form.html", context={"form": form})


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    data = {"response": tweets_list}
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by js
    return json data
    """
    data = {"isUser": False, "id": tweet_id}
    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not found"
        status = 404

    return JsonResponse(
        data, status=status
    )  # json.dumps content_type="application/json"
