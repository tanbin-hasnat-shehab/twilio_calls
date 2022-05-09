from twilio.rest import Client
import streamlit as st
client=Client('ACf0c9dd10f8ba0f28e2059ba419d712b0','16208f93e8280a26c4420d7572d4554a')


def make_call():
	call_now=client.calls.create(
			twiml='<response><say>Do you Know me</say></response>',
			from_='+19704699073',
			to='+8801533687497'



			)


	messege=client.messages.create(
			body='বেতন ঢুকছে??...হাসনাত',
			from_='+19704699073',
			to='+8801533687497'



			)
call=st.button('call')
if call:
	make_call()
