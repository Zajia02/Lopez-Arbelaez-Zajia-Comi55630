# Generated by Django 4.2.3 on 2023-08-31 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chaparreras',
            options={'verbose_name': 'Chaparreras', 'verbose_name_plural': 'Chaparreras'},
        ),
        migrations.AlterModelOptions(
            name='guantes',
            options={'verbose_name': 'Guantes', 'verbose_name_plural': 'Guantes'},
        ),
        migrations.AlterModelOptions(
            name='pantalon',
            options={'verbose_name': 'Pantalon', 'verbose_name_plural': 'Pantalones'},
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
