import enum


class Status(enum.Enum):
    SUCCESS = {'ok': True, 'http': {'status': 200},
               'why': "request successful"}
    ERR_GLOBAL_SYSTEM = {'ok': False, 'http': {
        'status': 500}, 'why': "Internal Server Error"}
    ERR_GLOBAL_MISSING_PARAMETERS = {
        'ok': False, 'http': {'status': 400}, 'why': "Data Missing"}
    FAILURE = {'ok': False,'http':{'status':500},
                'why':'request failed'}
    CORRUPT_FILE = {'ok': False,'http':{'status':500},
                'why':'uploaded file is corrupt'}
    DATA_NOT_FOUND = {'ok': False,'http':{'status':404},
                'why':'data not found'}
    WRONG_CODE = {'ok': False,'http':{'status':501},
                'why':'WRONG_EXAM_ID'}
    WRONG_STUDENT_CODE = {'ok': False,'http':{'status':501},
                'why':'WRONG_STUDENT_ID'}
    OPERATION_NOT_PERMITTED = {'ok': False, 'http': {'status': 400},
                               'why': 'operation not permitted'}
    ERROR_WEAK_PASSWORD = {'ok': False, 'http': {'status': 400}, 'why': 'weak password, at least provide 6 characters '}
    ERROR_GATEWAY = {'ok': False, 'http': {'status': 400}, 'why': 'gateway error'}
    ERROR_WRONG_PASSWORD = {'ok': False, 'http': {'status': 400}, 'why': 'wrong password '}
    USER_ALREADY_EXISTS = {'ok': False, 'http': {'status': 400}, 'why': 'username already exists '}
