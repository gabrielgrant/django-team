from setuptools import setup

setup(
    name='django-team',
    version='0.1.0dev',
    author='Gabriel Grant',
    packages=['team',],
    license='LGPL',
    long_description=open('README').read(),
    install_requires=[
        'PIL',
        'django-ckeditor',
        'django-html-field',
        'django-static-filtered-images',
    ],
    dependency_links = [
    	'http://github.com/gabrielgrant/django-ckeditor/tarball/master#egg=django-ckeditor',
        'http://github.com/gabrielgrant/django-html-field/tarball/master#egg=django-html-field',
        'http://github.com/gabrielgrant/django-static-filtered-images/tarball/master#egg=django-static-filtered-images',
    ]
)

