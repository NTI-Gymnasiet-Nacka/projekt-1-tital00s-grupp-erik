# Lazy source

* DO FULL IMPORTS!!!
```python3
from lazysource.module.file import Class
```
Test your subprogramms within that file in:
```python3
if __name__ == "__main__":
    run()
    print("YOUr tests etc")
    print("LAter we all gonna connect theese subprogramms in server module")
```
## To run individual files (without .py extension):
* PS not sure how all this works in vscode? MAybe u'll can just press
  play?!

```bash
cd lazysource
py -m module.file
```
## TO run an file from the root (without .py extension):
```bash
py -m lazysource.module.file
```

