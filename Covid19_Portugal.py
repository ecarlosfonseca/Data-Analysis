import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models.widgets import Tabs, Panel
from bokeh.layouts import gridplot, row, column
from bokeh.models import Label
from math import pi
from bokeh.transform import cumsum

url = 'https://raw.githubusercontent.com/dssg-pt/covid19pt-data/master/data.csv'
data = pd.read_csv(url, sep=',')

# Overall data
p1 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people infected',
            title='Infected evolution (region and total)', toolbar_location=None)
p1.line(list(range(len(data['confirmados']))), data['confirmados'], color='gray', legend='Portugal')
p1.line(list(range(len(data['confirmados']))), data['confirmados_arsnorte'], color='blue', legend='North')
p1.line(list(range(len(data['confirmados']))), data['confirmados_arscentro'], color='black', legend='Center')
p1.line(list(range(len(data['confirmados']))), data['confirmados_arslvt'], color='red', legend='Lisbon and Tejo valey')
p1.line(list(range(len(data['confirmados']))), data['confirmados_arsalentejo'] + data['confirmados_arsalgarve'],
        color='green', legend='South')
p1.line(list(range(len(data['confirmados']))), data['confirmados_acores'] + data['confirmados_madeira'], color='yellow',
        legend='Madeira and Açores')
p1.legend.location = 'top_left'

p2 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people deceased',
            title='Deceased evolution (region and total)', toolbar_location=None)
p2.line(list(range(len(data['obitos']))), data['obitos'], color='gray', legend='Portugal')
p2.line(list(range(len(data['obitos']))), data['obitos_arsnorte'], color='blue', legend='North')
p2.line(list(range(len(data['obitos']))), data['obitos_arscentro'], color='black', legend='Center')
p2.line(list(range(len(data['obitos']))), data['obitos_arslvt'], color='red', legend='Lisbon and Tejo valey')
p2.line(list(range(len(data['obitos']))), data['obitos_arsalentejo'] + data['obitos_arsalgarve'], color='green',
        legend='South')
p2.line(list(range(len(data['obitos']))), data['obitos_acores'] + data['obitos_madeira'], color='yellow',
        legend='Madeira and Açores')
p2.legend.location = 'top_left'

# Data per region for tab 2
p3 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='North',
            toolbar_location=None)
p3.line(list(range(len(data['confirmados']))), data['confirmados_arsnorte'], color='orange', legend='Infected')
p3.line(list(range(len(data['obitos']))), data['obitos_arsnorte'], color='red', legend='Deceased')
p3.legend.location = 'top_left'
p3.add_layout(Label(x=10, y=430, text='Total Population: 3.818.722 ppl  35,9%', x_units='screen', y_units='screen',
                    render_mode='css',
                    background_fill_color='white', background_fill_alpha=1.0))

p4 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='Center',
            toolbar_location=None)
p4.line(list(range(len(data['confirmados']))), data['confirmados_arscentro'], color='orange', legend='Infected')
p4.line(list(range(len(data['obitos']))), data['obitos_arscentro'], color='red', legend='Deceased')
p4.legend.location = 'top_left'
p4.add_layout(Label(x=10, y=430, text='Total Population: 2.348.453 ppl  22,1%', x_units='screen', y_units='screen',
                    render_mode='css',
                    background_fill_color='white', background_fill_alpha=1.0))

p5 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='Lisbon and Tejo valey',
            y_range=p3.y_range, toolbar_location=None)
p5.line(list(range(len(data['confirmados']))), data['confirmados_arslvt'], color='orange', legend='Infected')
p5.line(list(range(len(data['obitos']))), data['obitos_arslvt'], color='red', legend='Deceased')
p5.legend.location = 'top_left'
p5.add_layout(Label(x=10, y=430, text='Total Population: 2.808.414 ppl  26,4%', x_units='screen', y_units='screen',
                    render_mode='css',
                    background_fill_color='white', background_fill_alpha=1.0))

p6 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='South',
            toolbar_location=None)
p6.line(list(range(len(data['confirmados']))), data['confirmados_arsalentejo'] + data['confirmados_arsalgarve'],
        color='orange', legend='Infected')
p6.line(list(range(len(data['obitos']))), data['obitos_arsalentejo'] + data['obitos_arsalgarve'], color='red',
        legend='Deceased')
p6.legend.location = 'top_left'
p6.add_layout(Label(x=10, y=430, text='Total Population: 1.171.547 ppl  11%', x_units='screen', y_units='screen',
                    render_mode='css',
                    background_fill_color='white', background_fill_alpha=1.0))

p7 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='Madeira e Açores',
            y_range=p6.y_range, toolbar_location=None)
p7.line(list(range(len(data['confirmados']))), data['confirmados_acores'] + data['confirmados_madeira'], color='orange',
        legend='Infected')
p7.line(list(range(len(data['obitos']))), data['obitos_acores'] + data['obitos_madeira'], color='red',
        legend='Deceased')
p7.legend.location = 'top_left'
p7.add_layout(
    Label(x=10, y=430, text='Population: 489.018 ppl  4,6%', x_units='screen', y_units='screen', render_mode='css',
          background_fill_color='white', background_fill_alpha=1.0))

# Data per sex for tab 3
p8 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people infected', title='Infected',
            toolbar_location=None)
p8.line(list(range(len(data['confirmados']))), data['confirmados_f'], color='pink', legend='Female')
p8.line(list(range(len(data['confirmados']))), data['confirmados_m'], color='skyblue', legend='Male')
p8.legend.location = 'top_left'

p9 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people deceased', title='Deceased',
            toolbar_location=None)
p9.line(list(range(len(data['confirmados']))), data['obitos_f'], color='pink', legend='Female')
p9.line(list(range(len(data['confirmados']))), data['obitos_m'], color='skyblue', legend='Male')
p9.legend.location = 'top_left'

p10 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='Age 0 to 9',
             toolbar_location=None)
p10.line(list(range(len(data['confirmados']))), data['confirmados_0_9_f'], color='pink', legend='Female')
p10.line(list(range(len(data['confirmados']))), data['confirmados_0_9_m'], color='skyblue', legend='Male')
p10.legend.location = 'top_left'

p11 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='Age 10 to 19',
             y_range=p10.y_range, toolbar_location=None)
p11.line(list(range(len(data['confirmados']))), data['confirmados_10_19_f'], color='pink', legend='Female')
p11.line(list(range(len(data['confirmados']))), data['confirmados_10_19_m'], color='skyblue', legend='Male')
p11.legend.location = 'top_left'

p12 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='Age 20 to 29',
             toolbar_location=None)
p12.line(list(range(len(data['confirmados']))), data['confirmados_20_29_f'], color='pink', legend='Female')
p12.line(list(range(len(data['confirmados']))), data['confirmados_20_29_m'], color='skyblue', legend='Male')
p12.legend.location = 'top_left'

p13 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='Age 30 to 39',
             y_range=p12.y_range, toolbar_location=None)
p13.line(list(range(len(data['confirmados']))), data['confirmados_30_39_f'], color='pink', legend='Female')
p13.line(list(range(len(data['confirmados']))), data['confirmados_30_39_m'], color='skyblue', legend='Male')
p13.legend.location = 'top_left'

p14 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='Age 40 to 49',
             toolbar_location=None)
p14.line(list(range(len(data['confirmados']))), data['confirmados_40_49_f'], color='pink', legend='Female')
p14.line(list(range(len(data['confirmados']))), data['confirmados_40_49_m'], color='skyblue', legend='Male')
p14.legend.location = 'top_left'

p15 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='Age 50 to 59',
             y_range=p14.y_range, toolbar_location=None)
p15.line(list(range(len(data['confirmados']))), data['confirmados_50_59_f'], color='pink', legend='Female')
p15.line(list(range(len(data['confirmados']))), data['confirmados_50_59_m'], color='skyblue', legend='Male')
p15.legend.location = 'top_left'

p16 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='Age 60 to 69',
             toolbar_location=None)
p16.line(list(range(len(data['confirmados']))), data['confirmados_60_69_f'], color='pink', legend='Female')
p16.line(list(range(len(data['confirmados']))), data['confirmados_60_69_m'], color='skyblue', legend='Male')
p16.legend.location = 'top_left'

p17 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='Age 70 to 79',
             y_range=p16.y_range, toolbar_location=None)
p17.line(list(range(len(data['confirmados']))), data['confirmados_70_79_f'], color='pink', legend='Female')
p17.line(list(range(len(data['confirmados']))), data['confirmados_70_79_m'], color='skyblue', legend='Male')
p17.legend.location = 'top_left'

p18 = figure(x_axis_label='Days (from the 26th Feb)', y_axis_label='Number of people', title='Age 80 Plus',
             toolbar_location=None)
p18.line(list(range(len(data['confirmados']))), data['confirmados_80_plus_f'], color='pink', legend='Female')
p18.line(list(range(len(data['confirmados']))), data['confirmados_80_plus_m'], color='skyblue', legend='Male')
p18.legend.location = 'top_left'

# Stacked Bar chart
p_bar_tags = ['Infected', 'Recovered', 'Deceased', 'Hospitalized']
p_bar_y_data = ['Male', 'Female']
pie_colors = ['skyblue', 'pink']
p_bar_data = {'Type': p_bar_tags,
              'Male': [list(data['confirmados_m'])[-1], list(data['recuperados'])[-1], list(data['obitos_m'])[-1],
                       list(data['internados'])[-1]],
              'Female': [list(data['confirmados_f'])[-1], 0, list(data['obitos_f'])[-1], 0]}
tooltips = [("Type", "@Type"), ("Male", "@Male"), ("Female", "@Female")]
p19 = figure(x_range=p_bar_tags, title='Covid19 Portugal Current Numbers', tools="hover", tooltips=tooltips,
             toolbar_location=None)
p19.vbar_stack(p_bar_y_data, x='Type', width=0.9, fill_color=pie_colors, source=p_bar_data, legend_label=p_bar_y_data,
               line_color='white')
p19.y_range.start = 0
p19.legend.location = "top_right"
p19.xgrid.grid_line_color = None
p19.axis.minor_tick_line_color = None
p19.outline_line_color = None

# Pie Chart
p_pie_data_1 = {'Infected': list(data['confirmados_m'])[-1],
                'Recovered': list(data['recuperados'])[-1],
                'Deceased': list(data['obitos'])[-1],
                'Hospitalized': list(data['internados'])[-1],
                }
data_pie = pd.Series(p_pie_data_1).reset_index(name='value').rename(columns={'index': 'count'})
data_pie['angle'] = data_pie['value'] / data_pie['value'].sum() * 2 * pi
data_pie['color'] = ['palegreen', 'cadetblue', 'tomato', 'gray']
p20 = figure(title="Overall Numbers", toolbar_location=None,
             tools="hover", tooltips="@count: @value", x_range=(-0.5, 1.0))
p20.wedge(x=0, y=1, radius=0.4,
          start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
          line_color="white", fill_color='color', legend='count', source=data_pie)
p20.axis.axis_label = None
p20.axis.visible = False
p20.grid.grid_line_color = None

# Tabs Layout
grid1 = column(row(p19, p20), row(p1, p2))
grid2 = column(row(p3, p5), p4, row(p6, p7))
grid3 = row(p8, p9)
grid4 = column(row(p10, p11), row(p12, p13), row(p14, p15), row(p16, p17), row(p18))

# Tabs definition
tab1 = Panel(child=grid1, title='Country')
tab2 = Panel(child=grid2, title='Per Region')
tab3 = Panel(child=grid3, title='Evolution per sex')
tab4 = Panel(child=grid4, title='Infected per age and sex')

# Layout definition
layout = Tabs(tabs=[tab1, tab2, tab3, tab4])

output_file('Covid19.html')
show(layout)
