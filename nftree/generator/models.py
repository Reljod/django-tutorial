import uuid
from email.policy import default
from django.db import models

class NFT(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)
    is_frozen = models.BooleanField('is_frozen', default=False)
    image_url = models.URLField('image_url', null=True)