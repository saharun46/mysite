from django import forms 
class EmailPostForm(forms.Form):
    name = forms.Charfield(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)







## field2 = forms.ModelChoiceField(queryset=..., to_field_name="name")
