# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-节点管理(BlueKing-BK-NODEMAN) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at https://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
# Generated by Django 2.2.8 on 2020-06-02 03:04

import django_mysql.models
from django.db import migrations

import apps.node_man.models


class Migration(migrations.Migration):

    dependencies = [
        ("node_man", "0005_auto_20200518_1209"),
    ]

    operations = [
        migrations.AddField(
            model_name="host",
            name="extra_data",
            field=django_mysql.models.JSONField(blank=True, default=dict, null=True, verbose_name="额外数据"),
        ),
        migrations.AlterField(
            model_name="pipelinetree",
            name="tree",
            field=apps.node_man.models.LazyJSONField(default=dict, verbose_name="Pipeline拓扑树"),
        ),
    ]
