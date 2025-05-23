from ckeditor.widgets import CKEditorWidget
from django import forms
from blogpages.models import BlogDetail



class BlogDetailForm(forms.ModelForm):
    class Meta:
        model = BlogDetail
        fields = ['title', 'subtitle', 'body']
        widgets = {
            'body': CKEditorWidget(),
        }

