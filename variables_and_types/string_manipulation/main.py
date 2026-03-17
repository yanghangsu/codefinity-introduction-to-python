grocery_items = "milk cheese bread apples oranges chicken"
dairy1 = grocery_items[0:4]
dairy2 = grocery_items[5:11]
bakery1 = grocery_items[12:17]

# 从索引 a 开始，一直到索引 b 之前（不包括 b）, 数学中的区间：[a, b), 
# 数学和计算机中经常用 [start, end) 这样的左闭右开区间

print(f"We have dairy and bakery items: <{dairy1}>, <{dairy2}>, and <{bakery1}> in aisle 5")