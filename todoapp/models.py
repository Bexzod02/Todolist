from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
User = get_user_model()


STATUS = (
    (0, _('New')),
    (1, _('Process')),
    (2, _('Complated')),
    (3, _('Cancelled')),
)

class ArticleMenager(models.Manager):
    def search(self, query):
        lookups = Q(title__icontains = query)
        obj = Todo.objects.filter(lookups)
        return obj

class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = ArticleMenager()

    def __str__(self):
        return self.title
        
class Logo(models.Model):
    logo = models.ImageField()