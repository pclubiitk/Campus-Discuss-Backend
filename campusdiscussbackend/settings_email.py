"""
Django email-settings for campusdiscussbackend project.
Contains all the settings for different email types
"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'HOST.COM'
EMAIL_USE_TLS = True
EMAIL_PORT = 5432
EMAIL_HOST_USER = 'EMAIL'
EMAIL_HOST_PASSWORD = 'PASSWORD'

"""
This is a prototype of a class for sending email, for example - Activation.
It has three variables - 
EMAIL_SUBJECT: The subject of the email.
EMAIL_BODY: The body of the email.
REDIRECT_URL: Url it redirects to after sending the email.
"""
class ExampleEmail():
    EMAIL_SUBJECT = 'SUBJECT'
    EMAIL_BODY = 'BODY'
    REDIRECT_URL = 'URL'

