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
from ..base import ComponentAPI


class CollectionsBkLogin(object):
    """Collections of BK_LOGIN APIS"""

    def __init__(self, client):
        self.client = client

        self.get_all_users = ComponentAPI(
            client=self.client,
            method="GET",
            path="/api/c/compapi{bk_api_ver}/bk_login/get_all_users/",
            description="获取所有用户信息",
        )
        self.get_batch_users = ComponentAPI(
            client=self.client,
            method="POST",
            path="/api/c/compapi{bk_api_ver}/bk_login/get_batch_users/",
            description="批量获取用户信息",
        )
        self.get_batch_users_platform_role = ComponentAPI(
            client=self.client,
            method="POST",
            path="/api/c/compapi{bk_api_ver}/bk_login/get_batch_users_platform_role/",
            description="批量获取用户各平台角色信息",
        )
        self.get_user = ComponentAPI(
            client=self.client, method="GET", path="/api/c/compapi{bk_api_ver}/bk_login/get_user/", description="获取用户信息"
        )
        self.get_all_user = ComponentAPI(
            client=self.client,
            method="GET",
            path="/api/c/compapi{bk_api_ver}/bk_login/get_all_user/",
            description="获取所有用户信息",
        )
        self.get_batch_user = ComponentAPI(
            client=self.client,
            method="GET",
            path="/api/c/compapi{bk_api_ver}/bk_login/get_batch_user/",
            description="获取多个用户信息",
        )
        self.get_batch_user_platform_role = ComponentAPI(
            client=self.client,
            method="GET",
            path="/api/c/compapi{bk_api_ver}/bk_login/get_batch_user_platform_role/",
            description="获取多个用户在平台应用的角色",
        )
