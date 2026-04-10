from django import forms

class CoverForm(forms.Form):
    title = forms.CharField(label="Magazine Title", max_length=50)
    headline = forms.CharField(label="Main Headline", max_length=100)
    bg_color = forms.CharField(label="Background Color", widget=forms.TextInput(attrs={'type': 'color', 'value': '#ffffff'}))
    font_color = forms.CharField(label="Font Color", widget=forms.TextInput(attrs={'type': 'color', 'value': '#000000'}))
    font_size = forms.IntegerField(label="Font Size (px)", min_value=10, max_value=100, initial=40)
    magazine_image = forms.ImageField(label="Upload Cover Image", required=False)
