# Generated by Django 2.0.6 on 2018-12-15 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinstance',
            old_name='imprint',
            new_name='edition',
        ),
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('Mai', 'Maintenance'), ('Lo', 'On loan'), ('Av', 'Available'), ('Re', 'Reserved')], default='Mai', help_text='Book availability', max_length=3),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
