from django.urls import path
from products.api.views import api_detail_product_view


app_name = 'some_arb_name'

urlpatterns = [
    path('', api_detail_product_view, name="anything")
]