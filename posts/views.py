from django.shortcuts import render
from .models import Link

# Create your views here.
def all_links(request):
    links = Link.objects.all()
    return render(request, 'posts/all_links.html', {'links': links})
