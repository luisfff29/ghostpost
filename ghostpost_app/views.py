from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from ghostpost_app.models import GhostModel
from ghostpost_app.forms import GhostForm


# Create your views here.
def index(request):
    data = GhostModel.objects.all()
    return render(request, 'index.html', {'data': data})


def addpost(request):
    if request.method == "POST":
        form = GhostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostModel.objects.create(
                text=data['text'], boast_or_roast=data['boast_or_roast']
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = GhostForm()
    return render(request, 'addpost.html', {'form': form})


def for_up_vote(request, post_id):
    post = GhostModel.objects.get(id=post_id)
    post.up_vote += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def for_down_vote(request, post_id):
    post = GhostModel.objects.get(id=post_id)
    post.down_vote += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))
