from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from ghostpost_app.models import GhostPost
from ghostpost_app.forms import AddPost


# Create your views here.
def index(request):
    return render(request, 'index.html')


def submitpage(request):
    if request.method == "POST":
        form = AddPost(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = AddPost()
    return render(request, 'submitpage.html', {'form': form})
