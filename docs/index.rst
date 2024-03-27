.. eWaterCycle-HBV documentation master file, created by
   sphinx-quickstart on Thu Mar  7 10:34:21 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to an example of parallelisation in eWaterCycle
===========================================

Hydrolgical model can take long to run due to their complexity. They are inherently sequential as the as the next time step is controlled by the previous one. 
In some cases you want to run multiple models. To compare their performance or to apply data assimilation for example. If you want to speed this up you can run models in parallel.
The `ParallelisationSleep` model aims to add a testing example without having to specify parameters & forcing, whilst still acting like a model would. 


Installation
------------

Install this package alongside your eWaterCycle installation

.. code:: console

   pip install git+https://github.com/Daafip/ewatercycle-test-parallelisation@main

Then a example model to test parallelisation becomes available as one of the eWaterCycle models

.. code:: python

   from ewatercycle.models import ParallelisationSleep


All this does is wait when `.update()`` is called. Good for testing. 

Implementing your own model
---------------------------

For more information on how this plugin works, and on how to implement
your own model see the `plugin
guide <https://github.com/eWaterCycle/ewatercycle-leakybucket/blob/main/plugin_guide.md>`__


License
-------

This is a ``ewatercycle-plugin`` & thus this is distributed under the
same terms as the template: the
`Apache-2.0 <https://spdx.org/licenses/Apache-2.0.html>`__ license.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   example_parallelisation

