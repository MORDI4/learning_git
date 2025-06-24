shopping_list = {
    'warzywniak': ['burak','por','jablko','gruszka'],
    'miesny': ['cielecina', 'jagniecina', 'baranina'],
    'spozywczy': ['mleko', 'ser', 'jajka']
}
count = 0
for shop, products in shopping_list.items():
    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {products}")
    count += len(products)
print(f"W sumie kupuję {count} produktów.")