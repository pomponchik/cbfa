# cbfa

Немного манки-патчинга для FastAPI, хендлеры на основе классов. Пока без  поддержки ```self```.

Пользоваться так:

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
