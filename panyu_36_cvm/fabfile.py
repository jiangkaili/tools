# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/12/26 14:27
# @File    : fabfile.py
import os

from fabric.api import *
from fabric.api import run, env

env.user = 'root'
env.hosts = []

env.port = "22"
env.password = '123456'
env.tmp_ips = []

with open('panyu_36.txt') as f:
    readlines = f.readlines()
    for line in readlines:
        ip = line.strip()
        if ip:
            env.hosts.append(ip)

# with open('tmp.txt') as f:
#     readlines = f.readlines()
#     for line in readlines:
#         ip = line.strip()
#         if ip:
#             env.hosts.append(ip)

if os.path.exists("result.txt"):
    os.remove("result.txt")

@task
def py_36_cvm():
    with open("result.txt", "a+") as f:
        f.write("******************" + env.host + " ssh login success" + ": ***********************\n")

        result_cpu = run(' cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c')
        f.write(env.host + " cpu:  " + result_cpu + "\n")

        result_mem = run('cat /proc/meminfo | grep MemTotal')
        f.write(env.host + " mem:  " + result_mem + "\n")

        f.write("---------- disk -------------\n")
        result_df = run('df -h')
        f.write(result_df)
        f.write("\n")

        f.write("---------- network ----------\n")
        result_ifcfg = run('cat /etc/sysconfig/network-scripts/ifcfg-ens33')
        f.write(result_ifcfg)
        f.write("\n")

