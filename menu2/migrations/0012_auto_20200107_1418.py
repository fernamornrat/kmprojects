# Generated by Django 2.2.6 on 2020-01-07 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu2', '0011_auto_20200107_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiment',
            name='equipment',
        ),
        migrations.AddField(
            model_name='experiment',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experiment',
            name='ppe_type',
            field=models.CharField(choices=[('อุปกรณ์ป้องกันศีรษะ', 'อุปกรณ์ป้องกันศีรษะ'), ('อุปกรณ์ป้องกันใบหน้าและตา', 'อุปกรณ์ป้องกันใบหน้าและตา'), ('อุปกรณ์ป้องกันหู', 'อุปกรณ์ป้องกันหู'), ('อุปกรณ์ป้องกันการหายใจ', 'อุปกรณ์ป้องกันการหายใจ'), ('อุปกรณ์ป้องกันลำตัว', 'อุปกรณ์ป้องกันลำตัว'), ('อุปกรณ์ป้องกันมือ', 'อุปกรณ์ป้องกันมือ'), ('อุปกรณ์ป้องกันเท้า', 'อุปกรณ์ป้องกันเท้า')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
