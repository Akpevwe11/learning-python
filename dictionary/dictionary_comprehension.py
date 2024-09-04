sal_data_keys = ['Austin', 'Dallas', 'Houston', 'San Antonio']
sal_data_values = [911985, 911985, 911985, 911985]

sal_info = {}
print("#### Creating a dictionary without using comprehension ####")
for key, value in zip(sal_data_keys, sal_data_values):
    sal_info[key] = value
print(sal_info)
sal_info.clear()

#Using Dictionary Comprehension to populate the dictionary
print("#### Creating a dictionary using comprehension ####")

sal_info = {key: value for key, value in zip(sal_data_keys, sal_data_values)}
print(sal_info)