from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from ghostpost_app.models import GhostModel
from ghostpost_app.forms import GhostForm, AddFilter, DeletePost
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
        return render(request, 'magic.html', {'key': magic_str})

    form = GhostForm()
    return render(request, 'addpost.html', {'form': form})


def for_up_vote(request, post_id=None, magic=None):
    if post_id:
        post = GhostModel.objects.get(id=post_id)
    else:
        post = GhostModel.objects.get(magic=magic)
    post.up_vote += 1
    post.save()
    if post_id:
        return HttpResponseRedirect(reverse('posts', kwargs={'post_id': post_id}))
    else:
        return HttpResponseRedirect(reverse('magic_post', kwargs={'magic': magic}))


def for_down_vote(request, post_id=None, magic=None):
    if post_id:
        post = GhostModel.objects.get(id=post_id)
    else:
        post = GhostModel.objects.get(magic=magic)
    post.down_vote += 1
    post.save()
    if post_id:
        return HttpResponseRedirect(reverse('posts', kwargs={'post_id': post_id}))
    else:
        return HttpResponseRedirect(reverse('magic_post', kwargs={'magic': magic}))


def post_details(request, post_id):
    secret_key = GhostModel.objects.get(id=post_id).magic

    if request.method == 'POST':
        form = DeletePost(request.POST)
        if form['secret_key'].value() == secret_key:
            return HttpResponseRedirect(reverse("magic_post", kwargs={"magic": secret_key}))

    data = GhostModel.objects.get(id=post_id)
    form = DeletePost()

    return render(request, 'posts.html', {'data': data, 'form': form})


def magic_post(request, magic):
    data = GhostModel.objects.get(magic=magic)
    return render(request, 'posts.html', {'data': data})


def delete_post(request, magic):
    GhostModel.objects.filter(magic=magic).delete()
    return HttpResponseRedirect(reverse('homepage'))
