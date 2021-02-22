from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: 
        #class meta tell Django which model should be used to create this form 
        model = Post
        fields = ('title', 'text',)