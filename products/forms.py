from django import forms

from .models import Product 

class ProductForm(forms.ModelForm):
    username = forms.CharField(
        label="User name",
        widget=forms.TextInput(attrs={"placeholder": "Enter username . . ."})
    )
    email = forms.EmailField(widget = forms.TextInput(attrs ={"Placeholder" : "Enter Email . . ."} ))
    description = forms.CharField(
        label="Description",
        widget=forms.TextInput(attrs={"placeholder": "Enter Description . . ."})
    )
    price = forms.DecimalField(
        initial=0,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter price . . .',
            'class': 'pl-10 w-full border border-gray-300 rounded-md py-2 pr-3 placeholder-gray-400 placeholder-opacity-70 placeholder:font-light focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition'
        })
    )
    isActive = forms.BooleanField(
        required=False,
        label="I agree to the terms and conditions",
        help_text="You must agree before submitting."
    )

    class Meta:
        model = Product 
        fields = [
            'username',
            'description',
            'email',
            'price',
            'isActive'
        ]

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        # if not "CFE" in title: 
        #     raise forms.ValidationError("This is not a valid username")
        # if not "news" in title: 
        #     raise forms.ValidationError("This is not a valid title")
        return username

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        # if not email.endswith("edu"):
        #     raise forms.ValidationError("This is not valid email")
        return email
