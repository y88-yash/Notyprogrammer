from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComment
from django.contrib import messages
import datetime
from .forms import *

# Create your views here.

def bloghome(request):
    allpost = Post.objects.all()
  #  allpost = Post.objects.filter(testfield=12).order_by('-id')[0]
    context = {'allpost':allpost}
    #obj= Model.objects.filter(testfield=12).order_by('-id')[0]
    return render(request,"home/home.html",context)

def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context={'post':post,'comments':comments}

    return render(request,"blogtemp/blogpost.html",context)

def createposts(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid(): 

            post=form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request,"Post Created")
            return redirect('createposts') 
    else: 
        form = PostForm() 
    return render(request,"blogtemp/createpost.html",{'form' : form})


def postComment(request):
    if request.method=='POST':
         
        comment = request.POST.get("comment")
        user = request.user
        postSno =  request.POST.get("postSno")
        post = Post.objects.get(Sno=postSno)
        comment = BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,"Your comment has been posted successfully!")



    

    return redirect(f"/blog/{post.slug}")
