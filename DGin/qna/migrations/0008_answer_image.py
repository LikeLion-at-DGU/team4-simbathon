# Generated by Django 4.0.3 on 2022-06-25 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0007_alter_question_like_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='answer/'),
        ),
    ]
