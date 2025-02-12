from setuptools import find_packages, setup

package_name = 'motion_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kkcmaestro',
    maintainer_email='kkcmaestro@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'Leader_node = motion_control.Leader_motion:main',
            'Chaser_node = motion_control.ChaserBot:main'
        ],
    },
)
