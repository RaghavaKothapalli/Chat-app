import os

# ✅ MUST be before any Django imports
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# ✅ Setup Django immediately after setting environment
import django
django.setup()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
