from django import forms
from multiselectfield import MultiSelectField


class fUpload(forms.Form):
    CHOICES = [('eng', 'English'), ('urd', 'Urdu'), ('tel', 'Telugu')]
    langs = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                      choices=CHOICES)

    CHOICES_FILE = [('0', 'Image'), ('1', 'PDF')]
    file_type = forms.ChoiceField(widget=forms.RadioSelect,
                                  choices=CHOICES_FILE)

