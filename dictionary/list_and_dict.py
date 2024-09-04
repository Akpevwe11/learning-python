#Adding lists as value
eng_dict = {}

eng_dict['Solitude'] = ['lone', 'lonely', 'alone', 'unaccompanied', 'single', 'solitary',
                        'isolated', 'secluded']
eng_dict['Hope'] = ['aspiration', 'desire', 'wish', 'expectation', 'ambition', 'aim', 'goal']
print(eng_dict)

#Creating a dictionary with an empty list
eng_dict.clear()
eng_dict = {'solitude':[]}
eng_words = ['lone', 'lonely', 'alone', 'unaccompanied', 'single', 'solitary', 'isolated', 'secluded']
eng_dict['solitude'].append(eng_words[0])
print(eng_dict)

eng_dict['solitude'] = eng_words
print(eng_dict)

if 'solitude' in eng_dict:
    for list_item in eng_dict['solitude']:
        print(list_item)