import json
import os
def read_data(path, category_id = 0):
    with open(os.path.join(path, 'data/data.json'), encoding='utf-8') as f:
        products = json.load(f)
        if category_id > 0:
            products = [ p for p in products if p['category_id'] == category_id]
        return products