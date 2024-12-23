import numpy as np
import plotly.express as px


def plot_path(path: np.array) -> None:
    fig = px.line(path)
    fig.show()