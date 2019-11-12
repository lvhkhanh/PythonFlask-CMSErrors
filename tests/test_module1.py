## Imports
import pytest
import re
import sqlite3

from pathlib import Path
from redbaron import RedBaron

from tests.utils import *
#!

## Paths
handlers = Path.cwd() / 'cms' / 'handlers.py'
auth = Path.cwd() / 'cms' / 'admin' / 'auth.py'
#!

## Module Functions
def get_source_code(file_path):
    with open(file_path.resolve(), 'r') as source_code:
        return RedBaron(source_code.read())
#!

## Source Code
handlers_code = get_source_code(handlers)
auth_code = get_source_code(auth)
#!

## Tests
@pytest.mark.test_disable_werkzeug_logging_module1
def test_disable_werkzeug_logging_module1():
    # 01. Disable Werkzeug Logging
    # from logging import getLogger
    # request_log = getLogger('werkzeug')
    # request_log.disabled = True
    logging_import = get_imports(handlers_code, 'logging')
    logging_import_exits = logging_import is not None
    assert logging_import_exits, \
        'Do you have a `werkzeug.security` import statement?'
    get_logger_exists = 'getLogger' in logging_import
    assert get_logger_exists, \
        'Are you importing `getLogger` from `logging` in `cms/handlers.py`?'

    request_log = handlers_code.find('assign', lambda node: node.target.value == 'request_log')
    request_log_exists = request_log is not None
    assert request_log_exists, \
        'Are you setting the `user_id` variable correctly?'
    get_call = request_log.find('atomtrailers', lambda node: \
        node.value[0].value == 'getLogger' and \
        node.value[1].type == 'call'
        )
    get_call_exists = get_call is not None
    assert get_call_exists, \
        'Are you calling the `getLogger()` function and assigning the result to `request_log`?'
    get_argument = get_call.find('call_argument', lambda node: \
        str(node.value.value).replace("'", '"') == '"werkzeug"'  
    ) is not None
    assert get_argument, \
        'Are you passing the `getLogger()` function the correct argument?'


    request_log_disabled = handlers_code.find('assign', lambda node: \
        # node.target.find('atomtrailers', lambda node: \
        #     node.value[0].value == 'request_log' and \
        #     node.value[1].value == 'disabled'
        # ) and \
        print(type(node.value))
    )
    print(request_log_disabled)
    # request_log_disabled_exists = request_log_disabled is not None
    # assert request_log_disabled_exists, \
    #     'Have you set the `disabled` property on `request_log` to `True`?'

    assert False
'''
@pytest.mark.test_configure_logging_module1
def test_models_configure_logging_module1():
    # 02. Configure Logging
    # def configure_logging(name, level):
    #     log = getLogger(name)
    #     log.setLevel(level)
    assert False

@pytest.mark.test_rotating_file_handler_module1
def test_models_rotating_file_handler_module1():
    # 03. Rotate File Handler
    # from logging.handlers import RotatingFileHandler
    # handler = RotatingFileHandler('logs/{}.log'.format(name), maxBytes=5*1024*1024, backupCount=10)
    assert False

@pytest.mark.test_add_handler_module1
def test_models_add_handler_module1():
    # 04. Add Log Handler
    # log.addHandler(handler)
    # return log
    assert False

@pytest.mark.test_timestamp_module1
def test_models_timestamp_module1():
    # 05. Timestamp Formatting
    # from time import strftime
    # timestamp = strftime('[%d/%b/%Y %H:%M:%S]')
    assert False

@pytest.mark.test_access_log_module1
def test_modelsaccess_log__module1():
    # 06. Access Log
    # from logging import INFO, WARN, ERROR
    # access_log = configure_logging('access', INFO)
    assert False

@pytest.mark.test_after_request_module1
def test_models_after_request_module1():
    # 07. After Request
    # @app.after_request
    # def after_request(response):
    #     return response
    assert False

@pytest.mark.test_access_log_format_module1
def test_models_access_log_format_module1():
    # 08. Access Log Format
    # access_log.info('%s - - %s "%s %s %s" %s -', request.remote_addr, timestamp, request.method, request.path, request.scheme.upper(), response.status_code)
    assert False

@pytest.mark.test_valid_status_codes_module1
def test_models_valid_status_codes_module1():
    # 09. Valid Status Codes
    # if int(response.status_code) < 400:
    assert False
#!
'''