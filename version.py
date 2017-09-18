import sys
print(sys.version)
import cv2
print(cv2.__version__)

from pip.utils import get_installed_distributions

skips = ['setuptools', 'pip', 'distribute', 'python', 'wsgiref']
for dist in get_installed_distributions(local_only=True, skip=skips):
    print(dist.project_name, dist.version)

