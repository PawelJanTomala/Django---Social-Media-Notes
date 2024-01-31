from django.db import models

# Create your models here.

STATUS = (
    ('pending', 'Under Consideartion'),
    ('accepted', 'Accepted'),
    ('rejected', 'Rejected'),
    ('done', 'Done'),
    ('future', 'In Future'),
)
class Content(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    # movie_url = models.URLField(null = True, blank = True)
    status = models.CharField(choices = STATUS, max_length = 30, default = 'Under Consideration')

class Voices(models.Model):
    idea = models.ForeignKey(Content, on_delete = models.CASCADE)
    reason = models.URLField()
