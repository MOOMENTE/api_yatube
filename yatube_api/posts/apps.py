from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

    def ready(self):
        # Import signals so raw passwords get hashed automatically.
        from . import signals  # noqa: F401
