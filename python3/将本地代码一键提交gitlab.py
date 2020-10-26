import git
from  datetime import *
import os

try:
    repo = git.Repo('/Users/alias/opstool') #仓库地址
    remote = repo.remote() #创建对象
    print(remote.pull('master')) #下拉代码
    print(repo.git.add('*')) #添加本地文件
    print(repo.git.commit(m=datetime.now())) #提交代码
    print(remote.push('master')) #推送代码
except Exception as e:
    print(e)
