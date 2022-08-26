from django import forms
from products.models import Review, RATE_CHOICES, Product, Category


class RateForm(forms.ModelForm):
    """
    Form used to submit a product review. Takes a text area for inputing the
    written review as well as a choice field of scores from 1-5
    """
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'text-black'}), required=False)
    rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(
        attrs={'class': 'form-display'}), required=True)

    class Meta:
        """ Gives the text and rate form fields to the Review model """
        model = Review
        fields = ('text', 'rate')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_freindly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
