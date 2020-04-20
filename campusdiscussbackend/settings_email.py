"""
Django email-settings for campusdiscussbackend project.
"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mmtp.iitk.ac.in'
EMAIL_USE_TLS = True
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

ACTIVATION_SUBJECT = ["Activation mail for Campus Discuss","Password Reset Email For Campus Discuss"]
ACTIVATION_BODY = ["""Hi {name:s}! 
                     Click on the followiing link or copy-paste it to continue with the activation procedure.
                     {link:s}.""",
                    """Hi {name:s}! 
                     Click on the followiing link or copy-paste it to continue with the password reset procedure.
                     {link:s}."""
                     
                ]
ACTIVATION_REDIRECT = ["http://127.0.0.1:8000/","/"]
ACTIVATION_LINK = ["http://127.0.0.1:8000/users/verify/code={code:s}/","http://127.0.0.1:8000/users/resetpass/code={code:s}/"]
