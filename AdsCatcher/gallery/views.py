from django.shortcuts import render
from .models import Gallery

# Create your views here.
def gallery_list(request):
    gallery_list = Gallery.objects.all().order_by("id")

    return render(request, "gallery/index.html", {
        "gallery_list": gallery_list
    })