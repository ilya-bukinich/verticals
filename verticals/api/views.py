from rest_framework import generics, filters, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny
from bbs.models import Advert, Category
from api.serializers import AdvertSerializer, AdvertListSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'api_adverts_list': reverse('api_adverts_list', request=request, format=format),
        'api_categories_list': reverse('api_categories_list', request=request, format=format),
        'api_advert_create': reverse('api_advert_create', request=request, format=format),
    })


class AdvertAPIDetailView(generics.RetrieveAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    permission_classes = (AllowAny,)


class AdvertsAPIListView(generics.ListAPIView):
    serializer_class = AdvertListSerializer
    queryset = Advert.objects.all()
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    ordering_fields = ('price', 'create_datetime')


class AdvertAPICreateView(generics.CreateAPIView):
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    permission_classes = (AllowAny,)


class CategoryAPIListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)
