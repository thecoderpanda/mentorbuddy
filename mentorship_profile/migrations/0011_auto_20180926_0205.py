# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-26 02:05
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship_profile', '0010_auto_20180905_0128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentee',
            name='area_of_interest',
        ),
        migrations.AddField(
            model_name='mentee',
            name='areas_of_guidance',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('portfolio_code_review', 'Portfolio / Code Reviews'), ('job_search_interviews', 'Job Search and Interviews'), ('industry_trends', 'Industry Trends, Skills, Technologies'), ('leadership_management', 'Leadership / Management'), ('business_entrepreneurship', 'Business, Entrepreneurship'), ('career_growth', 'Career Growth')], default='unknown', max_length=130),
        ),
    ]
