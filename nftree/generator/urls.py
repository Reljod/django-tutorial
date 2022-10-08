from django.urls import path
from . import views

app_name = 'generator'
urlpatterns = [
    path('', views.Generate.as_view(), name='generate'),
    path('all', views.nfts, name='nfts'),
    path('<id>', views.nft_details, name='nft')
]