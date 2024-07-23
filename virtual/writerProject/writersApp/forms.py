from django import forms

class BookForm(forms.ModelForm)
    class Meta:
        model = Order
        fields = "__all__"
