
def send_email_template(slug, to_addresses, context={}, attachments=None, headers=None, **kwargs):
    from emailtemplates.models import EmailTemplate
    email_template = EmailTemplate.objects.get(slug=slug)
    return email_template.send(to_addresses, context, attachments, headers, **kwargs)
