from rest_framework.serializers import ModelSerializer, ValidationError
from tweetme2.settings import MAX_TWEET_LENGTH

from .models import Tweet


class TweetSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["content"]

    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise ValidationError("This tweet is too long")

        return value
