from setuptools import setup, find_packages


setup(
    name='django-extended-filters',
    version='0.5.8',
    url='https://bitbucket.org/legion_an/django-extended-filters',
    packages=find_packages(),
    include_package_data=True,
    license='',
    author='legion',
    author_email='legion.andrey.89@gmail.com',
    description='Add checkbox, daterange, tree-descendants and autocomplete filters in django admin',
    keywords=[
        'django admin',
        'django date range',
        'django checkbox filter',
        'django tree descendants filter'
        'django admin filter'
        'django admin autocomplete filter'
    ],
    install_requires=[
        "django",
    ],
)
