from django.shortcuts import render, redirect
from .models import Post
from django .contrib. auth import (authenticate, login, logout)
from django .contrib. auth import (authenticate, login, logout)


# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request,'home.html', context)

def move(request):
    return render(request, "move.html")

def add(request):
    title = request.POST["title"]
    writer = request.POST["writer"]
    content = request.POST["content"]
    Post.objects.create(title=title, writer=writer, content=content)
    return redirect("home")

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect("home")

def edit(request, pk):
    post = Post.objects.get(pk=pk)
    post.title = request.POST["title"]
    post.writer = request.POST["writer"]
    post.content = request.POST["content"]
    post.save()
    return redirect("home")


def sign_up(request):
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        cpassword=request.POST["cpassword"]
        if password == cpassword:
            user = User.objects.create_user(
                username=username, password=password
            )
            login(request, user)
            return render(request, "home.html")
        else:
            error = "비밀번호가 다릅니다,"
            context = {'error': error}


        user = User.object.create_user(
            username=request.POST["username"], password=request.POST["password"]
        )
        login(request, user)
        return render(request ,'home.html')
    else:
        return render(request, 'signup.html')    