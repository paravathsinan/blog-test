from django.shortcuts import render
from .models import Blog
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'startup\index.html',{'blogs':blogs})