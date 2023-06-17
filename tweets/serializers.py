from rest_framework.serializers import (
    CharField,
    IntegerField,
    ModelSerializer,
    Serializer,
    SerializerMethodField,
    ValidationError,
)

from tweetme2.settings import MAX_TWEET_LENGTH, TWEET_ACTION_OPTIONS

from .models import Tweet


class TweetActionSerializer(Serializer):
    id = IntegerField()
    action = CharField()
    content = CharField(allow_blank=True, required=False)

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in TWEET_ACTION_OPTIONS:
            raise ValidationError("This is not a valid action for tweets")

        return value


class TweetCreateSerializer(ModelSerializer):
    likes = SerializerMethodField(read_only=True)
    content = SerializerMethodField(read_only=True)

    class Meta:
        model = Tweet
        fields = ["id", "content", "likes"]

    def get_likes(self, obj):
        return obj.likes.count()

    def get_content(self, obj):
        content = obj.content
        if obj.is_retweet:
            content = obj.parent.content

        return content


class TweetSerializer(ModelSerializer):
    likes = SerializerMethodField(read_only=True)
    parent = TweetCreateSerializer(source="parent", read_only=True)

    class Meta:
        model = Tweet
        fields = ["id", "content", "likes"]

    def get_likes(self, obj):
        return obj.likes.count()

    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise ValidationError("This tweet is too long")

        return value
