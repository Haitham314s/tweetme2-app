from django.contrib.admin import ModelAdmin, site, TabularInline

# Register your models here.
from .models import Tweet, TweetLike


class TweetLikeAdmin(TabularInline):
    model = TweetLike


class TweetAdmin(ModelAdmin):
    list_display = ["__str__", "user"]
    search_fields = ["content", "user__username", "user__email"]

    class Meta:
        model = Tweet


site.register(Tweet)
