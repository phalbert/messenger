"""Default configuration

Use env var to override
"""
from environs import Env

env = Env()
env.read_env()

SENDGRID_API_KEY = env.str('SENDGRID_API_KEY', default='SENDGRID_API_KEY')

