from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from ghostpost_app.models import GhostModel
from ghostpost_app.forms import GhostForm, AddFilter
from ghostpost_app.helpers import order_posts, get_magic_str


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AddFilter(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            result = order_posts(data, GhostModel)
        return render(request, 'index.html', {'result': result, 'form': form})

    form = AddFilter()
    result = GhostModel.objects.order_by('date')

    return render(request, 'index.html', {'result': result, 'form': form})


def addpost(request):
    if request.method == "POST":
        form = GhostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            magic_str = get_magic_str()
            GhostModel.objects.create(
                text=data['text'], boast_or_roast=data['boast_or_roast'], magic=magic_str
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = GhostForm()
    return render(request, 'addpost.html', {'form': form})


def for_up_vote(request, post_id):
    post = GhostModel.objects.get(id=post_id)
    post.up_vote += 1
    post.save()
    return HttpResponseRedirect(reverse('posts', kwargs={'post_id': post_id}))


def for_down_vote(request, post_id):
    post = GhostModel.objects.get(id=post_id)
    post.down_vote += 1
    post.save()
    return HttpResponseRedirect(reverse('posts', kwargs={'post_id': post_id}))


def post_details(request, post_id):
    data = GhostModel.objects.get(id=post_id)
    return render(request, 'posts.html', {'data': data})


def magic_post(request, magic):
    data = GhostModel.objects.get(magic=magic)
    return render(request, 'posts.html', {'data': data})
