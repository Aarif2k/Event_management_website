from django import forms 
from .models import Booking
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit


class DateInput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets= {
            'booking_date':DateInput(),
        }

        labels={
            'name':"Event Name"
        }

    # def __init__(self, *args, **kwargs):
    #     super(BookingForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.layout = Layout(
    #         'field1',
    #         'field2',
    #         'field3',
    #         Submit('submit', 'Book Now')
    #     )