from django.shortcuts import render, get_object_or_404, redirect

from .models import Link
from .forms import LinkForm


# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        'links': links
    }
    return render(request, 'index.html', context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()
    return redirect(link.url)


def add_link(request):
    if request.method == "POST":
        # form has data
        form = LinkForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:

        form = LinkForm()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)
