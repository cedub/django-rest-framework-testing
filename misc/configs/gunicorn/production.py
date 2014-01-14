SITE = 'sbpt_leaderboard'

command = '/opt/{0}/bin/gunicorn'.format(SITE)
pythonpath = '/opt/{0}/{0}'.format(SITE)
bind = '127.0.0.1:8002'

preload_app = True
workers = 6
