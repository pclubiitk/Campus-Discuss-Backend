"""
Django email-settings for campusdiscussbackend project.
"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mmtp.iitk.ac.in'
EMAIL_USE_TLS = True
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

EMAIL_SUBJECT = {
        "Activation": "Activation mail for Campus Discuss",
        "PasswordReset": "Password Reset Email For Campus Discuss",
}
EMAIL_BODY = {
        "Activation": """Hi {name:s}! 
                     Click on the followiing link or copy-paste it to continue with the activation procedure.
                     {link:s}.""",
        "PasswordReset": """Hi {name:s}! 
                     Click on the followiing link or copy-paste it to continue with the password reset procedure.
                     {link:s}.""",
}
REDIRECT_LINK = {
        "Activation": "http://127.0.0.1:8000/",
        "PasswordReset": "/",
}
EMAIL_LINK = {
        "Activation":"http://127.0.0.1:8000/users/verify/code={code:s}/",
        "PasswordReset": "http://127.0.0.1:8000/users/resetpass/code={code:s}/",
}
