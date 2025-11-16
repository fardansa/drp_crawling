import urllib.request
import re

url = "https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html"
response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")

pattern = r'<article class="product_pod">.*?</article>'
books = re.findall(pattern, html, re.DOTALL)

print(f"Jumlah buku: {len(books)}")