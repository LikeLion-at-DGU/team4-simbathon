# Generated by Django 4.0.3 on 2022-06-30 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0010_remove_profile_grade_profile_year_in_school_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/'),
        ),
    ]
