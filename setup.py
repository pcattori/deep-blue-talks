from setuptools import setup
from glob import glob

setup(name='deep-blue-talks',
      version='0.2',
      description='bestow speech unto chess engines',
      long_description=open('README.md').read(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Games/Entertainment :: Board Games',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='deep blue talks chess pedro cattori',
      url='https://github.com/pcattori/deep-blue-talks',
      author='Pedro Cattori',
      author_email='pcattori@gmail.com',
      license='MIT',
      packages=['kasparobot'],
      package_data={
          'kasparobot' : ['engines/*']
      },
      install_requires=[
          'python-chess',
      ],
      dependency_links=[
          "git+https://github.com/niklasf/python-chess.git@883a491b414ab9c30a2021241ad4d2af2113c868#egg=python-chess"
      ],
      scripts=['bin/deep-blue-talks'],
      include_package_data=True,
      zip_safe=False)
