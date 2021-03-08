from app import db
from app.models import User, Client
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.embed import autoload_static
from bokeh.models import MultiSelect
from bokeh.layouts import column, row


def count_clients():

    df_clients = pd.read_sql("clients", db.engine)
    df_users = pd.read_sql("users", db.engine)
    df = pd.merge(
        df_clients,
        df_users[["id", "username"]],
        how="left",
        left_on="user_id",
        right_on="id",
    )
    df = df.groupby("username").count()
    print(df)

    options = list(df.index)

    plot = figure(x_range=options)
    plot.vbar(x=options, top=df.first_name, width=0.75)

    select = MultiSelect(options=options, value=[options[0]])
    layout = column(select, plot)

    return df, layout
