import json
import sys

import tinder_api as ti
from facebook_utils import query_profile_with_graph_api
from tinder_token import get_access_token

if __name__ == '__main__':

    credentials = json.load(open('credentials.json', 'r'))
    fb_id = credentials['FB_ID']
    fb_auth_token = get_access_token(credentials['FB_EMAIL_ADDRESS'], credentials['FB_PASSWORD'])
    token = ti.auth_token(fb_auth_token, fb_id)

    print('Which of your friends are on Tinder?')
    print('----------')
    print('FB_ID = {}'.format(fb_id))
    print('FB_AUTH_TOKEN = {}'.format(fb_auth_token))
    print('TINDER_TOKEN = {}'.format(token))
    print('----------')

    if not token:
        print('could not get Tinder token. Program will exit.')
        sys.exit(0)

    print('Successfully connected to Tinder servers.')
    my_profile = ti.profile(token)


    def get(profile_obj, field_name):
        try:
            return profile[field_name]
        except:
            return 'N/A'


    print('-' * 100)
    pattern = '%20s  %20s  %10s  %50s'
    print(pattern % ('First Name', 'Last Name', 'Gender', 'URL'))

    for friend in my_profile['friends']:
        profile = query_profile_with_graph_api(profile_id=friend, access_token=fb_auth_token)
        request = 'https://www.facebook.com/{}'.format(friend)

        print(pattern % (get(profile, 'first_name'),
                         get(profile, 'last_name'),
                         get(profile, 'gender'),
                         request))
    print('-' * 100)
