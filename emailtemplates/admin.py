from django.contrib import admin
from emailtemplates.models import EmailTemplate


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'subject', 'visible_from_address')
    search_fields = ('name', 'slug', 'subject', 'from_address', 'body')
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'from_address', 'bcc')}),
        ('Email', {'fields': ('subject', 'body',)}),
        ('Advanced', {'classes': ('',), 'fields': ('base_template', 'txt_body')})
    )
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(EmailTemplate, EmailTemplateAdmin)
