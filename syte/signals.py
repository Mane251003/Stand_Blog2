import json
import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Topic, Comment, BlogTemplate
from django.conf import settings

#JSON_FILE_PATH = '/home/mane/Downloads/stand_blog/syte/data.json'
JSON_FILE_PATH = os.path.join(settings.BASE_DIR, 'syte', 'data.json')
def write_data_to_json():

    try:
        blog_template = BlogTemplate.objects.get()
        download_data = {
            "template_name": blog_template.template_name,
            "title": blog_template.title,
            "button": blog_template.button
        }
    except BlogTemplate.DoesNotExist:
        download_data = {}
     




    item_data =  [
            {
                "id": topic.id,
                "title": topic.title,
                "description": topic.description,
                "created": topic.created.isoformat(),
                "image": topic.image.url if topic.image else None,
                "comments": [
                    {
                        "id": comment.id,
                        "name": comment.name,
                        "mail": comment.mail,
                        "subject": comment.subject,
                        "comment_text": comment.comment_text,
                        "created": comment.created.isoformat()
                    }
                    for comment in topic.comments.all()
                ],
            }
            for topic in Topic.objects.prefetch_related('comments').all()
        ]
    
    data = {
        "download_data": download_data,
        "item": item_data
    }
    with open(JSON_FILE_PATH, 'w') as f:
        json.dump(data, f, indent=4)
   

@receiver([post_save, post_delete], sender=Topic)
@receiver([post_save, post_delete], sender=Comment)
def update_json_on_save_delete(sender, instance, **kwargs):
    write_data_to_json()
