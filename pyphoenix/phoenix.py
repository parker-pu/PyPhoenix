# -*- coding: utf-8 -*-
import logging
import os
import sys

import jaydebeapi

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)


class PhoenixDB:
    """ 操作 Phoenix
    """
    url: str = "jdbc:127.0.0.1:2181;"
    drive: str = "org.apache.phoenix.jdbc.PhoenixDriver"
    params: dict = {'phoenix.schema.isNamespaceMappingEnabled': 'true'}
    jar_file: str = None

    logger = logging

    def __init__(self, *args, **kwargs):
        """ 初始化输入
        :param args:
        :param kwargs:
        """
        self.url = kwargs.get("url", self.url)
        self.drive = kwargs.get("drive", self.drive)
        self.params.update(kwargs.get("params", {}))
        self.jar_file = kwargs.get("jar_file", self.jar_file)
        self.logger = logging.getLogger(self.__class__.__name__)

    @property
    def connect(self):
        """ 返回一个连接 """
        return jaydebeapi.connect(self.drive, self.url, self.params, self.jar_file)

    def execute(self, sql):
        """ 执行对应的 SQL
        :param sql:
        :return:
        """
        con = self.connect
        curs = con.cursor()
        curs.execute(sql)
        con.commit()

        result = []
        try:
            result = curs.fetchall()
            self.logger.info("operation {} line".format(curs.rowcount))
        except jaydebeapi.Error as e:
            self.logger.error(e)
        finally:
            con.close()

        return result
