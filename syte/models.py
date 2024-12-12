from django.db import models
import os
import json
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator




class Text(models.Model):
    text=models.TextField(max_length=50,verbose_name="Write any information about yourself")
    text1=models.TextField(max_length=50, verbose_name="Write your questions")

    def __str__(self):
        return self.text
    


class Contact_link(models.Model):

    contact=models.CharField(max_length=3, choices=[
        ('FCB','FACEBOOK'),
        ('TWT', 'TWITTER'),
        ("BHN",  'BEHANCE'),
        ("LKD", "LINKEDIN"),
        ("DRB","DRIBBBLE"),
    ])

    
    def __str__(self):
        return self.get_contact_display()

class Topic(models.Model):
    
    title=models.CharField(max_length=16, verbose_name="Write the name of topic")
    description=models.CharField(max_length=50, verbose_name="Write the description")
    image=models.ImageField(upload_to="images/",verbose_name="Put the image", null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    information=models.TextField(max_length=950, verbose_name="Write the information about topic", null=True, blank=True)
    contact_links=models.ManyToManyField(Contact_link, verbose_name="Write the available contact links")
    short_desc=models.CharField(max_length=30, verbose_name="Write Characteristic 2 words", null=True, blank=True)

   
  
    def __str__(self):
        
        return self.description
    

class Comment(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=20, verbose_name="YOUR NAME")
    mail=models.EmailField(verbose_name="YOUR EMAIL")
    subject=models.CharField(max_length=255, verbose_name="SUBJECT")
    comment_text=models.TextField(max_length=50, verbose_name="TYPE YOUR COMMENT")
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.topic.title}"
    
phone_validator = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)
    
class ContactInfo(models.Model):
    phone_number=models.CharField(max_length=15, verbose_name="Write your phone number", blank=True, null=True)
    mail=models.EmailField(verbose_name="Your mail")
    address=models.CharField(max_length=50, verbose_name="Write your street address", validators=[phone_validator])

    def save(self, *args, **kwargs):
        if ContactInfo.objects.exists() and not self.pk:
            raise ValidationError("Only one contact info is allowed")
        super().save(*args,**kwargs)


class Message(models.Model):
    name=models.CharField(max_length=50, verbose_name="Write your name")
    email=models.EmailField()
    subject=models.CharField(max_length=255, blank=True)
    message=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} {self.email}"


class BlogTemplate(models.Model):
    template_name=models.CharField(max_length=60)
    title=models.CharField(max_length=60)
    button=models.CharField(max_length=16, default="Download Now!")
    
    def save(self,*args,**kwargs):
        if BlogTemplate.objects.exists() and not self.pk:
            raise ValidationError("Only one BlogTemplate instance is allowed.")
        
        super().save(*args,**kwargs)


   
    def __str__(self):
        return self.template_name
    
class Categories(models.Model):
    categories=models.CharField(max_length=30, verbose_name="Write any category")

    def __str__(self):
        return self.categories
    
class Tags(models.Model):
    tags=models.CharField(max_length=30, verbose_name="Write tha tags")

    def __str__(self):
        return self.tags
    

class About_us(models.Model):
    image=models.ImageField(upload_to='images/', verbose_name="Put the Image", null=True, blank=True)
    information=models.TextField(max_length=955, verbose_name="Write information about your page")
    donec_103=models.TextField(max_length=255, verbose_name="1-03 Donec porttitor augue")
    donec_203=models.TextField(max_length=255, verbose_name="2-03 Donec porttitor augue")
    donec_303=models.TextField(max_length=255, verbose_name="3-03 Donec porttitor augue")
    four_01=models.TextField(max_length=255, verbose_name="01 Four Columns")
    four_02=models.TextField(max_length=255, verbose_name="02 Four Columns")
    four_03=models.TextField(max_length=255, verbose_name="03 Four Columns")
    four_04=models.TextField(max_length=255, verbose_name="04 Four Columns")



class Toys(models.Model):
    toys_name=models.CharField(max_length=16, verbose_name="Write the name of toys")
    details=models.CharField(max_length=50, null=True, blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.toys_name
    

class Cars(models.Model):
    car_name=models.CharField(max_length=16, verbose_name="write the name of car",null=False)
    details=models.CharField(max_length=50, null=True, blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.car_name




