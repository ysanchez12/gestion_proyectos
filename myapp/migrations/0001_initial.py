# Generated by Django 3.0.6 on 2020-05-23 15:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Unitario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('costo', models.FloatField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unitarios', to='myapp.Proyecto')),
            ],
        ),
    ]
