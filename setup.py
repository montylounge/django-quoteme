from distutils.core import setup

setup(
    name='django-quoteme',
    version='0.1',
    description='A reusable app for quotes and testimonials.',
    author='Kevin Fricovsky',
    author_email='kfricovsky@gmail.com',
    url='http://github.com/montylounge/django-quoteme/tree/master',
    packages=['quoteme', 'quoteme.templatetags'],
    package_data={'quoteme': ['fixtures/*.json', 'templates/quoteme/*.*',
                              'templates/quoteme/includes/*.*']}
)