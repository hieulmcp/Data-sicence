import pandas as pd
import altair as alt

def load_data(file_dir):
    df = pd.read_csv(file_dir)
    return df


# Viết hàm
def visualize_line(var_year, year, date, df, width=650, height=500):
    df_copy = df.copy()
    df_copy = df_copy[
        (df_copy[var_year] == year[0])
        | (df_copy[var_year] == year[1])
        | (df_copy[var_year] == year[2])
    ]
    df_copy[date] = pd.to_datetime(df_copy[date])
    line = (
        alt.Chart(df_copy)
        .mark_line()
        .encode(x=date , y=date)
        .properties(width=width, height=height)
        .interactive()
    )
    return line

def bar(x, y, df, width=650, height=500,  ascending=False, top=20):
    bar_data = df.sort_values(by=y, ascending=ascending)
    bar_data = bar_data.head(top)
    chart1 = (
            alt.Chart(bar_data)
            .mark_bar()
            .encode(x=alt.X("event:N", sort="-y"), y="sum("+y+")")
            .properties(width=width, height=height)
            .interactive()
        )
    chart2 = (
            alt.Chart(bar_data)
            .mark_bar()
            .encode(x=x, y=y)
            .properties(width=width, height=height)
            .interactive()
        )

    return chart1 | chart2

def scatter(x, y, df, size, color, tooltip, width=650, height=500):
    chart1 = (
            alt.Chart(df)
            .mark_point()
            .encode(
                x=x,
                y=y,
                size=size,
                color=color,
                tooltip=tooltip,
            )
            .properties(width=width, height=height)
        )
    chart2 = (
            alt.Chart(df)
            .mark_point()
            .encode(
                x=x,
                y=y,
                size=size,
                color=color,
                tooltip=tooltip,
            )
            .properties(width=width, height=height)
        )

    return chart1 | chart2

def area_chart(x, y, var_year, year, df, color = "maroon", width=650, height=500, line=True):
    df_copy = df[df[var_year] == year[0]]
    df_copy[x] = pd.to_datetime(df_copy[x])
    chart1 = (
            alt.Chart(df_copy)
            .mark_area(color=color, line=line)
            .encode(x=x, y=y)
            .properties(width=width, height=height)
        )
    
    chart2 = (
            alt.Chart(df_copy)
            .mark_area(color=color)
            .encode(x=x, y=y)
            .properties(width=width, height=height)
        )

    return chart1 | chart2

def scatter_matrix(df, color, row, column, X_="column", Y_="row", width=300, height=300, type="quantitative"):
    chart = (
        alt.Chart(df)
        .mark_circle()
        .encode(
            alt.X(alt.repeat(X_), type=type),
            alt.Y(alt.repeat(Y_), type=type),
            color= color,
        )
        .properties(width=width, height=height)
        .repeat(
            row=row,
            column=column,
        )
        .interactive()
    )
    return chart

def link_scatter(x, y, color, tooltip, df, width=650, height=500, strokeColor="#ea4663", fillColor="#EEEEEE",  padding=10,  orient="top-right", cornerRadius=10):
    chart = (
        alt.Chart(df)
        .mark_point()
        .encode(
            x=x,
            y=y,
            color=color,
            href="url:N",
            tooltip=[tooltip, "url:N"],
        )
        .interactive()
        .properties(width=width, height=height)
        .configure_legend(
            strokeColor=strokeColor,
            fillColor=fillColor,
            padding=padding,
            cornerRadius=cornerRadius,
            orient=orient,
        )
    )
    return chart

def heatmap(x, y, color, tooltip, df, width=650, height=500):
    chart = (
        alt.Chart(df)
        .mark_rect()
        .encode(
            x=x+":O",
            y=y,
            color=color,
            tooltip=tooltip,
        )
        .interactive()
        .properties(width=width, height=height)
    )
    return chart

def horizontal_bar(x, y, df, top=20, width=650, height=500, ascending=False):
    bar_data = df.sort_values(by=x, ascending=ascending)
    bar_data = bar_data.head(top)
    chart = (
        alt.Chart(bar_data)
        .mark_bar()
        .encode(x=x, y=y)
        .properties(width=width, height=height)
        .interactive()
    )
    return chart

def grouped_bar_ngang(day, x, day1, day2, y, df, title, width=650, height=500, ascending=False):
    dff = df[(df[day] == day1) | (df[day] == day2)]
    chart1 = (
            alt.Chart(dff)
            .mark_bar()
            .encode(
                y=y+":O",
                x=alt.X("sum("+x+"):Q", title=title),
                color=y+":N",
                column=day+":N",
            )
            .properties(height=height, width=width)
        )

    return chart1

def grouped_bar_cot(day, x, day1, day2, y, df, title, width=650, height=500, ascending=False):
    dff = df[(df[day] == day1) | (df[day] == day2)]
    chart2 = (
            alt.Chart(dff)
            .mark_bar()
            .encode(
                x=x+":O",
                y=alt.Y("sum("+x+"):Q", title=title),
                color=y+":N",
                column=day+":N",
            )
            .properties(height=height, width=width)
        )

    return chart2

def stacked_bar(color, x, y, df, width=700, height=500):
    chart1 = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                y=y+":O",
                x="sum("+x+")",
                color=color,
                tooltip=["sum("+x+")"],
            )
            .properties(height=height, width=width)
            .interactive()
        )
    chart2 = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                y=y+":O",
                x="sum("+x+")",
                color=color,
                tooltip=["sum("+x+")"],
            )
            .properties(height=height, width=width)
            .interactive()
        )

    return chart1 | chart2

def normalized_chart(color, x, y, df, width=900, height=600, stack="normalize"):
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("mean("+x+")", stack=stack),
            y=y+":O",
            color=color,
            tooltip=["mean("+x+")", color],
        )
        .interactive()
        .properties(width=width, height=height)
    )
    return chart

def text_chart(color, x, y, df, detail, width=700, height=600, stack="normalize"):
    text = (
        alt.Chart(df)
        .mark_text(dx=-16, color=color)
        .encode(
            x=alt.X("sum("+x+"):Q", stack=stack),
            y=y+":O",
            detail=detail,
            text=alt.Text("sum("+x+"):Q", format=".1f"),
        )
    )

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("sum("+x+")", stack=stack),
            y=y+":O",
            color=detail,
            tooltip=["sum("+x+")", detail],
        )
        .interactive()
        .properties(height=height, width=width)
    )

    return text | chart

def boxplot(x, y, df, width=700, height=600):
    chart = (
        alt.Chart(df)
        .mark_boxplot()
        .encode(x=x+":O", y=y)
        .interactive()
        .properties(height=height, width=width)
    )
    return chart

def legend(color, x, y, df, detail, width=700, height=600, stack="normalize",  bind="legend", dx=-16):
    text = (
        alt.Chart(df)
        .mark_text(dx=dx, color=color)
        .encode(
            x=alt.X("sum("+x+"):Q", stack=stack),
            y=y+":O",
            detail=detail,
            text=alt.Text("sum("+x+"):Q", format=".1f"),
        )
    )
    selection = alt.selection_multi(fields=[detail], bind=bind)
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("sum("+x+")", stack=stack),
            y=y+":O",
            opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
            color=detail,
            tooltip=["sum("+x+")", detail],
        )
        .interactive()
        .properties(height=height, width=width)
        .add_selection(selection)
    )
    return chart + text
    
def concatenate(color1, color2, color3, x, y, df, width=450, height=450):
    scatter = (
        alt.Chart(df)
        .mark_point()
        .encode(x=x, y=y+":Q")
        .properties(width=width, height=height)
    )

    chart = alt.concat(
        scatter.encode(color=color1), scatter.encode(color=color2)
    ).resolve_scale(color=color3)
    return chart

def dual_y_axis(x, y, z, v, df, color="#1a9988", titleColor="#1a9988", width=700, height=600):
    base = alt.Chart(df).encode(alt.X("year("+x+"):T"))
    line_A = base.mark_line(color=color).encode(
        alt.Y("average("+y+"):Q", axis=alt.Axis(titleColor=color))
    )
    line_B = base.mark_line(color=color).encode(
        alt.Y("average("+z+"):Q", axis=alt.Axis(titleColor=titleColor))
    )

    chart = (
        alt.layer(line_A, line_B)
        .resolve_scale(y=v)
        .properties(height=height, width=width)
    )
    return chart

def horizontal_concat(x, y, df, width=300, height=300):
    chart1 = (
        alt.Chart(df)
        .mark_point()
        .encode(x=x, y=y)
        .properties(height=height, width=width)
    )
    chart2 = (
        alt.Chart(df)
        .mark_point()
        .encode(x=x, y=y)
        .properties(height=height, width=width)
    )

    # chart = chart1 | chart2
    chart = alt.hconcat(chart1, chart2)

    return chart

def vertical_concat(x, y, df, width=600, height=300, height2=60, type="interval", encodings=["x"]):
    base = (
        alt.Chart(df)
        .mark_area()
        .encode(x=x+":T", y=y+":Q")
        .properties(width=width, height=height)
    )
    brush = alt.selection(type=type, encodings=encodings)
    upper = base.encode(alt.X(x+":T", scale=alt.Scale(domain=brush)))
    lower = base.properties(height=height2).add_selection(brush)

    chart = upper & lower

    # chart = alt.vconcat(upper, lower)
    return chart

def interactive_chart(x, y, df, color="gray", width=600, height=500):
    brush = alt.selection_interval()
    chart = (
        alt.Chart(df)
        .mark_point()
        .encode(
            x=x+":Q",
            y=y+":Q",
            color=alt.condition(brush, x+":Q", alt.value(color)),
        )
        .properties(width=width, height=height)
        .add_selection(brush)
    )
    return chart

def layout_beta(x, y, color,df, width=600, height=500):
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=x+":O",
            y="sum("+y+")",
            color=color,
            tooltip=["sum("+y+")"],
        )
        .interactive()
        .properties(width=width, height=height)
    )

    return chart

def inputs_chart(x, y, date, color, start_date, end_date, df, width=700, height=500):
    df[date] = pd.to_datetime(df[date])
    if (start_date is not None) & (end_date is not None):
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        dff = df[df[date].isin(pd.date_range(start_date, end_date))]

        chart = (
            alt.Chart(dff)
            .mark_bar()
            .encode(
                x=x+":O",
                y="sum("+y+")",
                color=color,
                tooltip=["sum("+y+")"],
            )
            .interactive()
            .properties(height=height, width=width)
        )
        return chart