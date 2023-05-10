# Generated by Django 4.1.6 on 2023-04-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visionapp', '0006_alter_answer_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('choice1', models.CharField(max_length=100)),
                ('choice2', models.CharField(max_length=100)),
                ('choice3', models.CharField(max_length=100)),
                ('correct_answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
