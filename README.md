# Batcher

Store up items and process them as a batch, rather than one by one.

```
import batcher

def process_items(items):
    print(items)

with batcher.batcher(process_items, batch_size=5) as b:
    for i in range(10):
        b.push(i)
```

Will print:

```
[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
```
