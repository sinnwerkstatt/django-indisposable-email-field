from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from indisposable_email_field.models import DisposableDomainName


errmsg = getattr(settings,
                 "DISPOSABLE_EMAIL_DOMAIN_ERROR_MESSAGE",
                 _("You cannot use a disposable email address to sign up")
                 )


def validate_indisposable_email_domain(value):
    domain_name = value.rsplit('@')[-1]
    if DisposableDomainName.objects.filter(domain_name).exists():
        raise ValidationError(errmsg)
