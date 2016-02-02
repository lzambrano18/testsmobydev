from django.db import models


class Cause(models.Model):
    year = models.CharField(max_length=4,)

    ethnicity = models.CharField(max_length=200,)

    sex = models.CharField(max_length=6,)

    cause_of_death = models.CharField(max_length=200,)

    count = models.IntegerField()

    percent = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('detail', (), {'pk': self.pk})
