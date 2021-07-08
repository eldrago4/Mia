from __future__ import print_function
import pickle4 as pickle
from flask import Flask, url_for, session
from authlib.integrations.flask_client import OAuth
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class gsheet(object):
	def __init__(self):
		SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
		self.creds = None
		# The file token.pickle stores the user's access and refresh tokens, and is
		# created automatically when the authorization flow completes for the first
		# time.
		if os.path.exists('token.pickle'):
			with open('token.pickle', 'rb') as token:
				self.creds = pickle.load(token)
		# If there are no (valid) credentials available, let the user log in.
		# here 
			# Save the credentials for the next run

		self.service = build('sheets', 'v4', credentials=self.creds)

	def add(self, sheetid, sheetrange, ivalue):
		# Call the Sheets API
		sheet = self.service.spreadsheets()
		values = []
		values.append(ivalue)
		body = {'values': values}
		result = sheet.values().append(spreadsheetId=sheetid,
		                               range=sheetrange,
		                               valueInputOption='RAW',
		                               body=body).execute()
