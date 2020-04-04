'''
DRF BUILT IN EXCEPTIONS
https://stackoverflow.com/a/30628065/2897115

The Django REST framework provides several built in exceptions, which are mostly subclasses of DRF's APIException.
You can raise exceptions in your view like you normally would in Python:

Example:
from rest_framework.exceptions import APIException

def my_view(request):
    raise APIException("There was a problem!")

You could also create your own custom exception by inheriting from APIException and setting status_code and default_detail. Some of the built in ones are: ParseError, AuthenticationFailed, NotAuthenticated, PermissionDenied, NotFound, NotAcceptable, ValidationError, etc.

These will then get converted to a Response by the REST Framework's exception handler. Each exception is associated with a status code that is added to the Response. By default the exception handler is set to the built in handler:

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'
}

Exceptions:

https://stackoverflow.com/questions/38847441/django-exception-handling-best-practice-and-sending-customized-error-message

    Usually 4xx errors (Errors that are attributed to the client-side) are disclosed so the user may correct the request.

    On the other side, 5xx errors (Errors that are attributed to the server-side) are usually only presented without information. In my opinion for those you should use tools like Sentry do monitor and resolve this errors, that may have security issues embedded in them.


'''
##########################################
'''
GETIING USER FROM USERNAME
/home/web_dev/btgapp_from_server/btgapp_project_updated/venv_btg/lib/python3.6/site-packages/django/contrib/auth/base_user.py

User get user object based on a username (it can be email, some name etc)

class BaseUserManager(models.Manager):

...

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})

Usage:
User = get_user_model()
username = jwt_get_username_from_payload(payload)
user = User.objects.get_by_natural_key(username)

'''
#########################################
'''
PROCEDURE FOR GETTING USER FROM JWT TOKEN 
1) Get Authorizatio header
-- request.META.get('HTTP_AUTHORIZATION')
-- function: from rest_framework.authentication import get_authorization_header
2) Check for JWT_AUTH_HEADER_PREFIX in the header
-- function: get_jwt_value (class: JSONWebTokenAuthentication)
-- from rest_framework_jwt.settings import api_settings
-- api_settings.JWT_AUTH_HEADER_PREFIX
3) Get the Token
-- function: get_jwt_value (class: JSONWebTokenAuthentication)
4) Get the payload from token
-- function: authenticate (class: BaseJSONWebTokenAuthentication)
-- jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
-- payload = jwt_decode_handler(jwt_value)
5) get the user_model
-- function: authenticate_credentials (class: BaseJSONWebTokenAuthentication)
-- from django.contrib.auth import get_user_model
6) get the username from payload
-- function: authenticate_credentials (class: BaseJSONWebTokenAuthentication)
-- jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER
-- jwt_get_username_from_payload(payload)
7) get the user object using username (it can be email or username etc)
-- function: authenticate_credentials (class: BaseJSONWebTokenAuthentication)
-- User.objects.get_by_natural_key(username)
'''
##############################################################
'''
JWT_AUTH in settings.py

/home/web_dev/btgapp_from_server/btgapp_project_updated/venv_btg/lib/python3.6/site-packages/rest_framework_jwt/settings.py

Additional Settings
There are some additional settings that you can override similar to how you'd do it with Django REST framework itself. Here are all the available defaults.

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': settings.SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,

    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,

}

This packages uses the JSON Web Token Python implementation, PyJWT and allows to modify some of it's available options.
'''
############################################################
'''
Example of jwt

>>import jwt
>>key = 'secret'
>>encoded = jwt.encode({'some': 'payload'}, key, algorithm='HS256')
'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg'
>>decoded = jwt.decode(encoded, key, algorithms='HS256')
{'some': 'payload'}


###

The JWT specification defines some registered claim names and defines how they should be used. PyJWT supports these registered claim names:

“exp” (Expiration Time) Claim
“nbf” (Not Before Time) Claim
“iss” (Issuer) Claim
“aud” (Audience) Claim
“iat” (Issued At) Claim

1) Exp:

    jwt.encode({'exp': 1371720939}, 'secret')
    jwt.encode({'exp': datetime.utcnow()}, 'secret')

    Expiration time is automatically verified in jwt.decode() and raises jwt.ExpiredSignatureError if the expiration time is in the past:

    try:
        jwt.decode('JWT_STRING', 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        # Signature has expired

    You can turn off expiration time verification with the verify_exp parameter in the options argument.

    -- Leeway 

        PyJWT also supports the leeway part of the expiration time definition, which means you can validate a expiration time which is in the past but not very far. For example, if you have a JWT payload with a expiration time set to 30 seconds after creation but you know that sometimes you will process it after 30 seconds, you can set a leeway of 10 seconds in order to have some margin:

        jwt_payload = jwt.encode({
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=30)
        }, 'secret')

        time.sleep(32)

        # JWT payload is now expired
        # But with some leeway, it will still validate
        jwt.decode(jwt_payload, 'secret', leeway=10, algorithms=['HS256'])
        Instead of specifying the leeway as a number of seconds, a datetime.timedelta instance can be used. The last line in the example above is equivalent to:

        jwt.decode(jwt_payload, 'secret', leeway=datetime.timedelta(seconds=10), algorithms=['HS256'])

2) Issued At Claim (iat):

    jwt.encode({'iat': 1371720939}, 'secret')
    jwt.encode({'iat': datetime.utcnow()}, 'secret')
'''














#############################################
# PURPOSE: GET THE HTTP_AUTHORIZATION header and convert it to bytes if its not
#/home/web_dev/btgapp_from_server/btgapp_project_updated/venv_btg/lib/python3.6/site-packages/rest_framework/authentication.py

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = 'iso-8859-1'

def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.

    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, str):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


#############################################
#PURPOSE: get the jwt token from the HTTP_AUTHORIZATION header
#/home/web_dev/btgapp_from_server/btgapp_project_updated/venv_btg/lib/python3.6/site-packages/rest_framework_jwt/authentication.py
from rest_framework_jwt.settings import api_settings
from django.utils.encoding import smart_text
from rest_framework.authentication import get_authorization_header
from rest_framework import exceptions
from django.utils.translation import ugettext as _

def get_jwt_value(request):
    auth = get_authorization_header(request).split()
    auth_header_prefix = api_settings.JWT_AUTH_HEADER_PREFIX.lower()

    # checks if token is provided through a cookie when there is no HTTP_AUTHORIZATION header found
    if not auth:
        if api_settings.JWT_AUTH_COOKIE:
            return request.COOKIES.get(api_settings.JWT_AUTH_COOKIE)
        return None

    # Checks whether First word matches the JWT_AUTH_HEADER_PREFIX
    if smart_text(auth[0].lower()) != auth_header_prefix:
        return None

    # Checks if only JWT_AUTH_HEADER_PREFIX is provided without any token
    if len(auth) == 1:
        msg = _('Invalid Authorization header. No credentials provided.')
        # DRF provides built in exceptions. These will then get converted to a Response by the REST Framework's exception handler. more info above
        raise exceptions.AuthenticationFailed(msg)

    # Checks if anything more than JWT_AUTH_HEADER_PREFIX and token is provided
    elif len(auth) > 2:
        msg = _('Invalid Authorization header. Credentials string '
                'should not contain spaces.')
        raise exceptions.AuthenticationFailed(msg)

    return auth[1]



###################################################################
#PURPOSE:  Returns a two-tuple of `User` and token if a valid signature has been supplied using JWT-based authentication.  Otherwise returns `None`.
#get_jwt_value (from the file)
from rest_framework_jwt.settings import api_settings
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
#authenticate_credentials (from the same file)

def authenticate(request):
    """
    Returns a two-tuple of `User` and token if a valid signature has been
    supplied using JWT-based authentication.  Otherwise returns `None`.
    """
    jwt_value = get_jwt_value(request)
    if jwt_value is None:
        return None

    try:
        payload = jwt_decode_handler(jwt_value)
    except jwt.ExpiredSignature:
        msg = _('Signature has expired.')
        raise exceptions.AuthenticationFailed(msg)
    except jwt.DecodeError:
        msg = _('Error decoding signature.')
        raise exceptions.AuthenticationFailed(msg)
    except jwt.InvalidTokenError:
        raise exceptions.AuthenticationFailed()

    user = self.authenticate_credentials(payload)

    return (user, jwt_value)


#######################################################################
from django.contrib.auth import get_user_model
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

def authenticate_credentials(self, payload):
    """
    Returns an active user that matches the payload's user id and email.
    """
    User = get_user_model()
    username = jwt_get_username_from_payload(payload)

    if not username:
        msg = _('Invalid payload.')
        raise exceptions.AuthenticationFailed(msg)

    try:
        user = User.objects.get_by_natural_key(username)
    except User.DoesNotExist:
        msg = _('Invalid signature.')
        raise exceptions.AuthenticationFailed(msg)

    if not user.is_active:
        msg = _('User account is disabled.')
        raise exceptions.AuthenticationFailed(msg)

    return user


#####################################################
# Get payload from jwt_token
# jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

def jwt_decode_handler(token):
    options = {
        'verify_exp': api_settings.JWT_VERIFY_EXPIRATION,
    }
    # get user from token, BEFORE verification, to get user secret key
    unverified_payload = jwt.decode(token, None, False)
    secret_key = jwt_get_secret_key(unverified_payload)
    return jwt.decode(
        token,
        api_settings.JWT_PUBLIC_KEY or secret_key,
        api_settings.JWT_VERIFY,
        options=options,
        leeway=api_settings.JWT_LEEWAY,
        audience=api_settings.JWT_AUDIENCE,
        issuer=api_settings.JWT_ISSUER,
        algorithms=[api_settings.JWT_ALGORITHM]
    )


####################################################
# Gwt jwt_get_secret_key based on per user
# from django.contrib.auth import get_user_model
# Here JWT_GET_USER_SECRET_KEY defines the function from which we have to get the key using user. It can be defined by the user

def jwt_get_secret_key(payload=None):
    """
    For enhanced security you may want to use a secret key based on user.

    This way you have an option to logout only this user if:
        - token is compromised
        - password is changed
        - etc.
    """
    if api_settings.JWT_GET_USER_SECRET_KEY:
        User = get_user_model()  # noqa: N806
        user = User.objects.get(pk=payload.get('user_id'))
        key = str(api_settings.JWT_GET_USER_SECRET_KEY(user))
        return key
    return api_settings.JWT_SECRET_KEY


#THE BELOW FUNCTIONS CAN BE CUSTOMIZED

#################################################

def jwt_payload_handler(user):
    username_field = get_username_field()
    username = get_username(user)

    warnings.warn(
        'The following fields will be removed in the future: '
        '`email` and `user_id`. ',
        DeprecationWarning
    )

    payload = {
        'user_id': user.pk,
        'username': username,
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }
    if hasattr(user, 'email'):
        payload['email'] = user.email
    if isinstance(user.pk, uuid.UUID):
        payload['user_id'] = str(user.pk)

    payload[username_field] = username

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload


##################################################
## Create a jwt using payload
def jwt_encode_handler(payload):
    key = api_settings.JWT_PRIVATE_KEY or jwt_get_secret_key(payload)
    return jwt.encode(
        payload,
        key,
        api_settings.JWT_ALGORITHM
    ).decode('utf-8')




########################################
# Used in jwt_payload_handler

def get_username_field():
    try:
        username_field = get_user_model().USERNAME_FIELD
    except:
        username_field = 'username'

    return username_field


def get_username(user):
    try:
        username = user.get_username()
    except AttributeError:
        username = user.username

    return username