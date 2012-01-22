nose2-cov
=========

This plugin produces coverage reports.  It also supports coverage of subprocesses.

All features offered by the coverage package should be available, either through nose2-cov or
through coverage's config file.


Installation
------------

Install with pip::

    pip install nose2-cov

.. NOTE::

    Ensure you use pip instead of easy_install as the latter does not correctly install the
    init_cov_core.pth file needed for subprocess measurement.


Uninstallation
--------------

Uninstall with pip::

    pip uninstall nose2-cov
    pip uninstall cov-core

.. NOTE::

    Ensure that you manually delete the init_cov_core.pth file in your site-packages directory.

    This file starts coverage collection of subprocesses if appropriate during site initialisation
    at python startup.


Usage
-----

The following will report on the combined coverage of the main process and all of it's subprocesses::

    nose2 --with-cov testfoo

Shows a terminal report::

    ---------- coverage: platform linux2, python 2.7.1-final-0 -----------
    Name      Stmts   Miss  Cover
    -----------------------------
    testfoo      17      9    47%


Reporting
---------

It is possible to generate any combination of the reports for a single test run.

The available reports are terminal (with or without missing line numbers shown), HTML, XML and
annotated source code.

The terminal report without line numbers (default)::

    nose2 --with-cov --cov-report term testfoo

    ---------- coverage: platform linux2, python 2.7.1-final-0 -----------
    Name      Stmts   Miss  Cover
    -----------------------------
    testfoo      17      9    47%


The terminal report with line numbers::

    nose2 --with-cov --cov-report term-missing testfoo

    ---------- coverage: platform linux2, python 2.7.1-final-0 -----------
    Name      Stmts   Miss  Cover   Missing
    ---------------------------------------
    testfoo      17      9    47%   1-6, 9, 11, 13, 17, 19


The remaining three reports output to files (useful for when the output is going to a continuous
integration server)::

    nose2 --with-cov --cov-report html --cov-report xml --cov-report annotate testfoo


Coverage Data File
------------------

The data file is erased at the beginning of testing to ensure clean data for each test run.

The data file is left at the end of testing so that it is possible to use normal coverage tools to
examine it.


Limitations
-----------

For subprocess measurement environment variables must make it from the main process to the
subprocess.  The python used by the subprocess must have nose2-cov installed.  The subprocess must
do normal site initialisation so that the environment variables can be detected and coverage
started.


Acknowledgements
----------------

Whilst this plugin has been built fresh from the ground up it has been influenced by the work done
on pytest-coverage (Ross Lawley, James Mills, Holger Krekel) and nose-cover (Jason Pellerin) which are
other coverage plugins.

Ned Batchelder for coverage and its ability to combine the coverage results of parallel runs.

Holger Krekel for pytest with its distributed testing support.

Jason Pellerin for nose.

Michael Foord for unittest2.

No doubt others have contributed to these tools as well.
