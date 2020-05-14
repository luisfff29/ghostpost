from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from ghostpost_app.models import GhostPost
from ghostpost_app.forms import AddPost


# Create your views here.
def index(request):
    data = GhostPost.objects.all()
    return render(request, 'index.html', {'data': data})


def submitpage(request):
    if request.method == "POST":
        form = AddPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            GhostPost.objects.create(
                text=data['text'], boast_or_roast=data['boast_or_roast']
            )
        return HttpResponseRedirect(reverse('homepage'))

    form = AddPost()
    return render(request, 'submitpage.html', {'form': form})
