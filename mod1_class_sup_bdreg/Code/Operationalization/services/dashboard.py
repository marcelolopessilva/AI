import dash
import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash
import pandas as pd
import plotly.express as px
from applications.models import RelatorioDou, InsumoDou
from dash.dependencies import Input, Output
from datetime import datetime, date
import dash_table

app = DjangoDash('DashboardDOU')   # replaces dash.Dash

# Recupera os dados do relatório e decodifica algumas informações
df_relatorio = pd.DataFrame(RelatorioDou.objects.all().values())
df_relatorio.loc[df_relatorio['cod_interesse'] == 'SI', 'cod_interesse'] = 'Sem Interesse'
df_relatorio.loc[df_relatorio['cod_interesse'] == 'DI', 'cod_interesse'] = 'De Interesse'

# Faz o setup do gráfico do relatório
fig = px.bar(df_relatorio , x="num_dia"
                          , y="num_quantidade"
                          , color="cod_interesse"
                          , title="Previsões Diárias"
                          , labels = { "num_dia":"Mês/Dia",
                                       "num_quantidade":"Quantidade",
                                       "cod_interesse":"Previsão"
                                     }
                          , text = "num_quantidade"           
            )

fig.update_layout(
    font_family="Courier New",
    font_color="blue",
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="black",
    xaxis={'type': 'category'},
    barmode='group'
)

def atualiza_dataframe(data_escolhida):
    # Filtra dataframe para a data específica
    df_insumodou = pd.DataFrame(InsumoDou.objects.filter(dat_publicacao=data_escolhida).values('nome','secao','categoria','dsc_texto','din_validacao','cod_interesse'))

    # Ajusta textos das colunas se tiverem retorno
    if df_insumodou.empty:
        df_insumodou = pd.DataFrame({  'nome':[f'Sem dados para o dia {data_escolhida}!']
                                    , 'secao':['']
                                    , 'categoria':['']
                                    , 'dsc_texto':['']
                                    , 'din_validacao':['']
                                    , 'cod_interesse':['']
                                })
    else:
        df_insumodou['dsc_texto'] = df_insumodou['dsc_texto'].str.slice(22, 52) + '...'
        df_insumodou['categoria'] = df_insumodou['categoria'].str.slice(0, 30) + '...'
        df_insumodou.loc[df_insumodou['cod_interesse'] == 'SI', 'cod_interesse'] = 'Sem Interesse'
        df_insumodou.loc[df_insumodou['cod_interesse'] == 'DI', 'cod_interesse'] = 'De Interesse'

    #Renomeando as colunas
    renome_coluna = {'nome':"Nome"
                    ,'secao':"Seção"
                    ,'categoria': "Categoria"
                    ,'dsc_texto':'Texto'
                    ,'din_validacao':'Data da Previsão'
                    ,'cod_interesse':'Previsão'
                    }

    df_insumodou.rename(columns = renome_coluna, inplace = True)

    return df_insumodou

# Faz o setup da tabela dos registros

# Recupera os dados dos registros do dia
hoje = str(date.today().day)+'/'+str(date.today().month)+'/'+str(date.today().year)
dat_inicio = datetime.strptime(hoje, '%d/%m/%Y')

df = atualiza_dataframe(dat_inicio)

df['index'] = range(1, len(df) + 1)

#PAGE_SIZE = 10

app.layout = html.Div(
    children=[
                html.H1(children='Dashboard Operacional DOU'),

                html.Div([
                            html.Div(["Data da Previsão: ",
                                    dcc.DatePickerSingle(id='date-picker-single',date=datetime.now(), display_format='DD/MM/YYYY'),
                                    html.Br(),
                                    html.Div(id='my-date-output'),
                                    ]),
                            dcc.Graph(
                                id='relatorio-graph',
                                figure=fig,
                                responsive=True
                        )
                ]),
                dash_table.DataTable(
                                    id='datatable',
                                    columns=[
                                        {"name": i, "id": i} for i in df.columns
                                    ],
                                    # page_current=0,
                                    # page_size=PAGE_SIZE,
                                    # page_action='custom',
                                    filter_action="native",
                                    sort_action="native",
                                    sort_mode="multi",
                                    column_selectable="single",
                                    row_selectable="multi"
                                )
             ]
)

@app.callback(
    Output('datatable-paging', 'data'),
    [Input('datatable-paging', "page_current"),
     Input('datatable-paging', "page_size")],
    )
def update_table(page_current,page_size, date):
    return df.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')

@app.callback(
    Output('datatable', 'data'),
    [Input('date-picker-single', 'date')])
def update_data(date):
    if date is not None:
        df = atualiza_dataframe(date)
        data = df.to_dict('records')
    return data  