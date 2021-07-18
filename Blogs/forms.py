from django.forms import forms,ModelForm
from .models import Blog
class NewForm(ModelForm):
    class Meta:
        model = Blog
        fields =[
            'Name','Background_Image','Paragraph1','Subheading1','Subheading2','Paragraph2','Subheading3'
            ,'Paragraph3','slug'
        ]
