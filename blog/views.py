from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
# takes request object as the only parameter

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

#To display a single post
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='Published',
    	publish_year=year, publish_month=month,
    	publish_day=day)
    return render(request, 'blog/post/detail.html',
                  {'post':post})