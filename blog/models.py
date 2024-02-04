from django.urls import reverse , reverse_lazy
from django.db import models
from accounts.models import Userprofile 
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length = 300 , blank = True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(Userprofile, related_name= 'post_like' , null= True, blank = True)
    dislike = models.ManyToManyField(Userprofile, related_name= 'post_dislike', null = True, blank = True)

    def save(self):
        super().save()
        if not self.slug:
            self.slug = slugify(self.title)
            self.save()

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
    



    def __str__(self) -> str:
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now = True)
    is_validate = models.BooleanField(default = False)
    
    def __str__(self) -> str:
        return self.body
    
