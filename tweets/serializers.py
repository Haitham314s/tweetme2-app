from rest_framework.serializers import (
    CharField,
    IntegerField,
    ModelSerializer,
    Serializer,
    ValidationError,
)

from tweetme2.settings import MAX_TWEET_LENGTH, TWEET_ACTION_OPTIONS

from .models import Tweet


class TweetActionSerializer(Serializer):
    id = IntegerField()
    action = CharField()

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in TWEET_ACTION_OPTIONS:
            raise ValidationError("This is not a valid action for tweets")

        return value


class TweetSerializer(ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["content"]

    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise ValidationError("This tweet is too long")

        return value
