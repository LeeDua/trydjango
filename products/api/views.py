from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

from products.models import Product
from products.api.serializers import ProductSerializer

@api_view(['GET',])
def api_detail_product_view(request):
    try:
        product = Product.objects.get(id=1)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return JsonResponse({"prop1":"hey", "img":"some_fake_url.jpg","title":product.title})


@api_view(['PUT',])
def api_update_product_view(request):
    try:
        product = Product.objects.get(id=1)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = ProductSerializer(product)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_update_product_view(request):
    try:
        product = Product.objects.get(id=1)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        # operation = xx.delete()
        data = {}
        if True:
        # if operation:
            data["success"] = "delete successful"
            return Response(data=data)
        else:
            data['success'] = "delete failed"
        return Response(data=data)


