from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email(subject, template_name, context, recipient_list):
    # Adjust the path to the template
    template_path = f'home/emails/{template_name}'
    
    html_message = render_to_string(template_path, context)
    plain_message = strip_tags(html_message)
    
    email = EmailMessage(
        subject=subject,
        body=plain_message,
        from_email='xxxxxx@gmail.com',
        to=recipient_list,
    )
    email.content_subtype = 'html'  # Send as HTML
    email.send()
