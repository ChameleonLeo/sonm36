from django.db import models


class Artist(models.Model):
    info = models.JSONField()
