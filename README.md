![logo](https://raw.githubusercontent.com/pomponchik/cbfa/develop/docs/assets/logo_4.png)

[![Downloads](https://static.pepy.tech/badge/cbfa/month)](https://pepy.tech/project/cbfa)
[![Downloads](https://static.pepy.tech/badge/cbfa)](https://pepy.tech/project/cbfa)
[![codecov](https://codecov.io/gh/pomponchik/cbfa/graph/badge.svg?token=7XDY2T7S68)](https://codecov.io/gh/pomponchik/cbfa)
[![Test-Package](https://github.com/pomponchik/cbfa/actions/workflows/tests_and_coverage.yml/badge.svg)](https://github.com/pomponchik/cbfa/actions/workflows/tests_and_coverage.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/cbfa.svg)](https://pypi.python.org/pypi/cbfa)
[![PyPI version](https://badge.fury.io/py/cbfa.svg)](https://badge.fury.io/py/cbfa)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)


A bit of dummy patching for FastAPI, class-based handlers. So far without `self` support.

Install it:

```bash
$ pip install cbfa
```

And use:

```python
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from cbfa import ClassBased


app = FastAPI()
wrapper = ClassBased(app)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@wrapper('/item')
class Item:
    def get(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}

    def post(item_id: int, item: Item):
        return {"item_name": item.name, "item_id": item_id}
```
