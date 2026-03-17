# 从索引 a 开始，一直到索引 b 之前（不包括 b）, 数学中的区间：[a, b), 
# 数学和计算机中经常用 [start, end) 这样的左闭右开区间

s = "Python"
# 索引: 0 1 2 3 4 5
#      P y t h o n
s1 = s[0:1]  # 'P'      取索引 0
s2 = s[0:2]  # 'Py'     取索引 0,1
s3 = s[0:3]  # 'Pyt'    取索引 0,1,2
s4 = s[0:6]  # 'Python' 取索引 0,1,2,3,4,5
# 要包括哪个索引，就必须让右边的值 = 那个索引 + 1
print(f"P:{s1}, Py:{s2}, Pyt:{s3},Python:{s4}")

grocery_items = "milk cheese bread apples oranges chicken"
dairy1 = grocery_items[0:4]
dairy2 = grocery_items[5:11]
bakery1 = grocery_items[12:17]



print(f"We have dairy and bakery items: <{dairy1}>, <{dairy2}>, and <{bakery1}> in aisle 5")