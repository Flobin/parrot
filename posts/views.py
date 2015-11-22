from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType

from .models import Link, Comment
from .forms import LinkForm, CommentForm

# Create your views here.
def links(request):
    links = Link.objects.all().order_by('-posted')
    if request.method == 'POST':
        if request.user.is_authenticated():
            form = LinkForm(data=request.POST,auto_id=True)
            if form.is_valid():
                form.full_clean()
                form.save()
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/accounts/login/?next=/')
    else:
        form = LinkForm(auto_id=True)
    return render(request, 'posts/links.html', {'links': links, 'form': form})

def comments(request, link_id):
    link = get_object_or_404(Link, pk=link_id)
    comments = link.comments.all()
    if request.method == 'POST':
        if request.user.is_authenticated():
            form = CommentForm(data=request.POST,auto_id=True)
            if form.is_valid():
                form.full_clean()
                form.save()
                return reverse('comments', kwargs={'link_id':link.id})
        else:
            return HttpResponseRedirect('/accounts/login/?next=/{0}/'.format(link.id))
    else:
        form = CommentForm(auto_id=True)
        return render(request, 'posts/comments.html', {'nodes':comments, 'link': link, 'form': form})
