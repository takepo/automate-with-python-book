# coding: utf-8
#! python3
# pw.py - パスワード管理プログラム(脆弱性あり)

PASSWORDS = {'email': 'hoge',
             'blog': 'hogehoge',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('使い方: python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + 'のパスワードをクリップボードにコピーしました')
else:
    print(account + 'というアカウント名はありません')
