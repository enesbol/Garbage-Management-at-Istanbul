import socket
import google_auth_httplib2
import httplib2
import pandas as pd
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import HttpRequest
import os 

socket.setdefaulttimeout(15 * 60)

SCOPE = "https://www.googleapis.com/auth/spreadsheets" 

SPREADSHEET_ID="1em4x3cE0R22mCwcNTQxhN4lblhGQkq9O_D48REQ8g1M"

@st.experimental_singleton()

def connect():
    # Create a connection object.
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=[SCOPE],
    )    
    
    # Create a new Http() object for every request
    def build_request(http, *args, **kwargs):
        new_http = google_auth_httplib2.AuthorizedHttp(
            credentials, http=httplib2.Http()
        )
        return HttpRequest(new_http, *args, **kwargs)

    authorized_http = google_auth_httplib2.AuthorizedHttp(
        credentials, http=httplib2.Http()
    )       
    service = build(
        "sheets",
        "v4",
        requestBuilder=build_request,
        http=authorized_http,
    )    

    gsheet_connector = service.spreadsheets()       
    return gsheet_connector


def collect(gsheet_connector) -> pd.DataFrame:
    
    values = (
        gsheet_connector.values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            range="A:C",
        )
        .execute()
    )
    

    df = pd.DataFrame(values["values"])    
    df.columns = df.iloc[0]
    df = df[1:]
    return df


def insert(gsheet_connector, row) -> None:
    values = (
        gsheet_connector.values()
        .append(
            spreadsheetId=SPREADSHEET_ID,
            range="A:C",
            body=dict(values=row),
            valueInputOption="USER_ENTERED",
        )
        .execute()
    )
