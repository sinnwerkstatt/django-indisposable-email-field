from django.core.validators import validate_email
from django.forms import EmailField

from indisposable_email_field.models import DisposableDomainName
from indisposable_email_field.validators import validate_indisposable_email_domain


# NOTE: This is done for reverse compatibility, in case anybody was importing
#       custom_email_validator from here
custom_email_validator = validate_indisposable_email_domain


class IndisposableEmailField(EmailField):
    default_validators = [validate_email, validate_indisposable_email_domain]
