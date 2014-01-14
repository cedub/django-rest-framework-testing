SITE = 'spbt_leaderboard'

command = '/opt/{0}/bin/gunicorn'.format(SITE)
pythonpath = '/opt/{0}/{0}'.format(SITE)

preload_app = True
workers = 1
