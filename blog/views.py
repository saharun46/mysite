from django.shortcuts import render, get_object_or_404

from mysite.blog.forms import EmailPostForm
from .models import Post 
# Create your views here.
def post_list(request):
    publish_posts = Post.published.all()
    d_posts = Post.draft.all()
    return render(request,
        'blog/post/list.html',
        {'posts':publish_posts,'d_posts':d_posts}
    )

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
        status = Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(request,'blog/post/detail.html',{'post':post})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method=='POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form':form})