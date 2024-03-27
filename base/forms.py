from . models import Comment,Contact
from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["name","body"]


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"