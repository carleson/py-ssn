print ('==============================')
print ('Social Security Number Validator')
print ('')
print ('version 0.1')
print ('==============================')
country = input('Enter Country (sv,dk, no, fi): ')
ssn = input('Enter Social Security Number (SSN): ')
ssn = str.replace(ssn,'-','')
ssn = str.replace(ssn,'.','')
ssn = ssn.strip()

if country == str.lower('sv'):
        print ('Sweden')
elif country == str.lower('no'):
        print ('Norway')
else:
        print ('Unknown option !')
print (ssn)

