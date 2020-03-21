from rest_framework import generics, filters, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from bbs.models import Advert, Category
from api.serializers import AdvertSerializer, AdvertListSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
def api_root(request, format=None):
    """
    API root representation
    """
    return Response({
        'For testing use credential': 'User: test, password: QqnSnm9h6CxPSAP',
        'api_adverts_list': reverse('api_adverts_list', request=request, format=format),
        'api_categories_list': reverse('api_categories_list', request=request, format=format),
        'api_advert_create': reverse('api_advert_create', request=request, format=format),
    })


class AdvertsListView(generics.ListAPIView):
    """
    Ads List View
    """
    serializer_class = AdvertListSerializer
    queryset = Advert.objects.all()
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('price', 'create_datetime')


class AdvertDetailView(generics.RetrieveAPIView):
    """
    Ad Detail View
    """
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AdvertCreateView(generics.CreateAPIView):
    """
    Ad Create View
    """
    serializer_class = AdvertSerializer
    queryset = Advert.objects.all()
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated,)


class CategoryListView(generics.ListAPIView):
    """
    Category List View
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
