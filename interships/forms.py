from django import forms
from .models import Intern, Role, RoleStatus

class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = '__all__'

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'

class RoleStatusForm(forms.ModelForm):
    class Meta:
        model = RoleStatus
        fields = '__all__'
