from random import randint

from django.contrib.auth import get_user_model
from django.db.models import CASCADE, AutoField, FileField, ForeignKey, Model, TextField

User = get_user_model()


class Tweet(Model):
    id = AutoField(primary_key=True)
    user = ForeignKey(User, on_delete=CASCADE)
    content = TextField(blank=True, null=True)
    image = FileField(upload_to="images/", blank=True, null=True)

    class Meta:
        ordering = ["-id"]

    def serialize(self):
        return {"id": self.id, "content": self.content, "likes": randint(0, 999)}
