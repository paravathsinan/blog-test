from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'startup\index.html',{'blogs':blogs})

@login_required
def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'startup/blog_details.html', {'blog':blog})
    


@login_required
def add_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            messages.success(request, 'Blog Created Successfully!')
            return redirect('index')
    form = BlogForm()
    return render(request, 'startup/add_blog.html', {'forms':form})


@login_required
def edit_post(request, id):
    blog = get_object_or_404(Blog, id=id,user=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog Updated!')
            return redirect('index')
            
        
    form = BlogForm(instance = blog)
    return render(request, 'startup/add_blog.html',{'forms':form})


@login_required
def delete(request, id):
    blog = get_object_or_404(Blog, id=id, user=request.user)
    blog.delete()
    messages.success(request, 'Deleted Successfully!')
    return redirect('index')
    
    
    
    




    