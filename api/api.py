# -*- coding: utf-8 -*-

"""
    Module with classes which get data from redis.
"""
import redis
import time
import settings
from datetime import date
from flask import jsonify
from flask_restful import Resource


FORMAT_DATE = '%Y-%m-%d'

FORMAT_DATETIME = '%Y-%m-%d %H:%M:%S.%f'


def convert_to_date(date_to_convert, format_date):
    """
    Function converts string to date. Very useful to compare date.
    :param date_to_convert:
    :param format_date:
    :return: date
    """
    datetime_convert = time.strptime(date_to_convert, format_date)
    return date(*datetime_convert[:3])


class Items(object):
    """
    Class Items connect and get data from redis. Method get_items can return all data from redis
    or filtered from one day.
    """
    def __init__(self):
        """
        Connection with redis.
        """
        self.redis_server = redis.Redis(host=settings.HOST, port=settings.PORT_REDIS, password=settings.PASSWORD)

    def get_items(self, date_filter=False, date_item=None):
        """
        Get items (hotshots) from redis.
        Parameter date_filter decide if we want hotshots from one day or all.
        :param date_filter
        :param date_item
        """
        keys = self.redis_server.keys()

        items = []

        if date_filter:
            keys = [key for key in keys if convert_to_date(key, FORMAT_DATETIME) == convert_to_date(date_item, FORMAT_DATE)]

        for key in keys:
            item = self.redis_server.hgetall(key)
            item['title'] = unicode(item.get('title'), 'utf-8')
            items.append(item)

        items.sort(reverse=True)

        return items


class HotshotsAll(Resource, Items):
    """
    This class return all data from redis.
    """
    def get(self):
        """
        Shows all hotshots.
        :return JSON
        """
        return jsonify(hotshots=self.get_items())


class HotshotsOneDay(Resource, Items):
    """
    Class HotshotsAll return filtered data from redis.
    """
    def get(self, date_hotshot):
        """
        Shows hotshots from one day.
        :param date_hotshot: string ex. 2015-11-05
        :return: JSON with data
        """
        return jsonify(hotshots=self.get_items(True, date_hotshot))
