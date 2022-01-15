from distutils.core import setup

import sawhorse


setup(
    name='django-sawhorse',
    version=sawhorse.__version__,
    author='James Lecker Jr',
    author_email='james@jameslecker.com',
    url='https://github.com/jlecker/django-sawhorse',
    description='An installable Django project to facilitate the development of pluggable apps.',
    packages=['sawhorse'],
    scripts=['sawhorse-manage.py'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
