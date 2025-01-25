from setuptools import setup

setup(
    name='BeginnerNN',
    version='1.0.0',
    description='A Python library to simplify creating neural networks for beginners, using PyTorch and NumPy to make it easy to use.',
    py_modules=['BeginnerNN'],
    package_dir={'': 'src'},
    author='Zian Conradie',
    author_email='zianconradie@gmail.com',
    url='https://github.com/yourusername/BeginnerNN',  # Add your GitHub URL once created
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7, <=3.10',
    install_requires=[
        'torch',
        'numpy',
    ],
)
