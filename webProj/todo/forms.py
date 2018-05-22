from django import forms

class TaskForm(forms.Form):
    task_text = forms.CharField(max_length=250)
    due_date = forms.DateField()

