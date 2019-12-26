
# How to work with Python packages

1. How to structure your project
2. How Python finds and imports your modules
3. How **editable** installs will help you
4. The difference between absolute and relative imports
5. How to make use of the \_\_init__.py
6. How to configure logging  
<br/>

---

## Sample Program Flow  
https://vf-commonit.visualstudio.com/VDP-BAM-Training/_git/python-package-sample

1. script
2. function
3. func1
4. helper
5. func2
6. helper

## Sample Folder Structure

- repo-folder
    - script.py
    - setup.py
    - package
        - \_\_init__.py
        - module.py
            - function( )
        - subpkg
            - \_\_init__.py
            - submod1.py
                - func1( )
            - submod2.py
                - func2( )
        - helppkg
            - \_\_init__.py
            - helpmod
                - helper( )  
<br/>

---

## Absolute Imports (from anywhere)

1. **import** package.subpkg.submod1.func1  
   y = package.subpkg.submod1.func1()  

2. **import** package.subpkg.submod1.func1 **as** func1  
   y = func1()

3. **from** package.subpkg.submod1 **import** func1  
   y = func1()

4. **from** package.subpkg **import** submod1 **as** s1  
   y = s1.func1()

## Relative Imports (not from *\_\_main__*)

5. In module.py: **from** .subpkg.submod1 **import** func1

6. In submod1.py: **from** .submod2 **import** func2

7. In submod1.py: **from** ..helppkg.helpmod **import** helper

<br/>

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
9. Check the installation with  
```pip show package-sample```.
10. Run the main module in script-mode again.
11. Add ```logging.basicConfig(level=0)``` to the top of
    the module code and run the module again.

## Take-aways

1. To import a module it's containing folder has to be either 
pip-installed (linked) into the Lib/site-packages or on the SYSTEM-PATH. 
2. Prefer _absolute imports_ starting with the main package over _relative imports_.
3. The \_\_init__.py can be used for convenience imports.
4. Don't put `logging.basicConfig()` into the module code since it is
executed once only.
