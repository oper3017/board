from django.shortcuts import render,get_object_or_404,redirect, HttpResponse
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
from .forms import PostForm, BoardSearchForm
from .forms import BoardSearchForm
from django.views.generic.edit import FormView

def post_list(request):
    posts = Post.objects.all()
    form = BoardSearchForm()
    return render(request, 'board/post_list.html', {'posts': posts, 'form':form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'board/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
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
    post = get_object_or_404(Post, pk=pk)
    allposts = Post.objects.all()
    if post.author == request.user:
        post.delete()
        return render(request, 'board/post_list.html', {'posts': allposts})
    else:
        return render(request, 'board/error_message.html')

def search(request):
    posts = Post.objects.all()
    form = BoardSearchForm()
    fil = request.GET['search_filter']
    
    if 'search_word' in request.GET and request.GET['search_word']:
        sWord = request.GET['search_word']
        if fil == 1:
            results = posts.filter(title__icontains = sWord)
        elif fil == 2:
            me = User.objects.get(username = sWord)
            return HttpResponse(me)
            results = posts.objects.filter(author = me)
        else:
            results = posts.filter(text__icontains = sWord)
        #return render(request, 'board/post_list.html', {'posts': results, 'form':form})
    else:
        return HttpResponse('검색어를 입력 해 주세요.')

        
    

