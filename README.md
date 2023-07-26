# monorepo-demo-install-requires

Repository demonstrating how to create a Python mono-repo that allows local dependencies to be installed in editable mode. This strategy uses a setup.py file with PIP to install the local libraries. There is no extra tooling other than a `local_requirement` helper function that forces PIP to install local dependencies.

# Demo

Install `lib-a` in editable mode, which will in turn install `lib-b` and `lib-c` in editable mode.

```
cd common-libraries/lib-a/
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

You can see that all 3 libs are installed like so:

```
python -c 'from lib_a import func_a ; func_a()'
python -c 'from lib_b import func_b ; func_b()'
python -c 'from lib_c import func_c ; func_c()'
```

This should print:

```
lib-a, func a
lib-b, func b
lib-c, func c
```

If you edit `lib-c`, its code update is reflected immediately in the venv.

```
echo "    print('edited')" >> ../lib-c/lib_c.py
```

Now check the lib-c code:
```
python -c 'from lib_c import func_c ; func_c()'
```

Should output:

```
lib-c, func c
edited
```

This demonstrates that the local dependencies are installed in editable mode in the venv.
