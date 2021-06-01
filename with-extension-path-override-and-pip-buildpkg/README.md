Only fails on `core20`.

Build fails to install the project's python files:

```plain
Building my-part 
+ snapcraftctl build
+ python3 -m venv /root/parts/my-part/install
+ SNAPCRAFT_PYTHON_VENV_INTERP_PATH=/root/parts/my-part/install/bin/python3
+ pip install -U pip setuptools wheel
Collecting pip
  Downloading pip-21.1.2-py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 5.1 MB/s 
Collecting setuptools
  Downloading setuptools-57.0.0-py3-none-any.whl (821 kB)
     |████████████████████████████████| 821 kB 31.3 MB/s 
Collecting wheel
  Downloading wheel-0.36.2-py2.py3-none-any.whl (35 kB)
Installing collected packages: pip, setuptools, wheel
  Attempting uninstall: pip
    Found existing installation: pip 20.0.2
    Not uninstalling pip at /usr/lib/python3/dist-packages, outside environment /usr
    Can't uninstall 'pip'. No files were found to uninstall.
  Attempting uninstall: setuptools
    Found existing installation: setuptools 45.2.0
    Not uninstalling setuptools at /usr/lib/python3/dist-packages, outside environment /usr
    Can't uninstall 'setuptools'. No files were found to uninstall.
  Attempting uninstall: wheel
    Found existing installation: wheel 0.34.2
    Not uninstalling wheel at /usr/lib/python3/dist-packages, outside environment /usr
    Can't uninstall 'wheel'. No files were found to uninstall.
Successfully installed pip-21.1.2 setuptools-57.0.0 wheel-0.36.2
+ pip install -U -r requirements.txt
+ '[' -f setup.py ']'
+ pip install -U .
Processing /root/parts/my-part/build
Building wheels for collected packages: test-python
  Building wheel for test-python (setup.py) ... done
  Created wheel for test-python: filename=test_python-0.1-py3-none-any.whl size=1627 sha256=5ec028aeda8c50c344643c0d28f70c4959f1fd5cefd2e4400f6fc620e08ca863
  Stored in directory: /tmp/pip-ephem-wheel-cache-ca3r2gne/wheels/46/f6/fc/6368727ea9c1d1a43260f9cadc0ddcee3986759a04e0bac238
Successfully built test-python
Installing collected packages: test-python
Successfully installed test-python-0.1
+ xargs -0 sed -i '1 s|^#\!/root/parts/my-part/install/bin/python3.*$|#\!/usr/bin/env python3|'
+ find /root/parts/my-part/install -type f -executable -print0
++ determine_link_target
+++ set +o +x
+++ grep xtrace
++ opts_state='set -o xtrace'
+++ dirname /root/parts/my-part/install/bin/python3
++ interp_dir=/root/parts/my-part/install/bin
+++ which python3
++ python_path=/usr/bin/python3
+++ readlink -e /usr/bin/python3
++ python_path=/usr/bin/python3.8
++ for dir in "${SNAPCRAFT_PART_INSTALL}" "${SNAPCRAFT_STAGE}"
++ echo /usr/bin/python3.8
++ grep -q /root/parts/my-part/install
++ for dir in "${SNAPCRAFT_PART_INSTALL}" "${SNAPCRAFT_STAGE}"
++ echo /usr/bin/python3.8
++ grep -q /root/stage
++ echo /usr/bin/python3.8
++ eval 'set -o xtrace'
+++ set -o xtrace
+ python_path=/usr/bin/python3.8
+ ln -sf /usr/bin/python3.8 /root/parts/my-part/install/bin/python3
Staging gnome-3-38-extension 
+ snapcraftctl stage
Staging my-part 
+ snapcraftctl stage
Priming gnome-3-38-extension 
+ snapcraftctl prime
Priming my-part 
+ snapcraftctl prime
Failed to generate snap metadata: The specified command 'bin/test-python' defined in the app 'test-python' does not exist.
Ensure that 'bin/test-python' is installed with the correct path.
```