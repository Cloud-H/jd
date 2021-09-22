#!python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/22 3:55 下午
# @File    : pyjs.py.py
# @Project : jd_scripts
# @Desc    : 用于执行JS脚本
import os
import sys
from config import JD_COOKIES, BASE_DIR
from utils.cookie import export_cookie_env


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print('参数错误')
        sys.exit(1)
    script_path = args[1]

    if not os.path.exists(script_path):
        script_path = os.path.join(BASE_DIR, script_path)
        if not os.path.exists(script_path):
            print('脚本不存在!')
            sys.exit(1)

    export_cookie_env(JD_COOKIES)
    os.system(f'node {script_path}')
