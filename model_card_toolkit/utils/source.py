"""Sources to extract quantitative information for model cards.

These classes are inputs to the ModelCardToolkit, providing paths to data to
populate a ModelCard.
"""

import dataclasses
from typing import List, Optional, Text


@dataclasses.dataclass
class TfmaSource:
  """Source to extract TFMA eval result data for a model card.

  Attributes:
    paths: The paths to the eval result output from TensorFlow Model Analysis or
      TFX Evaluator.
    file_format: Optional file extension to filter eval result files
      by.
    metrics_include: The list of metric names to include in the model card. By
      default, all metrics are included. Mutually exclusive with
      metrics_exclude.
    metrics_exclude: The list of metric names to exclude in the model card. By
      default, no metrics are excluded. Mutually exclusive with
      metrics_include.
  """
  paths: List[Text] = dataclasses.field(default_factory=list)
  file_format: Optional[Text] = ''
  metrics_include: List[Text] = dataclasses.field(default_factory=list)
  metrics_exclude: List[Text] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class TfdvSource:
  """Sources to extract TFDV data for a model card.

  Attributes:
    dataset_statistics_paths: The paths to the output from TensorFlow Data
      Validation or TFX ExampleValidator.
  """
  dataset_statistics_paths: List[Text] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class Source:
  """Sources to extract data for a model card.

  Attributes:
    tfma: The source info for TFMA.
    tfdv: The source info for TFDV.
    dataset_statistics_paths: The paths to the output from TensorFlow Data
      Validation or TFX ExampleValidator.
  """
  tfma: TfmaSource = dataclasses.field(default_factory=TfmaSource)
  tfdv: TfdvSource = dataclasses.field(default_factory=TfdvSource)
