import dash_html_components as html
import base64


hive_header = html.Div(
    className='header',
    children=html.Div(
        className='container-width',
        style={'height': '100%'},
        children=[
            html.Img(
                src="https://herke-my.sharepoint.com/personal/t_lambalk_herke_nl/Documents/HIVE/Images/HIVE.png?slrid=6714269e-8031-4000-938d-c9e3003f7c2c",
                className="logo"
            ),

            html.Div(className="links", children=[
                html.A('Start', className="link", href="/pages/start"),
                html.A('Search', className="link", href="/pages/search"),
                html.A('Settings', className="link", href="/pages/settings")
            ])
        ]
    )
)