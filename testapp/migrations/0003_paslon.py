# Generated by Django 3.1.1 on 2020-09-18 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20200918_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='paslon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomorurut', models.IntegerField()),
                ('isputra', models.BooleanField()),
                ('namaketua', models.TextField()),
                ('namawakil', models.TextField()),
                ('votecount', models.IntegerField()),
            ],
        ),
    ]
