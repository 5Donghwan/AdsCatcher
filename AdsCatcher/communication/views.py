from django.shortcuts import render, redirect
from .forms import ReportForm, FeedbackForm
from .models import Report, Feedback
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def report_new(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.author = request.user
            report.save()
            form.save()
            return redirect('communication:report_new')
    else:
        form = ReportForm()
    return render(request, "communication/report.html", {"form": form})

@login_required
def feedback_new(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.author = request.user
            feedback.save()
            form.save()
            return redirect('communication:feedback_new')
    else:
        form = FeedbackForm()
    return render(request, "communication/feedback.html", {"form": form})

    