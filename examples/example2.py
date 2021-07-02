import shoestring

def example2():
    markdown = shoestring.MarkdownParser('''
# Example markdown with code snippet

```python
num = 0
for j in range(20):
    num = num + j
print(j)
```

```bash
echo "Hello, world!"
```
    ''')

    for cs in markdown.code_snippets:
        print(f'Snippet language: {cs.language}; Snippet length: {len(cs.code)}')
    

if __name__ == '__main__':
    example2()