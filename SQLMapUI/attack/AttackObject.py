# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * 攻击参数，定义了攻击动作所需要的属性
 *
 * @author margin 2017/02/16.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/02/16 margin 创建.
 *
 """

import Queue

class AttackObject(object):
    # 用户名字典
    usernames = "/Users/margin/PycharmProjects/SQLMap/SQLMapUI/attack/username.txt"
    # 密码字典
    passwords = "/Users/margin/PycharmProjects/SQLMap/SQLMapUI/attack/password.txt"
    # 攻击线程
    threads = 1
    # 超时时间
    timeout = 10
    # ip
    ip = ""
    # 端口
    port = "22"
    # 破解字典
    attack_queue = Queue.Queue(maxsize = 1)

    def __init__(self,threads=1,timeout=10):
        self.threads = threads
        self.timeout = timeout

    def getUserNames(self):
        """
        获取用户名字典
        :return:
        """
        return self.usernames

    def getPasswords(self):
        """
        获取密码字典
        :return:
        """
        return self.passwords

    def getThreads(self):
        """
        获取攻击线程
        :return:
        """
        if self.threads == 0 or self.threads == "":
            self.threads = 1
        return self.threads

    def getTimeout(self):
        """
        获取超时时间
        :return:
        """
        return self.timeout

    def getIp(self):
        """
        获取ip
        :return:
        """
        return self.ip

    def getPort(self):
        """
        获取port
        :return:
        """
        return self.port

    def getAttack_queue(self):
        """
        获取port
        :return:
        """
        return self.attack_queue