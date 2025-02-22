from django import forms


class BaseForm(forms.Form):
    """
    BaseForm personalizado para adicionar classes CSS aos campos automaticamente.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if any([
               isinstance(field.widget, forms.TextInput),
               isinstance(field.widget, forms.Textarea),
               isinstance(field.widget, forms.NumberInput),
            ]):
                field.widget.attrs.setdefault('class', 'form-control')
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.setdefault('class', 'form-select')
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.setdefault('class', 'form-check-input')
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs.setdefault('class', 'form-file')


class BaseModelForm(forms.ModelForm):
    """
    BaseForm personalizado para Models para adicionar classes CSS aos campos automaticamente.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if any([
               isinstance(field.widget, forms.TextInput),
               isinstance(field.widget, forms.Textarea),
               isinstance(field.widget, forms.NumberInput) 
            ]):
                field.widget.attrs.setdefault('class', 'form-control')
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.setdefault('class', 'form-select')
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.setdefault('class', 'form-check-input')
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs.setdefault('class', 'form-file')
