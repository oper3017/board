from django.shortcuts import render,get_object_or_404,redirect, HttpResponse
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm, BoardSearchForm
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import UploadForm,Upload

def post_list(request):
    posts = Post.objects.all()
    form = BoardSearchForm()
    return render(request, 'board/post_list.html', {'posts': posts, 'form':form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'board/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            upload = Upload()
            upload.pic = form.cleaned_data['docfile']
            upload.save()
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'board/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('board:post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'board/post_edit.html', {'form': form})
    else:
        return render(request, 'board/error_message.html')

def post_remove(request, pk):
    form = BoardSearchForm()
    post = get_object_or_404(Post, pk=pk)
    allposts = Post.objects.all()
    if post.author == request.user:
        post.delete()
        return render(request, 'board/post_list.html', {'posts': allposts, 'form':form})
    else:
        return render(request, 'board/error_message.html')

def search(request):
    posts = Post.objects.all()
    form = BoardSearchForm()
    fil = int(request.GET['search_filter'])
    
    if 'search_word' in request.GET and request.GET['search_word']:
        sWord = request.GET['search_word']
        if fil == 1:
            results = posts.filter(title__icontains = sWord)
        elif fil == 2:
            me = User.objects.get(username = sWord)
            results = posts.filter(author = me)
        elif fil == 3:
            results = posts.filter(text__icontains = sWord)
        else:
            return HttpResponse('검색이 잘못되었습니다.')
        return render(request, 'board/post_list.html', {'posts': results, 'form':form})
    else:
        return HttpResponse('검색어를 입력 해 주세요.')

def image(request):
    if request.method=="POST":
        img = UploadForm(request.POST, request.FILES)       
        if img.is_valid():
            img.save()
            images=Upload.objects.all()
            return render(request,'board/image.html',{'form':img,'images':images})
    else:
        img=UploadForm()
        images=Upload.objects.all()
    return render(request,'board/image.html',{'form':img,'images':images})