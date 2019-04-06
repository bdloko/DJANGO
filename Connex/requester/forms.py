from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from requester.models import Requester, Challenge, Comment, Dates
from django_bootstrap3_multidatepicker.django_bootstrap3_multidatepicker import widgets, fields

class RequesterForm(forms.ModelForm):

    class Meta:
        model = Requester
        fields = (
            'company',
            'address_line_1',
            'city',
            'postal_code',
            'email_address',
            'telephone',
            'picture',
            'description',
        )

class ChallengeForm(forms.ModelForm):
    closing = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Challenge
        fields = ['title', 'category', 'story', 'status', 'closing',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'comment', 'options'}

class DateInput(forms.DateInput):
    input_type = 'date'

class DatesForm(forms.ModelForm):

    class Meta:
        model = Dates
        fields = ['entry', 'entry_validation', 'scoring', 'faciliated_judging', 'announce_finalists', 'presentation', 'winners_announcement']
        widgets = {
            'entry': DateInput(),
            'entry_validation': DateInput(),
            'scoring': DateInput(),
            'faciliated_judging': DateInput(),
            'announce_finalists': DateInput(),
            'presentation': DateInput(),
            'winners_announcement' :DateInput(),
        }