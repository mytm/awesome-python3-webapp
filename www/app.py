#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'mytm'

'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
	return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	srv = await loop.create_server(app.make_handler(), '192.168.1.125', 9000)
	logging.info('sever started at http://192.168.1.125:9000...')
	return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
