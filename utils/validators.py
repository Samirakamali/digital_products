from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class PhoneNumberValidator(RegexValidator):
    regex = r'^98[0-9]{10}$'
    message = _('Phone number must be a VALID 12 digits like 98xxxxxxxxxx')
    code = 'invalid_phone_number'


class SKUValidator(RegexValidator):
    regex = r'^[a-zA-Z0-9]{6,20}$'
    message = _('SKU must be alphanumeric with 6 to 20 characters')
    code = 'invalid_sku'


class UsernameValidator(RegexValidator):
    regex = r'^[a-zA-Z][a-zA-Z0-9_]{1,}$'
    message = _('Enter a valid username starting with a-z. This value may contain only letters, numbers and underscore characters.')
    code = 'invalid_username'


class PostalCodeValidator(RegexValidator):
    regex = r'^[0-9]{10}$'
    message = _('Enter a valid postal code.')
    code = 'invalid_postal_code'


class IDNumberValidator(RegexValidator):
    regex = r'^[0-9]{10}$'
    message = _('Enter a valid id number.')
    code = 'invalid_id_number'


class IBANNumberValidator(RegexValidator):
    regex = r'^[a-zA-Z]{2}[0-9]{2}[0-9]{4}[0-9]{7}[a-zA-Z0-9]{1,16}$'
    message = _('Enter a valid IBAN number.')
    code = 'invalid_iban_number'


class BankCardNumberValidator(RegexValidator):
    regex = r'^[0-9]{16}$'
    message = _('Enter a valid card number.')
    code = 'invalid_bank_card_number'


# Instances for usage
validate_phone_number = PhoneNumberValidator()
validate_sku = SKUValidator()
validate_username = UsernameValidator()
validate_postal_code = PostalCodeValidator()
validate_id_number = IDNumberValidator()
validate_iban_number = IBANNumberValidator()
validate_bank_card_number = BankCardNumberValidator()