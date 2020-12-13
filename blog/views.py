from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import PostForm
from .models import Post


# Create your views here.
def home(request):
    data = dict(posts=Post.objects.all())
    return render(request, template_name='blog/home.html', context=data)


def index(request):
    return render(request, template_name='blog/index.html')


def create_post(request):
    form = PostForm()
    data = {
        'form': form,
    }
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-url')
    return render(request, template_name='blog/create_post.html', context=data)
