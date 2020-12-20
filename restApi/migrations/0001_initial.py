from django.db import migrations
from restApi.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(self,apps, schema_editor):
        user = CustomUser(name="Abir", 
        email = "debabir91@gmail.com",
        is_staff = True,
        is_superuser = True,
        phone = "123456789",
        gender = "Male")

        user.set_password("123")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]