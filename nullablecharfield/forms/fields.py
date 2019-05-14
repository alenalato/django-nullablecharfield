from django.forms.fields import CharField
from nullablecharfield.widgets import NullableTextWidget

class CharNullField(CharField):
    widget = NullableTextWidget
    description = "CharField that stores NULL"

    def __init__(self, *args, **kwargs):
        if 'null' in kwargs:
            self.null = kwargs['null']
            del kwargs['null']
        super(CharNullField, self).__init__(*args, **kwargs)
        self.widget.isnull = self.null

    def to_python(self, value):
        if value is None:
            return None
        return super(CharNullField, self).to_python(value)
