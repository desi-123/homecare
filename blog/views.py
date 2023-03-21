from django.shortcuts import get_object_or_404, render
from .models import Blog

def blog(request):
 blogs = Blog.objects.all()
 context = {
  'blogs': blogs,
 }
 return render(request, 'pages/blog.html', context)

def singleBlog(request, blog_id):
 blog = get_object_or_404(Blog, pk=blog_id)
 context = {
  'blog': blog
 }
 return render(request, 'pages/singleBlog.html', context)

