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
# Generated by Django 2.2.8 on 2020-07-15 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("node_man", "0010_auto_20200628_1746"),
    ]

    operations = [
        migrations.AddField(
            model_name="processstatus",
            name="retry_times",
            field=models.IntegerField(default=0, verbose_name="重试次数"),
        ),
    ]
