# Generated by Django 3.0.5 on 2022-07-15 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200508_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Giao_vien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_gv', models.CharField(blank=True, max_length=10, null=True)),
                ('ten_gv', models.CharField(max_length=30)),
                ('gioi_tinh', models.CharField(max_length=10)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Khoi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_khoi', models.SmallIntegerField()),
                ('ten_khoi', models.CharField(blank=True, max_length=100, null=True)),
                ('khoi_tit', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nien_khoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nien_khoa', models.CharField(max_length=9)),
                ('nien_khoa_tit', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mon_hoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_mon', models.CharField(max_length=10)),
                ('ten_mon', models.CharField(max_length=50)),
                ('mon_tit', models.CharField(blank=True, max_length=200, null=True)),
                ('ma_khoi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.Khoi')),
            ],
        ),
        migrations.CreateModel(
            name='Lop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_lop', models.CharField(max_length=10)),
                ('ten_lop', models.CharField(max_length=50)),
                ('ma_gv', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.Giao_vien')),
                ('ma_khoi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.Khoi')),
                ('nien_khoa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.Nien_khoa')),
            ],
        ),
        migrations.CreateModel(
            name='Hoc_sinh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ma_hs', models.CharField(max_length=10)),
                ('ho_ten', models.CharField(blank=True, max_length=100, null=True)),
                ('ngay_sinh', models.DateField(blank=True, null=True)),
                ('gioi_tinh', models.CharField(blank=True, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ')], max_length=10, null=True)),
                ('dia_chi', models.CharField(blank=True, max_length=150, null=True)),
                ('phu_huynh', models.CharField(blank=True, max_length=150, null=True)),
                ('phone_phu_huynh', models.CharField(blank=True, max_length=10, null=True)),
                ('diem_toan', models.FloatField(blank=True, null=True)),
                ('diem_van', models.FloatField(blank=True, null=True)),
                ('diem_ngoai_ngu', models.FloatField(blank=True, null=True)),
                ('diem_ly', models.FloatField(blank=True, null=True)),
                ('diem_hoa', models.FloatField(blank=True, null=True)),
                ('diem_tb', models.FloatField(blank=True, null=True)),
                ('ghi_chu', models.TextField(blank=True, max_length=350, null=True)),
                ('gv_hoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='school.Giao_vien')),
                ('gv_ly', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='school.Giao_vien')),
                ('gv_ngoai_ngu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='school.Giao_vien')),
                ('gv_toan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='school.Giao_vien')),
                ('gv_van', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='school.Giao_vien')),
                ('gvcn', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='school.Giao_vien')),
                ('ma_lop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='school.Lop')),
                ('mon_hoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='school.Mon_hoc')),
                ('mon_ly', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='school.Mon_hoc')),
                ('mon_ngoai_ngu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='school.Mon_hoc')),
                ('mon_toan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='school.Mon_hoc')),
                ('mon_van', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='school.Mon_hoc')),
            ],
        ),
    ]
