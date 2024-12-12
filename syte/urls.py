from django.urls import path
from . import views
from .views import DataTo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    
    path('post-details/', views.post_details, name='post-details'),
    path('contact/', views.contact, name='contact'),
   
   

    path('login/', views.login_, name='login'),
    path('register/', views.register_, name='register'),
    path('logout/', views.logout_, name='logout'),

    path('text/create', views.text_create, name='text_create'),
    path('text/<int:pk>', views.text_detail, name='text_detail'),

    path('post-details/<int:id>/', views.PostDetailView.as_view(), name='topic_details'),  


    path('add-comment', views.AddCommentView.as_view(), name='add_comment'),
    

 

    path('data-to/', DataTo.as_view(), name='data_to'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)