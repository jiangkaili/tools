# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/12/26 14:27
# @File    : fabfile.py
from fabric.api import *
from fabric.api import run, env

env.user = 'root'
# env.hosts = ['jkl@192.168.0.103:22', 'root@192.168.0.105:22']

env.port = "22"
env.password = '123456'
# env.passwords = {'jkl@192.168.0.103:22': '123456', 'root@192.168.0.105:22': '123456'}
env.tmp_ips = []

with open('panyu_31.txt') as f:
    readlines = f.readlines()
    for line in readlines:
        ip = line.strip()
        if ip:
            env.hosts.append(ip)
print(env.hosts)

with open('panyu_5.txt') as f:
    readlines = f.readlines()
    for line in readlines:
        ip = line.strip()
        if ip:
            env.tmp_ips.append(ip)
print(env.tmp_ips)


@task
def py_31_ping_5():
    with open("result.txt", "a+") as f:
        f.write("******************" + env.host + " ssh login success" + ": ***********************\n")
        for ip in env.tmp_ips:
            result = run('ping {} -c 1'.format(ip))
            if result.succeeded:
                print(ip + "-> success")
                f.write(env.host + ": ping -> " + ip + ": success\n")
            else:
                with open("result.txt", "a+") as f:
                    f.write(env.host + ": ping -> " + ip + ": error\n")


@task
def py_31_ping_31():
    with open("result.txt", "a+") as f:
        f.write("******************" + env.host + "-> ssh login success" + ": ***********************\n")
        for ip in env.hosts:
            result = run('ping {} -c 1'.format(ip))
            if result.succeeded:
                print(ip + "-> success")
                f.write(env.host + ": ping -> " + ip + ": success\n")
            else:
                with open("result.txt", "a+") as f:
                    f.write(env.host + ": ping -> " + ip + ": error\n")
