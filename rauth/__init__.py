'''
    rauth
    -----

    OAuth 1.0/a, 2.0, and Ofly wrapped around Python Requests. Basic usage:

        >>> import rauth
        >>> service = rauth.OAuth2Service(client_id='foo', client_secret='bar')
        >>> authorize_url = service.get_authorize_url()

        ...

        >>> session = service.get_auth_session(...)
        >>> r = session.get('resource')
        >>> print r.json

'''

__all__ = ['OAuth1Service', 'OAuth2Service', 'OflyService', 'OAuth1Session',
           'OAuth2Session', 'OflySession']

from rauth.__about__ import (__title__, __version_info__, __version__, __author__,
                             __license__, __copyright__)

# HACK: setup workaround for the need to have Requests at runtime
try:
    from .service import OAuth1Service, OAuth2Service, OflyService
    from .session import OAuth1Session, OAuth2Session, OflySession

    # placate pyflakes
    (OAuth1Service, OAuth2Service, OflyService, OAuth1Session, OAuth2Session,
     OflySession)
except ImportError:  # pragma: no cover
    pass
