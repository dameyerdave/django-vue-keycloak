from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from urllib.parse import quote


class KeycloakAccountAdapter(DefaultAccountAdapter):

    def get_logout_redirect_url(self, request):
        """
        if allauth logout is called this function
        returns the redirect url after the logout. We can
        use this feature to provide the keycloak logout
        url. With it the keycloak session is also deleted.
        """
        if settings.KEYCLOAK_LOGOUT_ON_LOGOUT:
            redirect_uri = quote(
                f"{'https' if request.is_secure() else 'http' }://{request.get_host()}{settings.LOGOUT_REDIRECT_URL}",
                safe="",
            )
            return f"{settings.KEYCLOAK_SERVER_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/logout/?post_logout_redirect_uri={redirect_uri}&client_id={settings.KEYCLOAK_CLIENT_ID}"
        else:
            return super().get_logout_redirect_url(request)
