import os
import sys
from distutils.core import setup

sys.path.insert(0, os.path.dirname(__file__))
import stripe

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

setup(name='stripe',
      version=stripe.VERSION,
      description='Stripe python bindings',
      author='Stripe',
      author_email='support@stripe.com',
      url='https://stripe.com/',
      packages=['stripe'],
      package_data={'stripe' : ['data/ca-certificates.crt']},
      install_requires=['simplejson', 'pycurl']
)
