from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all().order_by('id')
    serializer_class = StockSerializer
    filter_backends = [SearchFilter]
    search_fields = ['products__title', 'products__description']

    def get_queryset(self):
        queryset = super().get_queryset()
        product_id = self.request.query_params.get('products')
        if product_id:
            queryset = queryset.filter(products=product_id)
        return queryset
