from setuptools import setup
with open('README.txt') as yeet:
    long_description = yeet.read()
    
setup(
   name='Pillow3f',
   version='0.5',
   description='3D graphics library using Pillow',
   author='Robert Bassett',
   author_email='bassett.w.robert@gmail.com',
   packages=['Pillow3f'],  #same as name
   long_description = long_description
)
