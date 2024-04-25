from drf_auto_endpoint.endpoints import Endpoint
from drf_auto_endpoint.router import register
from django.contrib.auth import get_user_model
from .models import Product
from .views import UserViewSet


class DefaultEndpoint(Endpoint):
    """The default Endpoint"""

    include_str = False

    def get_url(self):
        """The core endpoint defaults to not include the application name in the apis url."""
        if hasattr(self, "url") and self.url is not None:
            return self.url

        return "{}".format(self.model_name.replace("_", "-"))


@register
class ProductEndpoint(DefaultEndpoint):
    model = Product


@register
class UserEndpoint(DefaultEndpoint):
    model = get_user_model()
    base_viewset = UserViewSet
