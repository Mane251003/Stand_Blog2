from django.contrib import admin
from .models import Text,Topic,Comment, BlogTemplate, Contact_link, About_us, Categories, ContactInfo, Message, Tags
from .forms import MessageForm

admin.site.register(Text)
admin.site.register(Comment)
admin.site.register(BlogTemplate)
admin.site.register(About_us)
admin.site.register(Categories)
admin.site.register(Tags)
admin.site.register(ContactInfo)
admin.site.register(Message)

@admin.register(Contact_link)
class ContactLinkAdmin(admin.ModelAdmin):
    list_display = ('contact',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created')
    filter_horizontal = ('contact_links',)