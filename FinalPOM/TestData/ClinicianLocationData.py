import random
import string

class ClinicianLocationData:
    alpha = string.ascii_letters

    clinician = {
        'NPI': '1245609908',
        'memeberID' : '',
        'DOB': 10202000,
        'email': 'clin' + str(random.randrange(1, 999999)) + '@yop.co.in',
        'phone': str(random.randrange(1000000000, 9999999999)),
        'phoneextn': '1234',
        'clinicianType': '',
        'nonCinicianType': '',
        'designation': '',
        'title': '',
        'gender': ''
    }

    location = {
        'name': "".join(random.choices(alpha + string.digits, k=5)),
        'id': "".join(random.choices(alpha + string.digits, k=4)),
        'area': 'Rural',
        'type': 'Full Time',
        'number': "".join(random.choices(alpha + string.digits, k=5)),
        'building': "".join(random.choices(alpha + string.digits, k=5)),
        'zipcode': '40008'

    }
