from django.shortcuts import render

# Create your views here.
def report(request):
    return render(request, "communication/report.html")

def feedback(request):
    return render(request, "communication/feedback.html")