import json
import time

import aiohttp
import requests

url = "https://script.google.com/macros/s/AKfycbzFXVfjwX_RB6XkjLpwlMIXl_IVeoqaYnfhRf774xknBAcV00Ef3OPK89uS7TBFppwfVg/exec"


class TranslateError(Exception):
    pass


class Translator:
    def translate(self, text="Hello World!!", source="", target="ja"):
        try:
            return json.loads(requests.post(url, data={"text": text, "source": source, "target": target}).text)["result"]
        except json.JSONDecodeError:
            raise TranslateError("The API is not working properly.")


class AsyncTranslator:
    async def translate(self, text="Hello World!!", source="", target="ja"):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data={"text": text, "source": source, "target": target}) as response:
                try:
                    return json.loads(await response.text())["result"]
                except json.JSONDecodeError:
                    raise TranslateError("The API is not working properly.")
