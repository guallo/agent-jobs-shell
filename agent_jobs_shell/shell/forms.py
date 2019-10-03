from django import forms


class JobForm(forms.Form):
    uuid = forms.UUIDField(required=False)
    cmd = forms.CharField()
    directory = forms.CharField(max_length=128, required=False)
    user = forms.CharField(max_length=32, required=False)
    payload = forms.FileField(required=False)
    extra_env_json = forms.CharField(required=False)
