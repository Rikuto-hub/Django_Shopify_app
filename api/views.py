import shopify
from shopify_app.decorators import shop_login_required
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import json
# from rest_framework.generics import get_object_or_404
# from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from django.http.response import JsonResponse


class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        products = shopify.Product.find(limit=10)
        result = []
        for product in products:
            data = {}
            data['id'] = product.id
            data['title'] = product.title
            data["price"] = product.variants[0].price
            result.append(data)
        response = {
            'products': result
        }
        return Response(response)

class CollectionView(APIView):
    def get(self, request, *args, **kwargs):
        collections = shopify.CustomCollection.find(limit=10)
        products = collections[0].products()
        result = []
        for collection in collections:
            data = {}
            data['id'] = collection.id
            data['title'] = collection.title
            products = collection.products()
            products_of_collection = []
            for product in products:
                data_v2 = {
                    'id': product.id,
                    'title': product.title,
                    'price': product.variants[0].price,
                }
                products_of_collection.append(data_v2)
            data['products'] = products_of_collection
            result.append(data)
        response = {
            'collections': result
        }
        return Response(response)

class OrderView(APIView):
    def get(self, request, *args, **kwargs):
        order = shopify.Order.find(limit=10)
        print(order)
        return Response("aaaaa")

