from django.shortcuts import render
from django.views import generic
from .models import Advert, Category


# Create your views here.
def index(request):
    num_ads = Advert.objects.all().count()
    list_cats = Category.objects.all().count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={'num_ads': num_ads, 'list_cats': list_cats, 'num_visits': num_visits},
    )


class AdvertDetailView(generic.DetailView):
    model = Advert


class AdvertListView(generic.ListView):
    model = Advert
    paginate_by = 10
