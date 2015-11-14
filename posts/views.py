from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from .models import Link, Comment
from .forms import LinkForm

# Create your views here.
def links(request):
    links = Link.objects.all().order_by('-posted')
    return render(request, 'posts/links.html', {'links': links})

def comments(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    comments = Comment.objects.filter(
        object_id = link.id,
        content_type=ContentType.objects.get_for_model(link)
        ).order_by('-posted')
    return render(request, 'posts/comments.html', {'comments': comments, 'link': link})

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
