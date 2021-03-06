from distutils.core import setup

setup(
    name='django-quoteme',
    version='0.2',
    description='A reusable app for quotes and testimonials.',
    author='Kevin Fricovsky',
    author_email='kfricovsky@gmail.com',
    url='http://github.com/montylounge/django-quoteme/tree/master',
    packages=[
        'quoteme',
        'quoteme.templatetags'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)