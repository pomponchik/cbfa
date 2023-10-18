from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf8') as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name='cbfa',
    version='0.0.1',
    author='Evgeniy Blinov',
    author_email='zheni-b@yandex.ru',
    description='Class-based views for the FastAPI',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/pomponchik/cbfa',
    packages=find_packages(exclude='tests'),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
)
