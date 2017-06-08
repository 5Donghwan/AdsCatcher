from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from allauth.socialaccount.models import SocialAccount, SocialToken
# Create your views here.
def login_index(request):
    return render(request, "blog/login_index.html")

# def socialToken_list(request):
    
#     social_account_list = SocialAccount.objects.all()    
#     return render(request,'blog/login_index.html',{
#         'social_account_list': social_account_list,
#     })
