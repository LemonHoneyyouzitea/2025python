# author:zzk
# 2025年01月03日
import sys
print(sys.path)
sys.path.insert(0,'module')
print(sys.path)
print('-'*50)
import my_module
my_module.test1()