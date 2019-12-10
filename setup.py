from distutils.core import setup
setup(
  name = 'trash_pandas',         
  packages = [''],   
  version = '0.1',      
  license='GNU General Public License v3.0',        
  description = 'Analytic tool for Pandas DataFrame exploration',   
  author = 'Mifour',                  
  author_email = 'mifour@yopmail.com',      
  url = 'https://github.com/Mifour/trash_pandas',   
  download_url = 'https://github.com/Mifour/trash_pandas/archive/0.1.tar.gz',
  package_dir={'': '.'},    
  keywords = ['PANDAS', 'EXPLORE', 'ANALYTICS'],   
  install_requires=['pandas', 'numpy', 'bashplotlib', 'scipy'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',     
    'Topic :: Scientific/Engineering :: Mathematics',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',   
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
