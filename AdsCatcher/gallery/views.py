from django.shortcuts import render
from .forms import GalleryForm
from .models import Gallery
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "gallery/index.html")

def gallery_list(request):
    gallery_list = Gallery.objects.all().order_by("-id")

    return render(request, "gallery/index.html", {
        "gallery_list": gallery_list
    })

@login_required
def gallery_new(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.author = request.user
            gallery.save()
            return redirect("gallery:index")
    else:
        form = GalleryForm()
    return render(request, "gallery/gallery_form.html", {"form": form})