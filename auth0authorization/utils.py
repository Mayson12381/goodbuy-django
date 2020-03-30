import json
import requests
import jwt
from django.contrib.auth import authenticate


def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')
    authenticate(remote_user=username)
    return username


def jwt_decode_token(token):
    print(f'\nToken: {token}\n')
    header = jwt.get_unverified_header(token)

    print('test1.1')
    jwks = requests.get(
        'https://{}/.well-known/jwks.json'.format('goodbuy.eu.auth0.com')).json()
    public_key = None
    print('test2')
    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    print('test3')

    if public_key is None:
        raise Exception('Public key not found.')

    print('test4')

    issuer = 'https://{}/'.format('goodbuy.eu.auth0.com')
    return jwt.decode(token, public_key, audience='https://goodbuy-api', issuer=issuer, algorithms=['RS256'])
