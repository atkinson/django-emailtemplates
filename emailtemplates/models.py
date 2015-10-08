import logging

from django.template import Template, Context, loader, TemplateDoesNotExist
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.template.defaultfilters import striptags

from autoslug import AutoSlugField

logger = logging.getLogger(__name__)


class EmailTemplate(models.Model):
    name = models.CharField(max_length=1024)
    slug = AutoSlugField(max_length=255, populate_from='name', unique=True, blank=True, editable=True)
    base_template = models.CharField(max_length=1024, blank=True, help_text="If present, the name of a django template.<br/> The body field will be present as the 'email_body' context variable")
    subject = models.CharField(max_length=1024)
    from_address = models.CharField(max_length=1024, blank=True, null=True, help_text="Specify as: 'Full Name &lt;email@address>'<br/>Defaults to: 'no-reply@site.domain'")
    body = models.TextField(default='')
    txt_body = models.TextField(blank=True, null=True, help_text="If present, use as the plain-text body")

    def natural_key(self):
        return [self.slug]

    def __unicode__(self):
        return self.name

    def publish(self):
        super(EmailTemplate, self).publish()
        self.publish_by('slug')

    def render(self, context):
        if self.base_template:
            try:
                t = loader.get_template(self.base_template)
                context.update({'email_body': self._render_from_string(self.body, context)})
                return t.render(Context(context))
            except TemplateDoesNotExist as e:
                pass
        return self._render_from_string(self.body, context)

    def render_txt(self, context):
        if self.txt_body:
            return self._render_from_string(self.txt_body, context)

    def visible_from_address(self):
        if self.from_address:
            return self.from_address
        default_settings_email = getattr(settings, 'EMAILTEMPLATES_DEFAULT_FROM_EMAIL', None)
        if default_settings_email:
            return default_settings_email
        site = Site.objects.get_current()
        if site.name:
            return '%s <no-reply@%s>' % (site.name, site.domain)
        else:
            return 'no-reply@%s' % site.domain

    def send(self, to_addresses, context={}, attachments=None, headers=None):
        html_body = self.render(context)
        text_body = self.render_txt(context) or striptags(html_body)
        try:
            from inlinestyler.utils import inline_css
            html_body = inline_css(html_body)
        except ImportError:
            logger.info('pip install instyler to render CSS inline in emails')

        subject = self._render_from_string(self.subject, context)
        if isinstance(to_addresses, (str,unicode)):
            to_addresses = (to_addresses,)

        whitelisted_email_addresses = getattr(settings, 'EMAILTEMPLATES_DEBUG_WHITELIST', [])
        if getattr(settings, 'EMAILTEMPLATES_DEBUG', False):
            # clean non-whitelisted emails from the to_address
            cleaned_to_addresses = []
            for address in to_addresses:
                try:
                    email_domain = address.split('@')[1]
                except IndexError:
                    email_domain = None
                if email_domain in whitelisted_email_addresses or address in whitelisted_email_addresses:
                    cleaned_to_addresses.append(address)
            to_addresses = cleaned_to_addresses

        msg = EmailMultiAlternatives(subject, text_body, self.visible_from_address(), to_addresses, headers=headers)
        msg.attach_alternative(html_body, "text/html")

        if attachments is not None:
            for attach in attachments:
                msg.attach(*attach)
        return msg.send()

    def _render_from_string(self, s, context):
        t = Template(s)
        return t.render(Context(context)).encode('utf-8', 'ignore')

    @staticmethod
    def send_template(slug, to_address, context={}, attachments=None, headers=None):
        from emailtemplates.utils import send_email_template
        return send_email_template(slug, to_address, context=context, attachments=attachments, headers=headers)

