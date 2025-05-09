from setuptools import setup
setup(
  name = 'btalignment',
  packages = ['btalignment'],
  version = '1.0',
  description = 'This computes the 3d pose of cameras and calibration boards.',
  author = 'Mike Smith',
  author_email = 'm.t.smith@sheffield.ac.uk',
  url = 'https://github.com/SheffieldMLtracking/btalignment.git',
  download_url = 'https://github.com/SheffieldMLtracking/btalignment.git',
  keywords = ['3d','alignment','calibration','cameras','pose','position'],
  classifiers = [],
  install_requires=['numpy','pylibdmtx @ git+https://github.com/SheffieldMLtracking/pylibdmtx'],
  scripts=['bin/btalignment'],
)
