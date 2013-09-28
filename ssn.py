"""Social Security Number Validator, version 0.11 """

class ssn:
    """A simple class for validating Social Security Numbers"""

def __init__(self, country, number):
    self._number = number.strip()
    self._number = str.replace(self._number, '-','')
    self._number = str.replace(self._number, '.','')

    self._country = str.lower(country)


    if not (self._number.isdigit()):
        raise ValueError('Invalid Social Security Number \'{}\''.format(self._number))

def IsValid(self):
    """Check if selected Social Security Number is valid """
    return True

def Value(self):
    """Get Social Security Number"""
    return self._number

# country = input('Enter Country (sv,dk, no, fi): ')
# ssn = input('Enter Social Security Number (SSN): ')
# ssn = str.replace(ssn,'-','')
# ssn = str.replace(ssn,'.','')
# ssn = ssn.strip()
#
# if country == str.lower('sv'):
#        print ('Sweden')
# elif country == str.lower('no'):
#        print ('Norway')
#else:
#        print ('Unknown option !')
#print (ssn)

