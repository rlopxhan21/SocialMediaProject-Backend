# Generated by Django 4.1.6 on 2023-02-18 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_alter_comment_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['updated', 'created']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['updated', 'created']},
        ),
    ]
