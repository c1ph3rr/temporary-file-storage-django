from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column

from .models import StorageModel


class StorageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Upload', css_class='mt-2 btn btn-dark'))
        self.helper.layout = Layout(
            Row(
                Column('file', css_class='mt-4'),
            )
        )

    class Meta:
        model = StorageModel
        fields = ['file']
        labels = {
            'file': 'Select a file'
        }