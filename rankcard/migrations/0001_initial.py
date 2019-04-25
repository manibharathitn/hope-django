# Generated by Django 2.0.13 on 2019-04-13 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('mark', models.IntegerField()),
            ],
            options={
                'db_table': 'mark',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.AddField(
            model_name='mark',
            name='student',
            field=models.ForeignKey(db_column='student_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='rankcard.Student'),
        ),
    ]