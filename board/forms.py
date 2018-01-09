from django import forms
from .models import Post,Upload


class PostForm(forms.ModelForm):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes',
        required=False
    )
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
