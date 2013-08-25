from setuptools import setup, find_packages

setup(name='financial_fundamentals',
      version='1',
      description='Caching for financial metrics.',
      author='Andrew Kittredge',
      author_email='andrewlkittredge@gmail.com',
      license='Apache 2.0',
      packages=find_packages(),
      classifiers=[
	'Development Status :: 4 - Beta',
	'License :: OSI Approved :: Apache Software License',
	'Natural Language :: English',
	'Programming Language :: Python',
	'Programming Language :: Python :: 2.7',
	'Operating Audience :: Science/Research',
	'Intended Audience :: Science/Research',
	'Topic :: Office/Business :: Financial',
     	],	
      install_requires=[
	'numpy',
	'pytz',
	'requests_cache',
	'requests',
	'BeautifulSoup',
	'pymongo',
	'mock',
	'pandas',
	],
      url='https://github.com/andrewkittredge/financial_fundamentals',
)
