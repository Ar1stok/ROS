from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'time_tf2_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ar1sto',
    maintainer_email='ar1sto@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'time_tf2_broadcaster = time_tf2_py.time_tf2_broadcaster:main',
            'time_tf2_listener = time_tf2_py.time_tf2_listener:main',
        ],
    },
)
