from flask import Flask
import os
import pusher

app = Flask('apps')
p = pusher.Pusher(
	app_id='86639',
	key='ead87dfcb6bc713491cc',
	secret='90d77f611808f4f95eeb'
)

userlist = {}

import controller