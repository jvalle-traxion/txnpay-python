from setuptools import setup

setup(
    name = 'txnpay',
    packages = ['txnpay'],
    version = '0.1',
    license='bsd-3-clause',
    description = 'An official Python SDK of TraxionPay.',
    author = 'jvalle',
    author_email = 'jvalle@traxiontech.net',
    url = 'https://github.com/jvalle-traxion/txnpay-python',
    download_url = '',
    keywords = ['payment', 'merchant', 'cash'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)