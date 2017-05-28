from django.shortcuts import render

# Create your views here.
def login_index(request):
    return render(request, "blog/login_index.html")

def report(request):
    return render(request, "blog/report.html")

def feedback(request):
    return render(request, "blog/feedback.html")