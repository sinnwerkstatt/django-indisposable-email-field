from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.forms import EmailField
from django.utils.translation import ugettext_lazy as _

from indisposable_email_field.models import DisposableDomainName


def custom_email_validator(value):
    domainname = value.rsplit('@')[-1]
    domain = DisposableDomainName.objects.filter(value=domainname)
    if domain:
        raise ValidationError(_('This domain name is not valid'))


class IndisposableEmailField(EmailField):
    default_validators = [validate_email, custom_email_validator]
