from django.db import models
from django.utils.translation import ugettext_lazy as _

class DisposableDomainName(models.Model):
    value = models.CharField(unique=True, max_length=500,
        verbose_name=_('Domain Name'),
        help_text=_('Domain name that should be blacklisted')
    )

    def __unicode__(self):
        return self.value