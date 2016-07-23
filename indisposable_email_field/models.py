from django.db import models
from django.utils.translation import ugettext_lazy as _


class DisposableDomainName(models.Model):
    value = models.CharField(
        help_text=_('Domain name that should be blacklisted'),
        max_length=255,
        unique=True,
        verbose_name=_('Domain Name'),
    )

    def __str__(self):
        return self.value

    def __unicode__(self):
        return self.value
