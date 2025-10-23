import unittest
from solution import URLShortener


class TestURLShortener(unittest.TestCase):
    def test_basic_encode_decode(self):
        shortener = URLShortener()
        long_url = "https://example.com/very/long/path"
        short = shortener.encode(long_url)
        self.assertEqual(shortener.decode(short), long_url)

    def test_multiple_urls(self):
        shortener = URLShortener()
        url1 = "https://example.com/page1"
        url2 = "https://example.com/page2"
        short1 = shortener.encode(url1)
        short2 = shortener.encode(url2)
        self.assertNotEqual(short1, short2)
        self.assertEqual(shortener.decode(short1), url1)
        self.assertEqual(shortener.decode(short2), url2)

    def test_same_url_twice(self):
        shortener = URLShortener()
        url = "https://example.com/page"
        short1 = shortener.encode(url)
        short2 = shortener.encode(url)
        self.assertEqual(short1, short2)

    def test_different_short_codes(self):
        shortener = URLShortener()
        urls = [f"https://example.com/page{i}" for i in range(5)]
        shorts = [shortener.encode(url) for url in urls]
        self.assertEqual(len(set(shorts)), 5)

    def test_decode_all_encoded(self):
        shortener = URLShortener()
        urls = ["https://a.com", "https://b.com", "https://c.com"]
        shorts = [shortener.encode(url) for url in urls]
        decoded = [shortener.decode(short) for short in shorts]
        self.assertEqual(decoded, urls)


if __name__ == "__main__":
    unittest.main(verbosity=2)
