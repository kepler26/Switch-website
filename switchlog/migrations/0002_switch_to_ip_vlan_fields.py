from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switchlog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(model_name='logentry', name='ip'),
        migrations.RemoveField(model_name='logentry', name='interface'),
        migrations.AddField(
            model_name='logentry',
            name='ip_address',
            field=models.CharField(blank=True, default='No change', max_length=255),
        ),
        migrations.AddField(
            model_name='logentry',
            name='vlan_changes',
            field=models.CharField(blank=True, default='No change', max_length=255),
        ),
        migrations.RenameField(
            model_name='logentry',
            old_name='view',
            new_name='view_log',
        ),
        migrations.AlterField(
            model_name='logentry',
            name='hostname',
            field=models.CharField(blank=True, default='No change', max_length=255),
        ),
        migrations.AlterModelOptions(
            name='logentry',
            options={'ordering': ['-date', '-time']},
        ),
    ]
