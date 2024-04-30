import random

class RegistrationData:
    num = str(random.randrange(0,9999))
    reg = {
        "first_name" : 'test first',
        "last_name" : 'test last',
        "email_address" : num+'@yopmail.com',
        "contact_no" : '4444444444',
        "username" : num,
        "org_name" : 'hospitals and labs'+num,
        "tin" : str(random.randrange(100000000,999999999))

    }