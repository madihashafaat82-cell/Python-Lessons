def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result

students = [[1. , 'Arham'],[2. , 'Hanan'] , [3. , 'Sarim'] , [4. , 'Ashir'] , [5. , 'Hassan']]

print('Original lists of list:')
print(students)
print('Convert list to a dictionary:')
print(test(students))


