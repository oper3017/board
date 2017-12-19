from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

CHOICES= [
    ('1', '제목'),
    ('2', 'ID'),
    ('3', '내용'),
    ]

class BoardSearchForm(forms.Form):
    search_word = forms.CharField(label='검색')
    search_filter= forms.CharField(widget=forms.Select(choices=CHOICES))


    