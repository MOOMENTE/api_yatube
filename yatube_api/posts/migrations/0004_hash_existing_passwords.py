from django.contrib.auth.hashers import identify_hasher, make_password
from django.db import migrations


def hash_existing_passwords(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    for user in User.objects.all():
        password = user.password
        if not password:
            continue
        try:
            identify_hasher(password)
        except ValueError:
            user.password = make_password(password)
            user.save(update_fields=['password'])


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20250919_0934'),
    ]

    operations = [
        migrations.RunPython(hash_existing_passwords, noop),
    ]
