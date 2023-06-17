from random import randint

from django.contrib.auth import get_user_model
from django.db.models import (
    CASCADE,
    AutoField,
    FileField,
    ForeignKey,
    ManyToManyField,
    Model,
    TextField,
    DateTimeField,
    SET_NULL,
)

User = get_user_model()


class TweetLike(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    tweet = ForeignKey("Tweet", on_delete=CASCADE)
    timestamp = DateTimeField(auto_now_add=True)


class Tweet(Model):
    parent = ForeignKey("self", null=True, on_delete=SET_NULL)
    id = AutoField(primary_key=True)
    user = ForeignKey(User, on_delete=CASCADE)
    likes = ManyToManyField(
        User, related_name="tweet_user", blank=True, through=TweetLike
    )
    content = TextField(blank=True, null=True)
    image = FileField(upload_to="images/", blank=True, null=True)
    timestamp = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-id"]

    @property
    def is_retweet(self):
        return self.parent != None

    def serialize(self):
        return {"id": self.id, "content": self.content, "likes": randint(0, 999)}
