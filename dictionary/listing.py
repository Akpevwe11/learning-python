sal_info = dict()
print(sal_info)

sal_info = {'Austin': 911985, 'Dallas': 911985, 'Houston': 911985, 'San Antonio': 911985}
print(sal_info)

print(sal_info.get('Austin', 'not found'))

##reassiigns the salary for Austin

sal_info['Austin'] = 1000000
print(sal_info)

##adding a new city
## sal_info.clear()
print(sal_info)

if 'San Antonio' not in sal_info:

    sal_info['San Antonio'] = 1000000
    print(sal_info)

## check using the not if
print(sal_info.keys())
print(sal_info.values())

print("key-value pair")
for key, value in sal_info.items():
    print(key, value)

print("City with highest Salary " + max(sal_info, key=sal_info.get))
print("City with lowest Salary " + min(sal_info, key=sal_info.get))

#prints dictionary in sorted order
print(sal_info)
print(sorted(sal_info.keys()))
print(sorted(sal_info.values()))
