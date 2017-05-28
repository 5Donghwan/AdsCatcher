from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blog/templates/index.html")

def reporting(request):
    return render(request, "blog/templates/reporting.html")

def feedback(request):
    return render(request, "blog/templates/feedback.html")