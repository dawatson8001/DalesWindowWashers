from django import forms
from django.contrib.auth.forms import UserCreationForm
from Accounts_app.models import User
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):

    MONTH_ABBREVIATIONS = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
        'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
    ]
    MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
    YEAR_CHOICES = [(i, i) for i in xrange(2015, 2036)]

    credit_card_number = forms.CharField(label='Credit card number')
    cvv = forms.CharField(label='Security code (CVV)')
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    first_name = forms.CharField(label='Forename')
    last_name = forms.CharField(label='Surname')
    password1 = forms.CharField(
        label='password',
        widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )


    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2', 'stripe_id']
        exclude = {'username'}

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    def save(self, commit=True):
        instance = super(UserRegistrationForm, self).save(commit=False)

        instance.username = instance.email

        if commit:
            instance.save()

        return instance


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class PersonalDetailsForm(forms.Form):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Forename')
    last_name = forms.CharField(label='Surname')

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        exclude = {'username'}

    def save(self, commit=True):
        instance = super(PersonalDetailsForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance