shopping_list = {
    'warzywniak': ['burak','por','jablko','gruszka'],
    'miesny': ['cielecina', 'jagniecina', 'baranina'],
    'spozywczy': ['mleko', 'ser', 'jajka']
}
count = 0
for shop, products in shopping_list.items():
    print(f"Idę do {shop.capitalize()}, kupuję tu następujące rzeczy: {[i.capitalize() for i in products]}")
    count += len(products)
print(f"W sumie kupuję tyle produktów: {count}")
