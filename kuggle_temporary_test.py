# -*- coding: utf-8 -*-
"""kuggle_temporary_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EKj8Roal7XJwuMiF5PC_KmrV7ULnoZnP
"""

import pandas as pd

# 데이터 로딩
df = pd.read_csv('https://raw.githubusercontent.com/konkuk-kuggle/Test/main/train.csv', encoding='utf-8')

df.describe()

df.info()