from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='instancia',
            field=models.CharField(default='None', max_length=24),
        ),
    ]