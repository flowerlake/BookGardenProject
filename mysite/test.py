import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print((BASE_DIR + '/myapp/static').replace("\\", "/"))
print([(BASE_DIR + 'myapp/templates').replace("\\", "/")])
print(('{0}/myapp/static'.format(BASE_DIR)).replace("\\", "/"))
