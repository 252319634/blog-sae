import os
import sys
root = os.path.dirname(__file__)                                             #输出当前文件所在文件夹的绝对路径
sys.path.insert(0, os.path.join(root, '..', 'site-packages'))                #将root路径中的上级目录的site-packages加入到Path中去
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pythondjangotest.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()