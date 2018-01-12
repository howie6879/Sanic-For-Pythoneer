#!/usr/bin/env python
import os

from functools import wraps

from motor.motor_asyncio import AsyncIOMotorClient

MONGODB = dict(
    MONGO_HOST=os.getenv('MONGO_HOST', ""),
    MONGO_PORT=os.getenv('MONGO_PORT', 27017),
    MONGO_USERNAME=os.getenv('MONGO_USERNAME', ""),
    MONGO_PASSWORD=os.getenv('MONGO_PASSWORD', ""),
    DATABASE='test_mongodb',
)


def singleton(cls):
    """
    用装饰器实现的实例 不明白装饰器可见附录 装饰器：https://github.com/howie6879/Sanic-For-Pythoneer/blob/master/docs/part2/%E9%99%84%E5%BD%95%EF%BC%9A%E5%85%B3%E4%BA%8E%E8%A3%85%E9%A5%B0%E5%99%A8.md
    :param cls: cls
    :return: instance
    """
    _instances = {}

    @wraps(cls)
    def instance(*args, **kw):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kw)
        return _instances[cls]

    return instance


class MotorBaseOld:
    """
    默认实现了一个db只创建一次，缺点是更换db麻烦
    """
    _db = None
    MONGODB = MONGODB

    def client(self, db):
        # motor
        self.motor_uri = 'mongodb://{account}{host}:{port}/{database}'.format(
            account='{username}:{password}@'.format(
                username=self.MONGODB['MONGO_USERNAME'],
                password=self.MONGODB['MONGO_PASSWORD']) if self.MONGODB['MONGO_USERNAME'] else '',
            host=self.MONGODB['MONGO_HOST'] if self.MONGODB['MONGO_HOST'] else 'localhost',
            port=self.MONGODB['MONGO_PORT'] if self.MONGODB['MONGO_PORT'] else 27017,
            database=db)
        return AsyncIOMotorClient(self.motor_uri)

    @property
    def db(self):
        if self._db is None:
            self._db = self.client(self.MONGODB['DATABASE'])[self.MONGODB['DATABASE']]

        return self._db


@singleton
class MotorBase:
    """
    更改mongodb连接方式 单例模式下支持多库操作
    About motor's doc: https://github.com/mongodb/motor
    """
    _db = {}
    _collection = {}
    MONGODB = MONGODB

    def __init__(self):
        self.motor_uri = ''

    def client(self, db):
        # motor
        self.motor_uri = 'mongodb://{account}{host}:{port}/{database}'.format(
            account='{username}:{password}@'.format(
                username=self.MONGODB['MONGO_USERNAME'],
                password=self.MONGODB['MONGO_PASSWORD']) if self.MONGODB['MONGO_USERNAME'] else '',
            host=self.MONGODB['MONGO_HOST'] if self.MONGODB['MONGO_HOST'] else 'localhost',
            port=self.MONGODB['MONGO_PORT'] if self.MONGODB['MONGO_PORT'] else 27017,
            database=db)
        return AsyncIOMotorClient(self.motor_uri)

    def get_db(self, db=MONGODB['DATABASE']):
        """
        获取一个db实例
        :param db: database name
        :return: the motor db instance
        """
        if db not in self._db:
            self._db[db] = self.client(db)[db]

        return self._db[db]

    def get_collection(self, db_name, collection):
        """
        获取一个集合实例
        :param db_name: database name
        :param collection: collection name
        :return: the motor collection instance
        """
        collection_key = db_name + collection
        if collection_key not in self._collection:
            self._collection[collection_key] = self.get_db(db_name)[collection]

        return self._collection[collection_key]


if __name__ == '__main__':
    import asyncio


    async def do_insert(db):
        data = {
            "user": 'user01',
            "password": '123456',
        }
        result = await db.user.insert_one(data)
        print('插入成功：{0}'.format(result.inserted_id))
        return result


    old_ins = MotorBaseOld()
    old_ins_db = old_ins.db

    new_ins = MotorBase()
    new_ins_db = new_ins.get_db()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_insert(old_ins_db))

    loop.run_until_complete(do_insert(new_ins_db))
