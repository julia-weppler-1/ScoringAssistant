# excel_app/forms.py
from django import forms

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Upload Excel File')
