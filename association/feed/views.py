from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post, Like, Comment

def feed_list(request):
    posts = Post.objects.filter(is_published=True)
    
    if not request.session.session_key:
        request.session.create()
    session_id = request.session.session_key
    
    context = {
        'posts': posts,
        'session_id': session_id,
    }
    return render(request, 'feed.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_published=True)
    
    if not request.session.session_key:
        request.session.create()
    session_id = request.session.session_key
    
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        content = request.POST.get('content')
        if author_name and content:
            Comment.objects.create(
                post=post,
                author_name=author_name,
                content=content
            )
            return redirect('post_detail', post_id=post_id)
    
    context = {
        'post': post,
        'session_id': session_id,
    }
    return render(request, 'post_detail.html', context)

def like_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        session_id = request.POST.get('session_id')
        
        if session_id:
            like, created = Like.objects.get_or_create(
                post=post,
                user_session=session_id
            )
            if not created:
                like.delete()
            
            return JsonResponse({
                'liked': created,
                'like_count': post.like_count()
            })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)