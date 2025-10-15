# Copyright 2020-2024 The Emukit Authors. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# Copyright 2018-2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0


from itertools import cycle
from typing import List

import matplotlib.pyplot as plt
import numpy as np

from .benchmark_result import BenchmarkResult


class BenchmarkPlot:
    """Creates plots comparing results from different loops.

    Matplotlib is now a mandatory dependency; this class always has plotting support.
    """

    def __init__(
        self,
        benchmark_results: BenchmarkResult,
        loop_colours: List = None,
        loop_line_styles: List[str] = None,
        x_axis_metric_name: str = None,
        metrics_to_plot: List[str] = None,
    ):
        self.benchmark_results = benchmark_results
        self.loop_names = benchmark_results.loop_names

        if loop_colours is None:
            self.loop_colours = _get_default_colours()
        else:
            self.loop_colours = loop_colours

        if loop_line_styles is None:
            self.loop_line_styles = ["-"]
        else:
            self.loop_line_styles = loop_line_styles

        if metrics_to_plot is None:
            self.metrics_to_plot = self.benchmark_results.metric_names
        else:
            for metric_name in metrics_to_plot:
                if metric_name not in self.benchmark_results.metric_names:
                    raise ValueError(metric_name + " not found in saved metrics from benchmark results.")
            self.metrics_to_plot = metrics_to_plot

        if x_axis_metric_name is not None:
            if x_axis_metric_name not in self.metrics_to_plot:
                raise ValueError("x_axis " + x_axis_metric_name + " is not a valid metric name")
            self.metrics_to_plot.remove(x_axis_metric_name)

        self.x_label = "Iteration" if x_axis_metric_name is None else x_axis_metric_name
        self.fig_handle = None
        self.x_axis = x_axis_metric_name

    def make_plot(self, log_y: bool = False) -> None:
        n_metrics = len(self.metrics_to_plot)
        self.fig_handle, _ = plt.subplots(n_metrics, 1)

        for i, metric_name in enumerate(self.metrics_to_plot):
            plt.subplot(n_metrics, 1, i + 1)
            plt.title(metric_name)

            colours = cycle(self.loop_colours)
            line_styles = cycle(self.loop_line_styles)
            min_x = np.inf
            max_x = -np.inf

            legend_handles = []
            for loop_name in self.loop_names:
                metric = self.benchmark_results.extract_metric_as_array(loop_name, metric_name)
                colour = next(colours)
                line_style = next(line_styles)
                mean, std = _get_metric_stats(metric)
                if self.x_axis is not None:
                    x = np.mean(self.benchmark_results.extract_metric_as_array(loop_name, self.x_axis), axis=0)
                else:
                    x = np.arange(0, mean.shape[0])
                min_x = np.min([np.min(x), min_x])
                max_x = np.max([np.max(x), max_x])
                mean_plt = plt.plot(x, mean, color=colour, linestyle=line_style)
                plt.xlabel(self.x_label)
                fill_plt = plt.fill_between(x, mean - std, mean + std, alpha=0.2, color=colour)
                legend_handles.append((fill_plt, mean_plt[0]))
            plt.legend(legend_handles, self.loop_names)
            plt.tight_layout()
            plt.xlim(min_x, max_x)
            if log_y:
                plt.yscale("log")

    def save_plot(self, file_name: str) -> None:
        if self.fig_handle is None:
            raise ValueError("Please call make_plot before saving to file")
        self.fig_handle.savefig(file_name)

def _get_metric_stats(metric):
    return metric.mean(axis=0), metric.std(axis=0)

def _get_default_colours():
    return plt.rcParams["axes.prop_cycle"].by_key()["color"]