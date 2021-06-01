Only fails on `core20` with `gnome-3-38`. Fails with:

```plain
Building my-part 
+ snapcraftctl build
+ python3 -m venv /root/parts/my-part/install
+ SNAPCRAFT_PYTHON_VENV_INTERP_PATH=/root/parts/my-part/install/bin/python3
+ pip install -U pip setuptools wheel
Traceback (most recent call last):
  File "/snap/gnome-3-38-2004-sdk/current/usr/bin/pip", line 6, in <module>
    from pkg_resources import load_entry_point
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 3254, in <module>
    def _initialize_master_working_set():
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 3237, in _call_aside
    f(*args, **kwargs)
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 3266, in _initialize_master_working_set
    working_set = WorkingSet._build_master()
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 584, in _build_master
    ws.require(__requires__)
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 901, in require
    needed = self.resolve(parse_requirements(requirements))
  File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 787, in resolve
    raise DistributionNotFound(req, requirers)
pkg_resources.DistributionNotFound: The 'pip==20.0.2' distribution was not found and is required by the application
Failed to build 'my-part'.
```