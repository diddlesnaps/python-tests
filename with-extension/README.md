Only fails on `core20` with `gnome-3-38`. Fails with:

```plain
Building my-part 
+ snapcraftctl build
+ python3 -m venv /root/parts/my-part/install
+ SNAPCRAFT_PYTHON_VENV_INTERP_PATH=/root/parts/my-part/install/bin/python3
+ pip install -U pip setuptools wheel
Collecting pip
  Downloading pip-21.1.2-py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 3.7 MB/s 
Collecting setuptools
  Downloading setuptools-57.0.0-py3-none-any.whl (821 kB)
     |████████████████████████████████| 821 kB 76.6 MB/s 
Collecting wheel
  Downloading wheel-0.36.2-py2.py3-none-any.whl (35 kB)
Installing collected packages: pip, setuptools, wheel
  Attempting uninstall: pip
    Found existing installation: pip 20.0.2
    Uninstalling pip-20.0.2:
ERROR: Could not install packages due to an EnvironmentError: [Errno 30] Read-only file system: '__init__.py'

Failed to build 'my-part'.
```