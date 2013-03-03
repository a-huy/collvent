import re
from django.core.exceptions import ValidationError
from django.utils.encoding import smart_text

phone_digits_re = re.compile(r'^(?:1-?)?(\d{3})[-\.]?(\d{3})[-\.]?(\d{4})$')

def validate_password(in_pass):
    if len(in_pass) < 6: raise ValidationError

def clean_us_phone_number(in_phone):
    value = re.sub('(\(|\)|\s+)', '', smart_text(in_phone))
    matches = phone_digits_re.search(value)
    if not matches: raise ValidationError
    return value

def update_user(user, email, phone, password, first_name, last_name):
    if email: user.email = email
    if phone: user.phone = phone
    user.set_password(password)
    if first_name: user.first_name = first_name
    if last_name: user.last_name = last_name
    user.save()
