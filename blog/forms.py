from django import forms
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

from blog.models import Comment


class CommentForm(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        #self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(Submit('submit', 'Save', css_class='btn-primary'))

    class Meta:
        model = Comment
        fields = ["content"]