# Generated by Django 2.2.6 on 2020-01-07 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu2', '0010_experiment_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='course',
            field=models.CharField(choices=[('ฟิสิกส์', 'ฟิสิกส์'), ('เคมี', 'เคมี'), ('ชีววิทยา', 'ชีววิทยา'), ('โครงงานวิทยาศาสตร์', 'โครงงานวิทยาศาสตร์')], max_length=50),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='degree',
            field=models.CharField(choices=[('มัธยมศึกษาตอนต้น', 'มัธยมศึกษาตอนต้น'), ('มัธยมศึกษาตอนปลาย', 'มัธยมศึกษาตอนปลาย')], max_length=50),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='ghs_name_1',
            field=models.CharField(choices=[('สารไวไฟ', 'สารไวไฟ'), ('สารออกซิไดซ์', 'สารออกซิไดซ์'), ('วัตถุระเบิด', 'วัตถุระเบิด'), ('ก๊าซบรรจุภายใต้ความดัน', 'ก๊าซบรรจุภายใต้ความดัน'), ('สารกัดกร่อน', 'สารกัดกร่อน'), ('พิษเฉียบพลัน', 'พิษเฉียบพลัน'), ('อันตรายต่อสุขภาพ', 'อันตรายต่อสุขภาพ'), ('ระวัง', 'ระวัง'), ('อันตรายต่อิ่งแวดล้อม', 'อันตรายต่อิ่งแวดล้อม')], max_length=50),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='ghs_name_2',
            field=models.CharField(blank=True, choices=[('สารไวไฟ', 'สารไวไฟ'), ('สารออกซิไดซ์', 'สารออกซิไดซ์'), ('วัตถุระเบิด', 'วัตถุระเบิด'), ('ก๊าซบรรจุภายใต้ความดัน', 'ก๊าซบรรจุภายใต้ความดัน'), ('สารกัดกร่อน', 'สารกัดกร่อน'), ('พิษเฉียบพลัน', 'พิษเฉียบพลัน'), ('อันตรายต่อสุขภาพ', 'อันตรายต่อสุขภาพ'), ('ระวัง', 'ระวัง'), ('อันตรายต่อิ่งแวดล้อม', 'อันตรายต่อิ่งแวดล้อม')], max_length=50),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='ghs_name_3',
            field=models.CharField(blank=True, choices=[('สารไวไฟ', 'สารไวไฟ'), ('สารออกซิไดซ์', 'สารออกซิไดซ์'), ('วัตถุระเบิด', 'วัตถุระเบิด'), ('ก๊าซบรรจุภายใต้ความดัน', 'ก๊าซบรรจุภายใต้ความดัน'), ('สารกัดกร่อน', 'สารกัดกร่อน'), ('พิษเฉียบพลัน', 'พิษเฉียบพลัน'), ('อันตรายต่อสุขภาพ', 'อันตรายต่อสุขภาพ'), ('ระวัง', 'ระวัง'), ('อันตรายต่อิ่งแวดล้อม', 'อันตรายต่อิ่งแวดล้อม')], max_length=50),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='ghs_name_4',
            field=models.CharField(blank=True, choices=[('สารไวไฟ', 'สารไวไฟ'), ('สารออกซิไดซ์', 'สารออกซิไดซ์'), ('วัตถุระเบิด', 'วัตถุระเบิด'), ('ก๊าซบรรจุภายใต้ความดัน', 'ก๊าซบรรจุภายใต้ความดัน'), ('สารกัดกร่อน', 'สารกัดกร่อน'), ('พิษเฉียบพลัน', 'พิษเฉียบพลัน'), ('อันตรายต่อสุขภาพ', 'อันตรายต่อสุขภาพ'), ('ระวัง', 'ระวัง'), ('อันตรายต่อิ่งแวดล้อม', 'อันตรายต่อิ่งแวดล้อม')], max_length=50),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='ghs_name_5',
            field=models.CharField(blank=True, choices=[('สารไวไฟ', 'สารไวไฟ'), ('สารออกซิไดซ์', 'สารออกซิไดซ์'), ('วัตถุระเบิด', 'วัตถุระเบิด'), ('ก๊าซบรรจุภายใต้ความดัน', 'ก๊าซบรรจุภายใต้ความดัน'), ('สารกัดกร่อน', 'สารกัดกร่อน'), ('พิษเฉียบพลัน', 'พิษเฉียบพลัน'), ('อันตรายต่อสุขภาพ', 'อันตรายต่อสุขภาพ'), ('ระวัง', 'ระวัง'), ('อันตรายต่อิ่งแวดล้อม', 'อันตรายต่อิ่งแวดล้อม')], max_length=50),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='ghs_name_6',
            field=models.CharField(blank=True, choices=[('สารไวไฟ', 'สารไวไฟ'), ('สารออกซิไดซ์', 'สารออกซิไดซ์'), ('วัตถุระเบิด', 'วัตถุระเบิด'), ('ก๊าซบรรจุภายใต้ความดัน', 'ก๊าซบรรจุภายใต้ความดัน'), ('สารกัดกร่อน', 'สารกัดกร่อน'), ('พิษเฉียบพลัน', 'พิษเฉียบพลัน'), ('อันตรายต่อสุขภาพ', 'อันตรายต่อสุขภาพ'), ('ระวัง', 'ระวัง'), ('อันตรายต่อิ่งแวดล้อม', 'อันตรายต่อิ่งแวดล้อม')], max_length=50),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='ghs_name_7',
            field=models.CharField(blank=True, choices=[('สารไวไฟ', 'สารไวไฟ'), ('สารออกซิไดซ์', 'สารออกซิไดซ์'), ('วัตถุระเบิด', 'วัตถุระเบิด'), ('ก๊าซบรรจุภายใต้ความดัน', 'ก๊าซบรรจุภายใต้ความดัน'), ('สารกัดกร่อน', 'สารกัดกร่อน'), ('พิษเฉียบพลัน', 'พิษเฉียบพลัน'), ('อันตรายต่อสุขภาพ', 'อันตรายต่อสุขภาพ'), ('ระวัง', 'ระวัง'), ('อันตรายต่อิ่งแวดล้อม', 'อันตรายต่อิ่งแวดล้อม')], max_length=50),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='ghs_name_8',
            field=models.CharField(blank=True, choices=[('สารไวไฟ', 'สารไวไฟ'), ('สารออกซิไดซ์', 'สารออกซิไดซ์'), ('วัตถุระเบิด', 'วัตถุระเบิด'), ('ก๊าซบรรจุภายใต้ความดัน', 'ก๊าซบรรจุภายใต้ความดัน'), ('สารกัดกร่อน', 'สารกัดกร่อน'), ('พิษเฉียบพลัน', 'พิษเฉียบพลัน'), ('อันตรายต่อสุขภาพ', 'อันตรายต่อสุขภาพ'), ('ระวัง', 'ระวัง'), ('อันตรายต่อิ่งแวดล้อม', 'อันตรายต่อิ่งแวดล้อม')], max_length=50),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='ghs_name_9',
            field=models.CharField(blank=True, choices=[('สารไวไฟ', 'สารไวไฟ'), ('สารออกซิไดซ์', 'สารออกซิไดซ์'), ('วัตถุระเบิด', 'วัตถุระเบิด'), ('ก๊าซบรรจุภายใต้ความดัน', 'ก๊าซบรรจุภายใต้ความดัน'), ('สารกัดกร่อน', 'สารกัดกร่อน'), ('พิษเฉียบพลัน', 'พิษเฉียบพลัน'), ('อันตรายต่อสุขภาพ', 'อันตรายต่อสุขภาพ'), ('ระวัง', 'ระวัง'), ('อันตรายต่อิ่งแวดล้อม', 'อันตรายต่อิ่งแวดล้อม')], max_length=50),
        ),
        migrations.AlterField(
            model_name='ppe',
            name='ppe_type',
            field=models.CharField(choices=[('อุปกรณ์ป้องกันศีรษะ', 'อุปกรณ์ป้องกันศีรษะ'), ('อุปกรณ์ป้องกันใบหน้าและตา', 'อุปกรณ์ป้องกันใบหน้าและตา'), ('อุปกรณ์ป้องกันหู', 'อุปกรณ์ป้องกันหู'), ('อุปกรณ์ป้องกันการหายใจ', 'อุปกรณ์ป้องกันการหายใจ'), ('อุปกรณ์ป้องกันลำตัว', 'อุปกรณ์ป้องกันลำตัว'), ('อุปกรณ์ป้องกันมือ', 'อุปกรณ์ป้องกันมือ'), ('อุปกรณ์ป้องกันเท้า', 'อุปกรณ์ป้องกันเท้า')], max_length=50),
        ),
    ]