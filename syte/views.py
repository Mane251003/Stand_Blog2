from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse,  FileResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import engines


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.conf import settings

from .models import Text,Topic, BlogTemplate, Cars, Toys,About_us, Comment, Categories, Contact_link, ContactInfo, Message, Tags
from .forms import TextForm, MessageForm

from django.http import JsonResponse
from django.views import View
from decimal import Decimal
from datetime import datetime

import logging
import json
import os 
import re
import requests
import hashlib

from django.http import JsonResponse



def index(request):
    topics=Topic.objects.prefetch_related('contact_links').all()
    topic_comment_counts=[]
    recent_topics=Topic.objects.order_by('-created')[:3]
    recent_topic=Topic.objects.order_by('-created').first()
  
    categories=Categories.objects.all()
    tags=Tags.objects.all()
    contact_links=Contact_link.objects.all()
  
    try:
        blog_template=BlogTemplate.objects.get()
    except BlogTemplate.DoesNotExist:
        blog_template=None

    for topic in topics:
 
        comment_count=topic.comments.count()
       
    
        topic_comment_counts.append({'topic':topic, 'comment_count':comment_count})
       
     
        


    context={'topic_comment_counts':topic_comment_counts, 'blog_template':blog_template,'recent_topics': recent_topics, 'categories':categories, 'contact_links':contact_links, 'tags':tags , 'recent_topic':recent_topic}
    return render(request, 'syte/index.html', context)

def about(request):

    try:
        about_us=About_us.objects.get()

    except About_us.DoesNotExist:
        about_us=None

    context={'about_us':about_us}
    return render(request, 'syte/about.html', context)

def blog(request):

    try:
        blog_template=BlogTemplate.objects.get()

    except BlogTemplate.DoesNotExist:
        blog_template=None

    categories=Categories.objects.all()
    tags=Tags.objects.all()
    topics=Topic.objects.all()
    topic_comment_counts=[]
    recent_topics=Topic.objects.order_by('-created')[:3]
    recent_topics_all=[]
    contact_links=Contact_link.objects.all()

    for topic in topics:
        comment_count=topic.comments.count()
        topic_comment_counts.append({'topic':topic, 'comment_count': comment_count})

    for rec_topic in recent_topics:
        comment_count=topic.comments.count()
        recent_topics_all.append({'topic':rec_topic, 'comment_count':comment_count})

    
    context={'blog_template':blog_template, 'topic_comment_counts':topic_comment_counts, 'recent_topics':recent_topics_all, 'categories':categories, 'tags':tags, 'contact_links':contact_links}

    return render(request, 'syte/blog.html', context)

def post_details(request, id):

    comments=Comment.objects.all()
    topic=get_object_or_404(Topic, id=id)
    topics=Topic.objects.all()
    categories=Categories.objects.all()
    tags=Tags.objects.all()
    topic_comment_counts=[]
    recent_topics=Topic.objects.order_by('-created')[:3]

    try:
        blog_template=BlogTemplate.objects.get()
   
    except BlogTemplate.DoesNotExist:
        blog_template=None

    print(f"blog template is {blog_template}")


    for topic in topics:
        comment_count=topic.comments.count()
        topic_comment_counts.append({'topic':topic, 'comment_count': comment_count})
    context={'comments':comments, 'recent_topics':recent_topics, 'topic_comment_counts':topic_comment_counts, 'topics':topics, 'categories':categories, 'tags':tags, 'blog_template':blog_template}

    return render(request, 'syte/post-details.html', context)

def contact(request):

    @staticmethod
    def is_valid_email(email):
       email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

       return re.match(email_regex, email) is not None
    
    try:
        contact_info=ContactInfo.objects.get()
    except ContactInfo.DoesNotExist:
        contact_info=None

    if request.method == 'POST':

        form=MessageForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            if not is_valid_email(email):
                form.add_error('email', 'Invalid email format.')
            else:

                Message.objects.create(
                   name=name,
                   email=email,
                   subject=subject,
                   message=message,
)
                
                return render(request, 'syte/index.html')

         
    else:
        form=MessageForm()


    
    
    context={'contact_info':contact_info , 'form':form}
    return render(request, 'syte/contact.html', context)




def download_file(request):
    file_path=os.path.join(settings.BASE_DIR, '/home/mane/Downloads/templatemo_551_stand_blog.zip')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='/home/mane/Downloads/templatemo_551_stand_blog.zip')



def register_(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrations succesfull, Log in')
            return redirect('login')
        
        else:
            messages.error(request, "Error, please try again")

    else:
        form=UserCreationForm()

    return render(request, 'syte/sign.html', {'form': form})

        
def login_(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Succesfull")

                return redirect('index')

            else:
                messages.error("False username or password")

        else:
            messages.error("False username or password")

    else:
        form=AuthenticationForm()
    return render(request, 'syte/login.html', {'form':form})



def logout_(request):
    logout(request)
    messages.success(request, "You logged out")
    return redirect('logout')

    
def text_create(request):

    if request.method=="POST":
        form=TextForm(request.POST)

        if form.is_valid():
            item=form.save()
            

            return redirect('text_detail',pk=item.pk)
    
    else:
        form=TextForm()
    return render(request, 'syte/text_create.html', {'form':form}) 
    

def text_detail(request, pk):

    text_instance=get_object_or_404(Text, pk=pk)

    return render(request, 'syte/text_detail.html', {'text': text_instance})



  

logger=logging.getLogger(__name__)



class PostDetailView(View):
    
    def get(self, request, id, *args, **kwargs):

        if id:

           topic=get_object_or_404(Topic, id=id)
           recent_topics=Topic.objects.order_by('-created')[:3]
           categories=Categories.objects.all()
           tags=Tags.objects.all()
           
           print(f"Original topic is {topic}")
           topic_id=id
           try:

            blog_template=BlogTemplate.objects.get()
   
           except BlogTemplate.DoesNotExist:
            blog_template=None
          
           context={
               'topic':topic,
               'comments':topic.comments.all(),
               'comment_count':topic.comments.count(),
               'topic_id':topic_id,
               'categories':categories, 
               'tags':tags, 
               'blog_template':blog_template,
               'recent_topics':recent_topics,
               'tags':tags,

           }

        else:
           return HttpResponse("That's not available")
     
        return render(request, 'syte/post-details.html', context)
    

class AddCommentView(View):

    @staticmethod
    def is_valid_email(email):
       email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

       return re.match(email_regex, email) is not None


    def post(self, request, *args, **kwargs):
       
        topic_id = request.POST.get('topic_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

    
        if not self.is_valid_email(email):
            return JsonResponse({"error": "Invalid email format"}, status=400)

        api_key = "9086191e383ff51739befc97024bbd561e4d4c1a"
        api_url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}"

        try:
            response = requests.get(api_url)
            print("Hunter API Response:", response.text)

            if response.status_code == 200:
                email_data = response.json()
                email_status = email_data.get('data', {}).get('status')
                email_result = email_data.get('data', {}).get('result')

                if email_status == "invalid" or email_result == "invalid":
                    return JsonResponse({"error": "Email is invalid."}, status=400)
            else:
                print("Hunter.io API returned non-200 status:", response.status_code)
        except Exception as e:
            return JsonResponse({"error": "Email verification failed.", "details": str(e)}, status=500)

      
        subject = self.get_grav_or_picture(email)
        print(f"Subject URL: {subject}")

        try:
            topic = get_object_or_404(Topic, id=topic_id)
            Comment.objects.create(
                topic=topic,
                name=name,
                mail=email,
                subject=subject,
                comment_text=message,
            )
        except ValueError:
            return HttpResponse("Invalid topic ID.", status=400)

        return redirect('topic_details', id=topic.id)

    @staticmethod
    def get_grav_or_picture(email):
       
        email = email.strip().lower()
        email_hash = hashlib.md5(email.encode('utf-8')).hexdigest()
        gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}?d=identicon&s=200"
        return gravatar_url
        



   
class AddMessageView(View):
    def post(self, request, *args, **kwargs):
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')



class DataTo(View):
    def get(self, request, *args, **kwargs):

        data=list(Cars.objects.all().values())
        data1=list(Toys.objects.all().values())
        
        topics=Topic.objects.all()
        data2=[]

        data3=list(BlogTemplate.objects.all().values())
        data4=list(Topic.objects.order_by('-created')[:3].values())
        data5=list(Categories.objects.all().values())
        messages=Message.objects.all()
        contact_info = ContactInfo.objects.first()

        if contact_info:
            contact_data = {
                'phone_number': contact_info.phone_number,
                'mail': contact_info.mail,
                'address': contact_info.address
            }
        else:
            contact_data = {}



        for topic in topics:
            comments=topic.comments.all()
            comment_data=[]

            for comment in comments:
                comment_data.append({
                     'name': comment.name,
                    'email': comment.mail,
                    'subject': comment.subject,
                    'comment_text': comment.comment_text,
                    'created': comment.created.strftime("%Y-%m-%d %H:%M:%S"),
                })



            data2.append({
                'id': topic.id,
                'title':topic.title,
                'description':topic.description,
                'image': topic.image.url if topic.image else None,
                'created': topic.created.strftime("%Y-%m-%d %H:%M:%S"),
                'information':topic.information,
                'contact_links':[link.get_contact_display() for link in topic.contact_links.all()],
                'short_desc':topic.short_desc,
                'comments':comment_data,
               
            })
  
        for item in data:
            for i,j in item.items():
                if isinstance(j, Decimal):
                    item[i] = float(j)

        for item in data1:
            for i,j in item.items():
                if isinstance(j, Decimal):
                    item[i] = float(j)

        for item in data4:

            if isinstance(item['created'], datetime):
                item['created'] = item['created'].strftime("%Y-%m-%d %H:%M:%S")

        data6 = []

        for message in messages:
            data6.append({
                'name': message.name,
                'email': message.email,
                'subject': message.subject,
                'message': message.message,
                'created': message.created.strftime("%Y-%m-%d %H:%M:%S"), 
            })


            

        all_data={'Topic': data2, 'blog_template': data3, 'recent_posts': data4, 'categories':data5, 'messages':data6, 'contact_info':contact_data}
        json_data = json.dumps(all_data, indent=4)
        with open(os.path.join('syte', 'dataa.json'), 'w') as f:
            f.write(json_data)
            
 
        
  
        return JsonResponse(all_data, safe=False)
   


