
# Sample Python Package

https://vf-commonit.visualstudio.com/VDP-BAM-Training/_git/python-package-sample

To demonstrate:

1. How to structure your own Python package
2. How to make use of the \_\_init__.py
3. How to find and import your modules
4. How **editable** installs will help you
5. Where to configure logging

## Sample Program Flow

1. script
2. main_function
3. function_1
4. helper
5. function_2
6. helper

## Sample Folder Structure

- python-package-sample
    - script.py
    - setup.py
    - package
        - \_\_init__.py
        - module
            - main_function( )
        - subpackage
            - \_\_init__.py
            - submodule_1.py
                - function_1( )
            - submodule_2.py
                - function_2( )
        - helppackage
            - \_\_init__.py
            - helpmodule
                - helper( )

## What to do

1. Clone the repository
2. Run script.py step-by-step in the debugger
3. Observe the different logs from code declaration and code execution
4. Compare the 2 methods of calling _helper_ in function_1 and function_2
5. Try to run the main module in script-mode
6. Check the first PATH element in the debugger with  
```import sys; sys.path[0]```
7. Make an editable install when you are inside the package-folder with  
```pip install -e .```
8. Check the installation with  
```pip show package-sample```
9. Run the main module in script-mode again
10. Add ```logging.basicConfig(level=50)``` to the top of
    the module code and run the module again.
