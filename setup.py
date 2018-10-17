try:
    from pip._internal.req import parse_requirements
except ImportError:
    from pip.req import parse_requirements
    
from setuptools import setup
import uuid

setup(
        name='ksim868',
        version='0.0.1',
        modules=['ksim868'],
        scripts=['ksim868.py'],
        url='https://github.com/Koodt/sim868',
        license='MIT License',
        author='Koodt',
        author_email='k0dt@k0dt.ru',
        description='SIM868 based TCP server and client.',
        install_requires= [str(ir.req) for ir in parse_requirements('requirements.txt', session=uuid.uuid1())]
)
