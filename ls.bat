::https://github.com/AmitNutman/MyShellProj

::python = so we can run a python file
:: "" = so it can have spaces - allows it to have spaces
:: %0 = the path of the current bat file - doesn't take it all -just the things (d, p)
:: ~ = removes quotes
:: d = take the Drive (C:)
:: p = take the path (\MyShellProj\)
::ls.py = the python file to run
:: %* = all params that the bat got

:: takes the path that the bat is in, connects it to the python file name, runs it with the params it got
python "%~dp0ls.py" %*


