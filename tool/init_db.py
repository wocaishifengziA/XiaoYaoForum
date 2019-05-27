# -*- coding:utf-8 -*-
from apps.community.models import CommunityGroup, CommunityGroupMember, Post, PostComment, CommentLike
from peewee import MySQLDatabase

from apps.question.models import Question, Answer
from apps.users.models import User
# from apps.community.models import CommunityGroup, CommunityGroupMember, Post, PostComment, CommentLike
# from apps.question.models import *

from XiaoYaoForm.settings import database

database = MySQLDatabase(
    'xyforum', host="118.24.115.8", port=3306, user="root", password="123456"
)


def init():
    # 生成表
    database.create_tables([User])
    database.create_tables([CommunityGroup, CommunityGroupMember])
    database.create_tables([Post, PostComment, CommentLike])
    database.create_tables([Question, Answer])


if __name__ == "__main__":
    init()
