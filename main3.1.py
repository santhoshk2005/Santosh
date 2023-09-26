def linearsearchproduct(productList,targetproduct):
  indices=[]
  for index, product in enumerate(productList):
    if product==targetproduct:
      indices.append(index)
  return indices
#Example usage:
product=["shoes","boot","loafer","sandel","shoes",]
target="shoes"
target2="apple"
result=linearsearchproduct(product,target2)
print(result)
