def linearSearchProduct(productList,targetProduct):
  indices = []
  for index,product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices
products = ["keyboard", "printer", "mouse", "keyboard", "touchpad", "keyboard"]
target = "keyboard"
result = linearSearchProduct(products,target)
print(result)