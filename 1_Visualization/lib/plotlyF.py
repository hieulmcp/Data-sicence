import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# Load file dữ liệu
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def piechart(groupby1, values, labels, data, colors = ["maroon", "black", "orange"], hoverinfo="label+percent", textinfo="value"):
    dff = data.groupby(groupby1)[values].sum().reset_index()
    labels = dff[labels]
    values = dff[values]
    colors = colors
    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hoverinfo=hoverinfo,
                textinfo=textinfo,
            )
        ]
    )
    fig.update_traces(marker=dict(colors=colors))
    return fig.show()




def donut(groupby1, values, names, data, hole=0.2):
    dff = data.groupby(groupby1)[values].sum().reset_index()
    fig = px.pie(
        dff,
        hole=hole,
        values=values,
        names=names,
        color_discrete_sequence=px.colors.sequential.Aggrnyl,
    )
    return fig.show()


def scatter(x, y, z, data, color, size, category_orders, width=900, height=600):
    fig = px.scatter(
        data,
        x=x,
        y=y,
        color= color,
        size=size,
        hover_data=[z],
        width=width,
        height=height,
        color_discrete_sequence=px.colors.sequential.Agsunset,
        category_orders= category_orders,
    )
    return fig.show()



def scatter_columns(x, y, z, facet_col, data, color, category_orders, width=900, height=600):
    fig = px.scatter(
        data,
        x=x,
        y=y,
        color=color,
        size=y,
        hover_data=[z],
        facet_col=facet_col,
        width=width,
        height=height,
        color_discrete_sequence=px.colors.sequential.algae,
        category_orders=category_orders,
    )
    return fig.show()



def line(groupby, z, names, data, width=1000, line_color="maroon"):
    dff = data.groupby(groupby)[z].count().reset_index()
    dff.columns = names
    fig = px.line(dff, 
    x=names[0], 
    y=names[1], 
    width=width)
    fig.update_traces(line_color=line_color)
    return fig.show()


def bar(groupby, x, y, z, title, data, width=900, height=700, line_color="maroon"):
    dff = data.groupby(groupby)[z].sum().reset_index()
    fig = px.bar(
        dff,
        x=x,
        y=y,
        title= title,
        width=width,
        height=height,
        color=x,
        color_discrete_sequence=px.colors.qualitative.G10,
    )
    return fig.show()


def stacked_bar(groupby1, groupby2, y, title, data, width=900, height=700):
    dff = (
        data.groupby([groupby1, groupby2])[y].sum().reset_index()
    )
    fig = px.bar(
        dff,
        x=groupby1,
        y=y,
        title=title,
        color=groupby2,
        color_discrete_sequence=px.colors.qualitative.D3,
        width=width,
        height=height,
    )
    return fig.show()


def animate(x , y, color, data, hover_data, category_orders, key, width=900, height=700, size_max=40):
    fig = px.scatter(
        data,
        x=x,
        y=y,
        color=color,
        animation_frame=key,
        size=y,
        size_max=size_max,
        hover_data=[hover_data],
        width=width,
        height=height,
        color_discrete_sequence=px.colors.sequential.Agsunset,
        category_orders=category_orders,
    )
    return fig.show()


def subplot(groupby , y, data, color1="SkyBlue", color2="red",width=900, height=700, size_max=40):
    dff = data.groupby(groupby)[y].sum().reset_index()
    fig = make_subplots(rows=1, cols=2)
    fig.add_trace(
        go.Bar(
            x=dff[groupby], 
            y=dff[y], 
            marker=dict(color=color1)
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Bar(x=dff[groupby], y=dff[y], marker=dict(color=color2)),
        row=1,
        col=2,
    )
    return fig.show()

