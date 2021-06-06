# google-translate.py
Library for using accurate Google Translate in Python

Pythonで正確なGoogle翻訳を使用するためのライブラリ

***


# English
This library uses the translation function of Google Apps Script.

## install
Install using pip.
```
pip install google-translate.py
```

## How to use
Normal:
```py
from google_translate_py import Translator

print(Translator().translate("Hello World!!", "en", "ja"))

>>> こんにちは世界！！
```

Async version:
```py
import asyncio
from google_translate_py import AsyncTranslator

async def main():
    print(await AsyncTranslator().translate("Hello World!!", "en", "ja"))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

>>> こんにちは世界！！
```

### Automatic language judgment
If you leave the second argument (`source`) empty, the language will be determined automatically.

Normal:
```py
from google_translate_py import Translator

print(Translator().translate("Hallo Welt!!", "", "ja"))

>>> こんにちは世界！！
```

Async version:
```py
import asyncio
from google_translate_py import AsyncTranslator

async def main():
    print(await AsyncTranslator().translate("Hallo Welt!!", "", "ja"))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

>>> こんにちは世界！！
```

**Thank you for reading!**

# 日本語
このライブラリはGoogle Apps Scriptの翻訳機能を利用しています。

## インストール
pipを使用してインストールします。
```
pip install google-translate.py
```

## 使い方
通常:
```py
from google_translate_py import Translator

print(Translator().translate("Hello World!!", "en", "ja"))

>>> こんにちは世界！！
```

非同期版:
```py
import asyncio
from google_translate_py import AsyncTranslator

async def main():
    print(await AsyncTranslator().translate("Hello World!!", "en", "ja"))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

>>> こんにちは世界！！
```

### 自動言語判定
二つ目の引数(`source`)を空にしておくと言語を自動で判定してくれます。

通常:
```py
from google_translate_py import Translator

print(Translator().translate("Hallo Welt!!", "", "ja"))

>>> こんにちは世界！！
```

非同期版:
```py
import asyncio
from google_translate_py import AsyncTranslator

async def main():
    print(await AsyncTranslator().translate("Hallo Welt!!", "", "ja"))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

>>> こんにちは世界！！
```

**読んでくれてありがとうございます!**
