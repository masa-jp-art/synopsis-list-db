!pip install gspread oauth2client openai==0.28 google-auth google-auth-oauthlib google-auth-httplib2 pandas --upgrade

import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import openai
import pandas as pd
from google.colab import auth
from google.auth import default
import os
import json

# Google認証
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)

# スプレッドシートとシートを開く
sheet_url = '<ここにスプレッドシートのURLを入れる>'
spreadsheet = gc.open_by_url(sheet_url)

# 各シートを取得
sheet_protagonist = spreadsheet.worksheet('protagonist')
sheet_SubCharacter = spreadsheet.worksheet('SubCharacter')
sheet_antagonist = spreadsheet.worksheet('antagonist')
sheet_catharsis = spreadsheet.worksheet('catharsis')
sheet_prot = spreadsheet.worksheet('prot')

# シートからランダムに値を取得
protagonist_reference= random.choice(sheet_protagonist.col_values(2)[1:])
SubCharacter_reference= random.choice(sheet_SubCharacter.col_values(2)[1:])
antagonist_reference= random.choice(sheet_antagonist.col_values(2)[1:])
catharsis_reference= random.choice(sheet_catharsis.col_values(2)[1:])
prot_reference= random.choice(sheet_prot.col_values(2)[1:])
print(f"""
# 資料
\n\n## 登場人物の設定
\n\n### 主人公
\n\n
\n\n
{protagonist_reference}
\n\n
\n\n### サブキャラクター
\n\n
{SubCharacter_reference}
\n\n
\n\n### 主人公と対立する者
\n\n
{antagonist_reference}
\n\n
\n\n## プロットの設定
\n\n### プロットの目的
\n\n
{catharsis_reference}
\n\n
\n\n### プロットの型
\n\n
{prot_reference}
\n\n
""")
