from pathlib import Path

def shopping(shop_file):
  data_path = Path() / "data"
  target_path = data_path / shop_file
  shop_dict = {} 
  with open(target_path, mode='r', encoding='utf-8') as f:
    for i, line in enumerate(f):
      if i >= 2:
        product, price = line.split()
        shop_dict[product] = price
  return shop_dict

def item_price(shop_file, item):
    shop_dict = shopping(shop_file)
    return shop_dict[item]
