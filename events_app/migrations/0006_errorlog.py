# Generated by Django 2.2.3 on 2019-07-26 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0005_auto_20190726_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.CharField(max_length=1000)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events_app.Event')),
            ],
        ),
    ]