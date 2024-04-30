import random
class OrganizationData:
    org = {
        "number&street" : 'number 101 street 404',
        "building/suite/floor" : 'building 2 floor 6 suite 909',
        "zipcode" : '40007',
        "type" : 'Multi-speciality Group'

    }
    contact = {
        'FirstName' : 'Contact FN',
        'MiddleName' : 'Contact MN',
        'LastName' : 'Contact LN',
        'Role' : 'Admin',
        'email_address' : 'Contact'+str(random.randrange(0,9999))+'@yop.com',
        'phone_number' : '6666666666',
        'phone_extn' : '1234',
        'alternate_number' : '4444444444',
        'alt_extn' : '4444',
        'Type' : 'Primary'


    }
    tin = {
        'tin_number':random.randrange(100000000,999999999),
        'valid_from':'10'+str(random.randrange(10,31))+'20'+str(random.randrange(10,18)),
        'valid_to': '10'+str(random.randrange(10,31))+'20'+str(random.randrange(21,23))

    }



