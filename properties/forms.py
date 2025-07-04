from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    main_image = forms.ImageField(label="Main Property Image", required=False)

    class Meta:
        model = Property
        fields = [
            'title', 'description', 'property_type', 'listing_type', 'price',
            'location', 'state', 'bedrooms', 'bathrooms', 'square_feet', 'parking_spaces', 'year_built',
            'furnished', 'available', 'featured', 'min_stay_nights',
            'wifi', 'pool', 'gym', 'security', 'generator', 'kitchen', 'air_conditioning',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
               isinstance(field.widget, forms.NumberInput) or \
               isinstance(field.widget, forms.EmailInput) or \
               isinstance(field.widget, forms.URLInput) or \
               isinstance(field.widget, forms.PasswordInput):
                field.widget.attrs.update({
                    'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-zaffre-500 focus:border-zaffre-500 sm:text-sm'
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-zaffre-500 focus:border-zaffre-500 sm:text-sm resize-y',
                    'rows': '4' # Ensure rows attribute is also applied if not already
                })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': 'mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-zaffre-500 focus:border-zaffre-500 sm:text-sm rounded-md'
                })
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({
                    'class': 'h-4 w-4 text-zaffre-600 focus:ring-zaffre-500 border-gray-300 rounded'
                })
            elif isinstance(field.widget, forms.ClearableFileInput): # For ImageField
                field.widget.attrs.update({
                    'class': 'mt-1 block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-zaffre-50 file:text-zaffre-700 hover:file:bg-zaffre-100'
                })
            
            # Apply styling to the surrounding <p> tag for each field
            self.fields[field_name].widget.attrs['class'] = self.fields[field_name].widget.attrs.get('class', '')

            # Add general classes for the label of each field
            self.fields[field_name].label_attrs = {'class': 'block text-sm font-medium text-gray-700'}