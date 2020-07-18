from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from campusdiscussbackend.settings import EXPO_SERVER
import requests

def push_notify(token, title, body):
    """
    API for sending a request to an Expo server.
    If you pass any one of the above as a list, make sure to pass all of them as lists.

    Please setup EXPO_SERVER in campusdiscussbackend.settings first.

    Args:
        token (list or string): Can be a list of tokens, or a single token.
        title (list or string): Can be a list of titles, or a single title. Will be applied serially tokenwise.
        body (list or string): Same as above.

    Returns:
        Json file containing response from server.
    """
    headers={'Content-Type':'application/json'}

    data=[]

    num=None
    if token is list:
        num=len(token)
    try:
        if num is not None:
            for i in range(num):
                data.append({
                    'to':'ExponentPushToken[{token}]'.format(token=token[i]),
                    'title':title[i],
                    'body':body[i],
                })
        else :
            data={
                'to':'ExponentPushToken[{token}]'.format(token=token),
                'title':title,
                'body':body,
            }
    except:
        return HttpResponse("One or more of the args do not have same datatypes.",status=403)
    
    r=requests.post(EXPO_SERVER, headers=headers, data=data)
    
    return r.json()

