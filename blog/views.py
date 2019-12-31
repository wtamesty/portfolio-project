from django.shortcuts import render, get_object_or_404


from .models import Blog

# Create your views here.
def all_blogs(request):
    blogs = Blog.objects
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail_blog.html', {'blog':detail_blog})
