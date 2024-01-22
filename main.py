import flet as ft
from flet_route import Routing
from routes import app_routes
from middlewares.app_middleware import AppBasedMiddleware
import sys
import certifi
import os

os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()
os.environ["SSL_CERT_FILE"] = certifi.where()


if os.getenv("FLET_PLATFORM") == "android":
    import ssl

    def create_default_context(
        purpose=ssl.Purpose.SERVER_AUTH, *, cafile=None, capath=None, cadata=None
    ):
        return ssl.create_default_context(
            purpose=purpose, cafile=certifi.where(), capath=capath, cadata=cadata
        )

    ssl._create_default_https_context = create_default_context
    