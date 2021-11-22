from django import forms
from tickets.models import Ticket


class PriorityForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('task_priority',)


class StatusForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('ticket_status',)


class LanguageForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ('language_choices',)


class TicketCreate(forms.ModelForm):
    company_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Company name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
    deadline = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Deadline', 'readonly': True}))
    if_fast = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    market_geography = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Market geography'}))
    short_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Short description'}))
    long_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Long description'}))
    comments = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Input comments', 'blank': True}))

    class Meta:
        model = Ticket
        fields = ('company_name', 'email', 'phone_number', 'deadline', 'task_priority', 'short_description', 'long_description', 'market_geography', 'language_choices', 'comments',)

    class Media:
        js = ('js/datepicker.js',)

    def __init__(self, *args, **kwargs):
        super(TicketCreate, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
