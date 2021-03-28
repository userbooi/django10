from django.shortcuts import render
from .models import Topic

# Create your views here.
def blog(request):
    info = Topic.objects.all
    return render(request, 'blogs/blog.html', {'infos':info})
