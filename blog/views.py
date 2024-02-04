from django.shortcuts import render
from .models import Posts , Comments
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from accounts.models import Userprofile

# Create your views here.
def index (requets):

    return render(requets, 'blog/index.html', {})

def post (requets, slug):
    p = get_object_or_404(Posts, slug=slug)
    if requets.method == 'GET':
        return render(requets, 'blog/post.html', {'p': p})
    elif requets.method == 'POST':
        body = requets.POST.get('body')
        comment = Comments(
            body = body,
            author = Userprofile.objects.last(),
            post = Posts.objects.get(slug = slug)
        )

        comment.save()
        return render(requets, 'blog/post.html', {"p": p})

def posts (requets):
    blog_post = Posts.objects.all().order_by("-created_at")[:10]
    return render(requets, 'blog/posts.html', {'blog_post':blog_post})
