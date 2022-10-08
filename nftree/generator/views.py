from audioop import reverse
from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from typing import List

from generator.models import NFT

def nfts(request: HttpRequest) -> HttpResponse:
    nft_objects = NFT.objects.all()    
    context = { 'nfts': nft_objects }
    return render(request, 'generator/nfts.html', context)

def nft_details(request: HttpRequest, id: str) -> HttpResponse:
    nft_object = get_object_or_404(NFT, pk=id)
    context = { 'nft': nft_object }
    return render(request, 'generator/nft.html', context)

class Generate(TemplateView):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'generator/index.html', {})

    def post(self, request, *args, **kwargs):
        
        name = request.POST['name']
        
        nft = NFT(name=name, image_url="www.example.com")
        nft.save()
        
        nft_id: str = nft.id
        
        return HttpResponseRedirect(reverse('generator:nft', args=(nft_id, )))
    