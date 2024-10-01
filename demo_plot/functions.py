import pandas as pd
import plotly.graph_objects as go

def custom_bar_plot(df, 
                    x=None, 
                    y=None, 
                    x_label="X-axis", 
                    y_label="Y-axis", 
                    x_scale=None, 
                    y_scale=None, 
                    x_tick_angle=None,
                    tick_font_size=8,
                    tick_color="black",
                    chart_title="Chart Title", 
                    chart_title_color="#7D7D7D", 
                    chart_title_font_size=12,
                    chart_title_pos=0.5,
                    legend_title="Legend", 
                    legend_orientation="v",
                    legend_align=(1,1), 
                    color='#1f77b4',
                    gradient=False,
                    color_scale="Blues",
                    single_bar_color=None, 
                    axis_label_color="#7D7D7D", 
                    axis_title_font_size=8,
                    hover_text=False, 
                    sort_by=None, 
                    sort_order="asc", 
                    bar_width=0.4,
                    x_grid=False,
                    y_grid=True
                    ):

    """
    Requires: df -> a dataframe, x -> variable along x axis, y -> variable along y axis ,
                    some default values are given for other parameters.

    Returns: a customised vertical barplot
    """

    
    # Sort the data if requested
    if sort_by is not None:
        if sort_by == "x":
            df = df.sort_values(by=x, ascending=(sort_order == "asc"))
        elif sort_by == "y":
            df = df.sort_values(by=y, ascending=(sort_order == "asc"))
    df[x] = df[x].astype('str')

    # Customize color of selected bar(s)
    highlight_color = 'rgba(222,45,38,0.8)'
    if single_bar_color is not None:
        colors = [highlight_color if i in single_bar_color else color for i in df[x]]
        color = colors
            
    # Create base plot
    fig = go.Figure()

    if gradient:        
        fig.add_trace(go.Bar(
            x=df[x] ,
            y=df[y] ,
            marker=dict(
            color=df[y],  
            colorscale=color_scale,  
            colorbar=dict(
                title='Population',  
                titlefont=dict(size=12))
            ),
            hovertext = [f'{x_label}: {x}<br>{y_label}: {y}' for x,y in zip(df[x], df[y])],
            hoverinfo='text' if hover_text else 'none',
            text=df[y] if not( hover_text) else None,
            width=bar_width
        ))
    else:
        fig.add_trace(go.Bar(
            x=df[x] ,
            y=df[y] ,
            marker_color=color,
            hovertext = [f'{x_label}: {x}<br>{y_label}: {y}' for x,y in zip(df[x], df[y])],
            hoverinfo='text' if hover_text else 'none',
            text=df[y] if not( hover_text) else None,
            width=bar_width
        ))        

    # Set axis labels and title
    fig.update_layout(
        title=dict(text=chart_title, font=dict(color=chart_title_color,size=chart_title_font_size),x= chart_title_pos, xanchor= 'auto'),
        legend_title_text=legend_title,
        legend=dict(orientation=legend_orientation,  
                    x=legend_align[0],              
                    y=legend_align[1]),
        xaxis=dict(
            gridcolor='#D3D3D3', showgrid=x_grid, title=x_label,
            tickmode='array',
            tickvals=df[x] ,  
            ticktext=df[x] ,  
            tickfont=dict(color=tick_color,size=tick_font_size),
            tickangle=x_tick_angle,
            title_font=dict(color=axis_label_color,size=axis_title_font_size),
            range=x_scale  
        ),
        
        yaxis=dict(gridcolor='#D3D3D3', showgrid=y_grid, title=y_label ,
                   title_font=dict(color=axis_label_color,size=axis_title_font_size), 
                   tickfont=dict(color=tick_color,size=tick_font_size), range=y_scale),
        plot_bgcolor='white'  
    )

    return(fig)
    