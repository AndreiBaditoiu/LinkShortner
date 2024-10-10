from django.shortcuts import render, get_object_or_404, redirect

from .models import Link


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

