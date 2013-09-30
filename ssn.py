"""Social Security Number Validator, version 0.11 """

class SSN:
    """A simple class for validating Social Security Numbers"""

    def __init__(self, country, number):
        self._number = number.strip()
        self._number = str.replace(self._number, '-','')
        self._number = str.replace(self._number, '.','')

        self._country = str.lower(country)


        if not (self._number.isdigit()):
            raise ValueError('Invalid Social Security Number \'{}\''.format(self._number))

    @property
    def isValid(self):
        """Check if selected Social Security Number is valid """
        i = 0
        checknumber = 0
        control = 0

        while i <= 9:
            if i % 2 == 0:
                control = int(self._number[i])*2
            else:
                control = int(self._number[i])*1

            if control > 9:
                checknumber = checknumber + int(str(control)[0])+ int(str(control)[1])
            else:
                checknumber = checknumber + int(str(control))

            i = i +1

        return checknumber

    def format(self):
        """Get Social Security Number"""
        return self._number

    def country(self):
        """Get selected country"""
        if self._country == str.lower('sv'):
            return 'Sweden'
        elif self._country == str.lower('no'):
            return 'Norway'
        elif self._country == str.lower('dk'):
            return 'Denmark'
        elif self._country == str.lower('fi'):
            return 'Finland'
        else:
            return 'Unknown option !'

ssn = SSN('dk','19020101-0101')
print (ssn.isValid)
print (ssn.country())

# country = input('Enter Country (sv,dk, no, fi): ')
# ssn = input('Enter Social Security Number (SSN): ')


