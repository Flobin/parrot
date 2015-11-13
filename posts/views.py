from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Link, Comment
from .forms import LinkForm

# Create your views here.
def all_links(request):
    links = Link.objects.all().order_by('-posted')
    return render(request, 'posts/all_links.html', {'links': links})

def all_comments(request, link_id):
    link = Link.objects.get(id=link_id)
    comments = Comment.objects.get(id=link_id)
    return render(request, 'posts/all_comments.html', {'comments': comments, 'link': link})

@login_required(login_url='/accounts/login/')
def submit(request):
    if request.method == 'POST':
        form = LinkForm(data=request.POST,auto_id=True)
        if form.is_valid():
            form.full_clean()
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = LinkForm(auto_id=True)
    return render(request, 'posts/submit.html', {'form': form})
