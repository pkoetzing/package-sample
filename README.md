
# How to work with Python packages

[Video-Stream](https://web.microsoftstream.com/video/24365309-1605-47ef-a9ad-0e76630295cd)

1. How to **structure** your project
2. How Python **finds** and **imports** your modules
3. How **editable installs** will help you
4. The difference between **absolute** and **relative** imports
5. How to make use of the **\_\_init__.py**

---

## Sample Program Flow

1. script
2. function
3. func1
4. helper
5. func2
6. helper

---

## Sample Folder Structure

- repo-folder
  - script.py
  - setup.py
  - package
    - \_\_init__.py
    - module.py
      - function( )
    - subpkg
      - submod1.py
        - func1( )
        - submod2.py
          - func2( )
    - helppkg
      - helpmod
        - helper( )  

---

## Import template

**FROM** \<package>\<module> **IMPORT** \<package>\<module>\<function> **AS** \<alias>

## Absolute Imports (from anywhere)

1. **import** package.subpkg.submod1.func1  
   y = package.subpkg.submod1.func1()  

1. **import** package.subpkg.submod1.func1 **as** func1  
   y = func1()

1. **from** package.subpkg.submod1 **import** func1  
   y = func1()

1. **from** package.subpkg **import** submod1 **as** s1  
   y = s1.func1()

## Relative Imports (not from *\_\_main__*)

1. In module.py: **from** .subpkg.submod1 **import** func1

1. In submod1.py: **from** .submod2 **import** func2

1. In submod1.py: **from** ..helppkg.helpmod **import** helper

---

## What to do

1. Run script.py step-by-step in the debugger.
2. Try out the different ways to import the package.
3. Compare the 2 methods of calling _helper_ in func1 and func2.
4. Compare absolute and relative import in module.py and submod1.py.
5. Observe the logs from code declaration and code execution.
6. Try to run the main module in script-mode.
7. Check the first PATH element in the debugger with  
```import sys; sys.path[0]```.
8. Make an editable install when you are inside the repo-folder with  
```pip install -e .```.  
(```conda develop .``` does a similar thing)
9. Check the installation with  
```pip show package-sample```.
10. Run the main module in script-mode again.

## Take-aways

1. To import a module it's containing folder has to on sys.path, which includes:
    1. The top-level script folder
    2. PYTHONPATH
    3. Lib/site-packages (```pip install --editable```)
2. Prefer _absolute imports_ starting with the main package over _relative imports_.
3. The \_\_init__.py can be used for convenience imports.
