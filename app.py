import dash
from dash import html
import dash_bootstrap_components as dbc

# =========== Variáveis =========== #
app = dash.Dash(external_stylesheets=[dbc.themes.MORPH])
server = app.server


# =========== Importando Dados Tratados =========== #


# =========== Layout =========== #
app.layout = html.Div([
                dbc.Row(
                    html.Div(style={"height": "25vh"}),
                ),
                dbc.Row([
                    dbc.Col(md=4),
                    dbc.Col(
                        dbc.Card([
                            dbc.CardBody([
                                html.H3("Para Natália:",className="card-header"),
                                html.H5("Olha só o que eu sei fazer Nat!",
                                        className="card-title",
                                        style={"padding-top":"10px"}),
                                html.P("rsrsrs",
                                    className="card-text")
                            ]),
                            dbc.CardImg(
                                src="https://uploads.metropoles.com/wp-content/uploads/2019/10/30122752/The-office-600x400.jpg"
                                )
                            ], className="border-secondary mb-3 mb-3"
                        ),
                        md=4
                    )
                ])
])
# =========== Callbacks =========== #


# =========== Run Server =========== #
if __name__ == "__main__":
    app.run_server(port=8050, debug=False)