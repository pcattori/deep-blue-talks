from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='deep-blue-talks',
      version='0.1',
      description='bestow speech unto chess engines',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.7',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ]
      keywords='deep blue talks chess pedro cattori',
      url='https://github.com/pcattori/deep-blue-talks',
      author='Pedro Cattori',
      author_email='pcattori@gmail.com',
      license='MIT',
      packages=['deep-blue-talks'],
      install_requires=[
          'python-chess',
      ],
      include_package_data=True,
      zip_safe=False)
