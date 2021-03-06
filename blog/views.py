from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.views.generic import TemplateView

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def home_page(request):
    return render(request, 'blog/home_page.html')

class HomePageView(TemplateView):
    template_name = "home_page.html"

