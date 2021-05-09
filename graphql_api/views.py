import shopify
from shopify_app.decorators import shop_login_required
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
import ast
import requests


@shop_login_required
def index(request):
    return 'test'

class ShopView(APIView):
    def get(self, request, *args, **kwargs):
        client = shopify.GraphQL()
        query = '''
            {
		        shop	{
				    id
				    name
				    email
		        }
            }
        '''
        result = client.execute(query)
        result = ast.literal_eval(result)
        return Response(result['data'])

class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        client =  shopify.GraphQL()
        query = '''
            {
                products(first: 10)  {
                    edges   {
                        node    {
                            id
                            handle
                            title
                        }
                    }
                }
                productVariants(first:10){
                    edges{
                    node{
                        title
                    }
                    }
                }
            }
        '''
        test = ['test', 'test']
        result = client.execute(query)
        result = ast.literal_eval(result)
        result['data']['products']['edges'][0]['node']['test'] = test
        return Response(result['data'])

class CollectionView(APIView):
    def get(self, request, *args, **kwargs):
        client =  shopify.GraphQL()
        query = '''
            {
                collections(first: 5){
                    edges{
                    node{
                        products (first: 5){
                        edges {
                            node {
                            id
                            }
                        }
                        }
                        title
                    }
                    }
                }
            }
        '''
        result = client.execute(query)
        result = ast.literal_eval(result)
        return Response(result['data'])

class CustomerView(APIView):
    def get(self, request, *args, **kwargs):
        client =  shopify.GraphQL()
        query = '''
            {
                customers(first:1){
                    edges{
                    node{
                        email
                        displayName
                    }
                    }
                }
            }
        '''
        result = client.execute(query)
        result = ast.literal_eval(result)
        return Response(result['data'])