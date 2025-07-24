# ---------------------------
# 一、创建列表
# ---------------------------
# 空列表
empty_list = []  
# 基础数据类型列表
basic_list = [1, "apple", 3.14, True]  
# 嵌套列表(列表中包含列表、元组、字典)
nested_list = [
    1,  
    [2, 3, [4, 5]],  # 二维嵌套
    ("a", "b"),      # 包含元组
    {"key": "value"} # 包含字典
]
print("创建的嵌套列表:", nested_list)  # 输出: [1, [2, 3, [4, 5]], ('a', 'b'), {'key': 'value'}]


# ---------------------------
# 二、访问元素(查)
# ---------------------------
fruits = ["apple", "banana", "cherry", "date"]

# 按索引访问(正数/负数索引)
print("\n访问元素:")
print("索引0的元素:", fruits[0])       # apple
print("最后一个元素:", fruits[-1])     # date

# 切片操作 [start:end:step]
print("索引1-2的元素(不包含end):", fruits[1:3])   # ['banana', 'cherry']
print("倒序切片(步长-1):", fruits[::-1])          # ['date', 'cherry', 'banana', 'apple']


# ---------------------------
# 三、增加元素(增)
# ---------------------------
nums = [1, 2, 3]

# append():末尾添加单个元素
nums.append(4)        # [1, 2, 3, 4]
print("\nappend后:", nums)

# extend():扩展另一个列表
nums.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
print("extend后:", nums)

# insert(index, value):指定位置插入
nums.insert(0, 0)     # 在索引0插入0，结果: [0, 1, 2, 3, 4, 5, 6]
print("insert后:", nums)

# 列表拼接 +
new_list = nums + [7, 8]  # 生成新列表，原列表不变
print("拼接后新列表:", new_list)

# 解包 * 添加元素
chars = ['a', 'b']
nums.extend([*chars, 9])  # 解包chars为单个元素，结果: [0, 1, 2, 3, 4, 5, 6, 'a', 'b', 9]
print("解包添加后:", nums)


# ---------------------------
# 四、删除元素(删)
# ---------------------------
fruits = ["apple", "banana", "cherry", "banana"]

# del:按索引删除(单个或切片)
del fruits[1]               # 删除索引1的"banana"，结果: ['apple', 'cherry', 'banana']
print("\ndel索引1后:", fruits)
del fruits[1:3]             # 删除索引1到2(不包含3)，结果: ['apple']
print("del切片后:", fruits)

# pop(index):删除并返回元素(默认最后一个)
popped = fruits.pop()       # 删除"apple"，popped="apple"，列表为空
print("pop后列表:", fruits)

# remove(value):删除首个匹配值
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")     # 删除第一个"banana"，结果: ['apple', 'cherry', 'banana']
print("remove后:", fruits)

# clear():清空列表
fruits.clear()              # 结果: []
print("clear后:", fruits)


# ---------------------------
# 五、修改元素(改)
# ---------------------------
nums = [10, 20, 30, 40]

# 直接赋值修改单个元素
nums[2] = 300             # 结果: [10, 20, 300, 40]
print("\n修改后:", nums)

# 切片修改(批量替换)
nums[1:3] = [200, 250]    # 索引1-2替换为[200,250]，结果: [10, 200, 250, 40]
print("切片修改后:", nums)
nums[1:3] = [2000]        # 长度可不同，结果: [10, 2000, 40]
print("切片修改(长度不同)后:", nums)


# ---------------------------
# 六、嵌套列表操作
# ---------------------------
# 创建二维列表
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 访问嵌套元素
print("\n嵌套列表访问:")
print("第二行第三列元素:", matrix[1][2])  # 5(索引从0开始，行1，列2)
print("第三行逆序元素:", matrix[-1][::-1]) # [9, 8, 7]

# 修改嵌套元素
matrix[0][1] = 20       # 修改第一行第二列元素为20，结果: [[1, 20, 3], [4, 5, 6], [7, 8, 9]]
print("修改后二维列表:", matrix)

# 向嵌套列表中添加元素
matrix[2].append(10)    # 向第三行添加10，结果: [7, 8, 9, 10]
print("添加元素后第三行:", matrix[2])

# 删除嵌套元素
del matrix[1][0]        # 删除第二行第一个元素4，结果: [[1, 20, 3], [5, 6], [7, 8, 9, 10]]
print("删除后二维列表:", matrix)


# ---------------------------
# 七、常用方法与内置函数
# ---------------------------
words = ["banana", "apple", "cherry", "apple"]

# 长度
print("\n列表长度:", len(words))  # 4

# 元素出现次数
print("apple出现次数:", words.count("apple"))  # 2

# 元素索引
print("cherry的索引:", words.index("cherry"))  # 2

# 排序
nums = [3, 1, 4, 2]
nums.sort()                # 原地排序，结果: [1, 2, 3, 4]
print("排序后:", nums)
sorted_nums = sorted(nums, reverse=True)  # 降序排序，生成新列表
print("降序排序:", sorted_nums)

# 反转
nums.reverse()             # 原地反转，结果: [4, 3, 2, 1]
print("反转后:", nums)

# 浅拷贝(嵌套列表需深拷贝)
copied_list = nums.copy()  # 或 nums[:]
print("浅拷贝:", copied_list)


# ---------------------------
# 八、列表推导式
# ---------------------------
# 生成平方数列表
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]
print("\n列表推导式-平方数:", squares)

# 筛选偶数
even_nums = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
print("列表推导式-偶数:", even_nums)

# 嵌套列表推导式(二维转一维)
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]  # [1, 2, 3, 4, 5, 6]
print("列表推导式-二维转一维:", flat)