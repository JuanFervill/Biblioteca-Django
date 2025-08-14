from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime #for checking renewal date range.

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Introduzca una fecha entre ahor y 3 semanas")
    
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        if data < datetime.date.today():
            raise ValidationError(_('Fecha pasada, introduzca una nueva'))
        
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Fecha pasada 4 semanas, introduzca una nueva'))
        
        return data