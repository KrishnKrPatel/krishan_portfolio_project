from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class ContactMessage(models.Model):
    name = models.CharField(_('Name'), max_length=50)
    mobile_no = models.CharField(_('Mobile Number'), max_length=50)
    email = models.EmailField(_('Email'))
    subject = models.CharField(_('Subject'), max_length=255)
    message = models.TextField(_('Message'), null=True, blank=True)
    created_on = models.DateTimeField(_('Created On'), auto_now_add=True)

    def __str__(self):
        return f"{self.name} --- {self.email}"

    class Meta:
        db_table = "contactmessage"
        ordering = ['-created_on']
        verbose_name = _('Contact Message')
        verbose_name_plural = _('Contact Messages')
