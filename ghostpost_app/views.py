from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from ghostpost_app.models import GhostModel
from ghostpost_app.forms import GhostForm, AddFilter


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = AddFilter(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['add_filter'] == '---------':
                result = GhostModel.objects.order_by('date')
            elif data['add_filter'] == 'all_boasts':
                result = GhostModel.objects.order_by(
                    'date').filter(boast_or_roast=True)
            elif data['add_filter'] == 'all_roasts':
                result = GhostModel.objects.order_by(
                    'date').filter(boast_or_roast=False)
            elif data['add_filter'] == 'up_vote':
                result = GhostModel.objects.order_by('-up_vote', 'date')
            elif data['add_filter'] == 'down_vote':
                result = GhostModel.objects.order_by('-down_vote', 'date')
            elif data['add_filter'] == 'vote_difference':
                result = GhostModel.objects.extra(
                    select={'diff': 'up_vote - down_vote'}).order_by('-diff')
        return render(request, 'index.html', {'result': result, 'form': form})

    form = AddFilter()
    result = GhostModel.objects.order_by('date')

    return render(request, 'index.html', {'result': result, 'form': form})


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
