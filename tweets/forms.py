from django.forms import ModelForm, ValidationError

from tweetme2.settings import MAX_TWEET_LENGTH

from .models import Tweet


class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ["content"]

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise ValidationError("This tweet is too long")

        return content
