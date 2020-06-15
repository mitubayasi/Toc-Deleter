#coding:utf-8

#reモジュールのインポート
import re

#同じディレクトリにあるファイルを開く
from os import path
a = path.join(path.dirname(__file__), "toc.ncx")

# ファイルを読み込む
with open(a,"r",encoding="utf-8") as file:
    filedata=file.read()

# 置換する
filedata=re.sub('.*\n.*\n.*<text>Page.*\n.*\n.*\n.*\n',"",filedata)

# ファイルに書き込む
with open(a,"w",encoding="utf-8") as file:
    file.write(filedata)