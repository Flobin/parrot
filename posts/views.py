from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.db.models import F

from .models import Link, Comment
from .forms import LinkForm, CommentForm

def links(request):
    all_links = Link.objects.all().order_by('-posted')
    paginator = Paginator(all_links, 10) #show 10 links per page
    page = request.GET.get('page')

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
        try:
            links = paginator.page(page)
        except PageNotAnInteger:
            # in case of invalid page, serve homepage, should probably add error message
            links = paginator.page(1)
        except EmtyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            links = paginator.page(paginator.num_pages)
    return render(request, 'posts/links.html', {'links': links, 'form': form})

def comments(request, link_id, comment_id=None):
    link = get_object_or_404(Link, pk=link_id)
    if comment_id is not None:
        parent = get_object_or_404(Comment, pk=comment_id)
    else:
        parent = None
    comments = link.comments.all()
    if request.method == 'POST':
        if request.user.is_authenticated():
            form = CommentForm(data=request.POST,auto_id=True)
            if form.is_valid():
                form.full_clean()
                new_comment = form.save(commit=False)
                new_comment.link = link
                if parent:
                    new_comment.parent = parent
                new_comment.save()
                return redirect('comments', link_id=link.id)
        else:
            return HttpResponseRedirect('/accounts/login/?next=/{0}/'.format(link.id))
    else:
        form = CommentForm(auto_id=True)
        return render(request, 'posts/comments.html', {'nodes':comments, 'link': link, 'form': form})

def vote_link(request, link_id=None):
    link = Link.objects.get(pk=link_id)
    if request.user.is_authenticated():
        submit_vote_button = request.POST.get('submit_vote_button')
        if submit_vote_button == 'upvote':
            link.upvotes = F('upvotes') + 1
            link.save()
            return HttpResponseRedirect('/#{0}'.format(link.id))
        elif submit_vote_button == 'downvote':
            link.downvotes = F('downvotes') + 1
            link.save()
            return HttpResponseRedirect('/#{0}'.format(link.id))
    else:
        return HttpResponseRedirect('/accounts/login/?next=/#{0}'.format(link.id))

def vote_comment(request, link_id=None, comment_id=None):
    link = Link.objects.get(pk=link_id)
    comment = Comment.objects.get(pk=comment_id)
    if request.user.is_authenticated():
        submit_vote_button = request.POST.get('submit_vote_button')
        if submit_vote_button == 'upvote':
            comment.upvotes = F('upvotes') + 1
            comment.save()
            return HttpResponseRedirect('/{0}/#{1}'.format(link.id, comment.id))
        elif submit_vote_button == 'downvote':
            comment.downvotes = F('downvotes') + 1
            comment.save()
            return HttpResponseRedirect('/{0}/#{1}'.format(link.id, comment.id))
    else:
        return HttpResponseRedirect('/accounts/login/?next=/{0}/#{1}'.format(link.id, comment.id))
