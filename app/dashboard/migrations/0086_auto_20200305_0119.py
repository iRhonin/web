# Generated by Django 2.2.4 on 2020-03-05 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0085_merge_20200303_2256'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='bounty',
            index_together={('current_bounty', 'network'), ('current_bounty', 'network', 'web3_created'), ('current_bounty', 'network', 'idx_status'), ('network', 'idx_status'), ('current_bounty', 'network', 'idx_status', 'web3_created')},
        ),
    ]
