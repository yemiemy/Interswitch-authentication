from django import forms

class CreateProjectForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'project title', 'class':'form-control field'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'project description', 'class':'form-control field'}))
	attachment = forms.FileField(required=False)
	# point = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'Town / City', 'class':'form-control'}))
	startdate = forms.CharField(widget=forms.DateTimeInput(attrs={'placeholder':'yyyy-mm-dd ', 'class':'form-control'}, format = 'yyyy-mm-dd'))
	deadline = forms.CharField(widget=forms.DateTimeInput(attrs={'placeholder':'yyyy-mm-dd ', 'class':'form-control'}))