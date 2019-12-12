from django.urls import path
from .views import upload_single


app_name = 'image_uploader'

urlpatterns = [
    path('', upload_single, name='upload-single')
]