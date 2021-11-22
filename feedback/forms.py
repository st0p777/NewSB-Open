from django import forms
from feedback.models import FeedBack


class NewFeedBack(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}), required=True)

    class Meta:
        model = FeedBack
        fields = ('username', 'email', 'phone', 'message',)

    def __init__(self, *args, **kwargs):
        super(NewFeedBack, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

