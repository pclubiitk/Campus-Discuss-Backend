"""
Django email-settings for campusdiscussbackend project.
"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'https://emailhost'
EMAIL_USE_TLS = True
EMAIL_PORT = 5432
EMAIL_HOST_USER = 'example@email.com'
EMAIL_HOST_PASSWORD = 'password'

ACTIVATION_SUBJECT = "Activation mail for Campus Discuss"
ACTIVATION_BODY = """Hi {name:s}! 
                     Click on the followiing link or copy-paste it to continue with the activation procedure.
                     {link:s}."""
ACTIVATION_REDIRECT = "https://redirectlink"
ACTIVATION_LINK = "https://campusdiscuss.in/verify?code={code:s}"
