"""eWaterCycle wrapper for the LeakyBucket model."""
import json
from collections.abc import ItemsView
from pathlib import Path
from typing import Any

from ewatercycle.base.model import ContainerizedModel, eWaterCycleModel
from ewatercycle.container import ContainerImage


class ParallelisationSleepMethods(eWaterCycleModel):
    """The eWatercycle Sleep model.
    
    Setup args:
        sleepiness: The length of sleep in seconds.
    """
    forcing: None  # The model requires no forcing.
    parameter_set: None  # The model has no parameter set.

    _config: dict = {
        "sleepiness": 1,
    }

    def _make_cfg_file(self, **kwargs) -> Path:
        """Write model configuration file."""

        for kwarg in kwargs:  # Write any kwargs to the config.
            self._config[kwarg] = kwargs[kwarg]

        config_file = self._cfg_dir / "sleepy_config.json"

        with config_file.open(mode="w") as f:
            f.write(json.dumps(self._config, indent=4))

        return config_file

    @property
    def parameters(self) -> ItemsView[str, Any]:
        return self._config.items()


class ParallelisationSleep(ContainerizedModel, ParallelisationSleepMethods):
    """The LeakyBucket eWaterCycle model, with the Container Registry docker image."""
    bmi_image: ContainerImage = ContainerImage(
        "ghcr.io/daafip/parallelisation-sleep-grpc4bmi:v0.0.2"
    )
