مثال عملي: دالة لإنشاء قوائم HTML

```python
def create_tag(content, tag="div"):
    return f"<{tag}>{content}</{tag}>"

print(create_tag("Hello"))         # <div>Hello</div>
print(create_tag("Title", "h1"))   # <h1>Title</h1>
```

