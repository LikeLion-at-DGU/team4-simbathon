# Generated by Django 4.0.3 on 2022-06-29 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0008_answer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_school', models.CharField(choices=[('1학년', '1학년'), ('2학년', '2학년'), ('3학년', '3학년'), ('4학년', '4학년'), ('대학원생', '대학원생'), ('졸업생', '졸업생')], default='1학년', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AddField(
            model_name='profile',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='qna.grade'),
        ),
    ]
