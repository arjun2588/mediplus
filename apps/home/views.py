from urllib import response
from django.shortcuts import render
from django.urls import reverse_lazy
from apps.home.forms import ContactForm
from apps.home.utils import send_email

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def contact(request):
    if request.method == 'POST':
        forms = ContactForm(request.POST)
        if forms.is_valid():
            #forms.save()
            context = {
                'subject': forms.cleaned_data['subject'],
                'message': forms.cleaned_data['message'],
                'name': forms.cleaned_data['name'],
                'email': forms.cleaned_data['email'],
                'phone': forms.cleaned_data['phone']
                       }
            send_email(
                subject=forms.cleaned_data['subject'],
                template_name='contact_us_email.html',
                context=context,
                recipient_list=['xxxx@gmail.com']  
            )
            success_url = reverse_lazy('contact')
    else:
        forms = ContactForm()

    return render(request,'home/contact.html',{'forms':forms})


def appointment(request):
    # if(request.method == 'POST'):
    #     form = AppointmentForm(request.POST)
    #         if form.is_valid()
    #             form.save()
    #             success_url = 
    # else    
    #     form = AppointmentForm()

    return render(request,'home/appointment.html')