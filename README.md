# eWaterCycle plugin test parallelisation BMI

This repository contains a BMI model which just sleeps: idea is to test parallelisation in eWatercycle with it.  Adds the ["ParrallelisationSleep" model](https://github.com/Daafip/test-parallelisation-BMI). 

Uses the [Basic Model Interface (BMI)](https://bmi.readthedocs.io/).


## Installation

Install this package alongside your eWaterCycle installation

```console
pip install ewatercycle-parallelisation-sleep
```

Then ParallelisationSleep becomes available as one of the eWaterCycle models

```python
from ewatercycle.models import Then ParallelisationSleep becomes available as one of the eWaterCycle models

```

## Implementing your own model

For more information on how this plugin works, and on how to implement your own model see the [plugin guide](https://github.com/eWaterCycle/ewatercycle-leakybucket/blob/main/plugin_guide.md)

## License

`ewatercycle-plugin` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
