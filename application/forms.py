from django import forms

from application.models import Reservation



class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter your phone number'}),
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'min'': str(date.today()), style' : 'width: 100%'}),
            'reservation_time': forms.DateInput(attrs={'type': 'time', 'style' : 'width: 100%'}),
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the number of guests'}),
            'special_request': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter any special request (optional)', 'rows': 3, 'style': 'width: 100%; max-width: 100%;'}),
        }
