class URLShortener:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.counter = 0
        self.base_url = "http://short.url/"

    def encode(self, longUrl):
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]

        code = self._encode_base62(self.counter)
        self.counter += 1

        self.url_to_code[longUrl] = code
        self.code_to_url[code] = longUrl

        return self.base_url + code

    def decode(self, shortUrl):
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(code, "")

    def _encode_base62(self, num):
        chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if num == 0:
            return chars[0]

        result = []
        while num > 0:
            result.append(chars[num % 62])
            num //= 62

        return ''.join(reversed(result))
