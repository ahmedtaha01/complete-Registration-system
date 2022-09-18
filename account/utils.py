from account.models import User
from django.http import HttpResponse ,request , Http404
from django.contrib.auth.hashers import make_password
from django.core.files.base import ContentFile
from urllib.error import HTTPError



def save_profile(backend, strategy, details, response,
        user=None,is_new=False, *args, **kwargs):
    url = None
    if backend.name == 'facebook':
        # url = "https://graph.facebook.com/%s/picture?type=large"%response['id']
        # url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        url='https://graph.facebook.com/{0}/picture/?type=large&access_token={1}'.format(response['id'],
                                                                                              response[
                                                                                                  'access_token'])
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal','')
    if backend.name == 'google-oauth2':
        url = response['image'].get('url')
        ext = url.split('.')[-1]
    if url:
        if is_new:    #first time
            user.get_image_from_url(url)
            user.save_url(response['link'])
            user.save()


# def change_activity(strategy, user, response, is_new=False,*args,**kwargs):
    