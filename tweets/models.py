from random import randint
from django.db.models import Model, AutoField, TextField, FileField, ForeignKey
from django.contrib.auth import get_user_model

User = get_user_model()


class Tweet(Model):
    id = AutoField(primary_key=True)
    user = ForeignKey(User)
    content = TextField(blank=True, null=True)
    image = FileField(upload_to="images/", blank=True, null=True)

    class Meta:
        ordering = ["-id"]

    def serialize(self):
        return {"id": self.id, "content": self.content, "likes": randint(0, 999)}
