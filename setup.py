from distutils.core import setup

setup(
    name='contrastive_learning_for_pcap',
    version='0.1',
    license='MIT',
    author="rotem_bar",
    author_email='rotembaruch@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/rotembaruch/contrastive_learning_for_pcap',
    keywords='clfp',
    install_requires=[
          'transformers',
          'scipy',
          'datasets',
          'pandas',
          'scikit-learn',
          'prettytable',
          'gradio',
          'torch',
          'scapy',
          'scikit-learn',
          'setuptools',
      ],

)