<<<<<<< HEAD
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

def get_name(request):

    if request.method=='POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['yasir.choudhary@fafadiatech.com']

            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)

            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'formTwo/sendMail.html', {'form':form})


=======
from django.shortcuts import render

# Create your views here.
>>>>>>> bb980a8d69038e69ac8eb1831811fe1bb3ecae27
