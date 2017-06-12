from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Blog
from allauth.socialaccount.models import SocialAccount, SocialToken
#for telegram bot sending message
import telegram 

bot = telegram.Bot(token='384831612:AAF_QK-qKzIdYbgEJ6ksjjckTxU_GabhlIo')
chat_id = bot.get_updates()[-1].message.chat.id
# Create your views here.
def login_index(request):
    blog_list = Blog.objects.all().order_by("-created_at")

    compared_title = blog_list[0].feed_title
    compared_created_time = blog_list[0].created_at

    for blog in blog_list:
        if blog.created_at == compared_created_time:
            if blog.feed_title != compared_title:
                blog.state = "modified"
                bot.sendMessage(chat_id=chat_id, text='광고를 잡은거 같아요!')
                Blog.objects.filter(feed_title = str(compared_title)).delete()
            else:
                pass
        else:
            pass
        compared_created_time = blog.created_at
        compared_title = blog.feed_title
        
    return render(request, "blog/login_index.html", {
        "blog_list": blog_list
    })

# def socialToken_list(request):
    
#     social_account_list = SocialAccount.objects.all()    
#     return render(request,'blog/login_index.html',{
#         'social_account_list': social_account_list,
#     })
