import requests
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Функция для загрузки данных
def load_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return pd.DataFrame(response.json().get("records", []))
    else:
        print(f"Ошибка загрузки: {response.status_code}")
        return pd.DataFrame()

# Загрузка данных
url = "http://backend:8000/nocodb-data/"
df = load_data(url)

# Проверка и преобразование данных (если нужно)
df['Date'] = pd.to_datetime(df['Date'])  # Конвертация даты
df.sort_values('Date', inplace=True)     # Сортировка по дате

# Инициализация Dash
app = dash.Dash(__name__)

# Макет приложения
app.layout = html.Div([
    html.H1("Анализ биржевых котировок", style={'textAlign': 'center'}),
    
    dcc.Dropdown(
        id='column-selector',
        options=[
            {'label': 'Цена закрытия', 'value': 'Close'},
            {'label': 'Максимальная цена', 'value': 'High'},
            {'label': 'Минимальная цена', 'value': 'Low'},
            {'label': 'Цена открытия', 'value': 'Open'},
            {'label': 'Объем торгов', 'value': 'Volume'}
        ],
        value='Close',
        clearable=False
    ),
    
    dcc.Graph(id='price-chart'),
    
    html.Div([
        dcc.RangeSlider(
            id='date-slider',
            min=0,
            max=len(df)-1,
            step=1,
            value=[0, len(df)-1],
            marks={i: date for i, date in enumerate(df['Date'].dt.strftime('%Y-%m-%d'))}
        )
    ], style={'marginTop': 40})
])

# Callback для обновления графика
@app.callback(
    Output('price-chart', 'figure'),
    [Input('column-selector', 'value'),
     Input('date-slider', 'value')]
)
def update_chart(selected_column, date_range):
    filtered_df = df.iloc[date_range[0]:date_range[1]+1]
    fig = px.line(
        filtered_df,
        x='Date',
        y=selected_column,
        title=f'Динамика {selected_column}',
        labels={'Date': 'Дата', selected_column: selected_column}
    )
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)