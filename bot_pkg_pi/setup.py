import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'bot_pkg_pi'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	(os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='x',
    maintainer_email='x@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'cam_pub = bot_pkg_pi.cam_pub:main',
        'motor = bot_pkg_pi.motor:main',
        'lidar = bot_pkg_pi.lidar:main',
        ],
    },
)
