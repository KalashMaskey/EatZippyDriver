from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize = value.size

    if filesize > 1048576:
        raise ValidationError("The max file size is 1mb")
    else:
        return value
