from setuptools import find_packages, setup

package_name = 'robot_echo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
   data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch', ['launch/echo.launch.py']),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amira',
    maintainer_email='bengrabamira@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'cmd_parser = robot_echo.cmd_parser:main',
        'logger_node = robot_echo.logger_node:main',
        'history_service = robot_echo.history_service:main',
    ],
},
)
