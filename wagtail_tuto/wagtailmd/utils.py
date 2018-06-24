from django.db.models import TextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

class MarkDownField(TextField):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MarkDownPanel(FieldPanel):
    def __init__(self, field_name, classname='', widget=None):
        super().__init__(field_name, classname, None)

        if self.classname != "":
            self.classname += " "
        self.classname += 'markdown' 
