from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import identify_hasher, make_password
from django.db.models.signals import pre_save
from django.dispatch import receiver

User = get_user_model()


@receiver(pre_save, sender=User)
def ensure_password_hashed(sender, instance, **kwargs):
    """Hash plain-text passwords set without using create_user."""
    password = instance.password
    if not password:
        return
    try:
        identify_hasher(password)
    except ValueError:
        instance.password = make_password(password)
