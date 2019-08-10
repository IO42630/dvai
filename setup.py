from setuptools import find_packages, setup

setup(name = 'dvai',
      version = '0.0.1',
      description = 'Authentication and Authorization for Constrained Environments',
      url = 'https://github.com/IO4263066/dvai',
      author = 'Ivan Olexyn',
      author_email = 'ivan@olexyn.com',
      packages = find_packages(),
      install_requires = [
          'scipy>=1.3.0'
          'halo>=0.0.26'
          'webrtcvad>=2.0.10'
          'pyaudio>=0.2.11'
          'numpy>=1.16.4'
          'deepspeech>=0.5.1'
          ],
      zip_safe = False)
