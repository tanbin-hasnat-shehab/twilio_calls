from twilio.rest import Client
import streamlit as st

#######
sid='AC8c67dd7dd08e64e851275055d3077f65'
Auth='7c9e2600f7f69fd865b3e0150fc14e0d'
My_Twilio_phone_number='+19706968514'


#########



st.header('Twilio make free calls')
st.markdown('<a href="https://console.twilio.com/?frameUrl=/console">goto twilio dashboard</a>',unsafe_allow_html=True)
SID=st.text_input('Account SID',sid)
auth=st.text_input('Auth Token',Auth)
tw_ph=st.text_input('My Twilio phone number',My_Twilio_phone_number)
st.markdown('<a href="https://console.twilio.com/us1/develop/phone-numbers/manage/verified?frameUrl=%2Fconsole%2Fphone-numbers%2Fverified%3Fx-target-region%3Dus1">see verified phone numbers you can call</a>',unsafe_allow_html=True)

to_call=st.text_input('Enter Number')
your_m=st.text_input('your message')



def make_call():
	client=Client(SID,auth)
	call_now=client.calls.create(
			twiml='<response><say>Do you Know me</say></response>',
			from_=tw_ph,
			to=to_call



			)


	messege=client.messages.create(
			body=your_m,
			from_=tw_ph,
			to=to_call



			)
call=st.button('SEND IT')
if call:
	st.success('call sent')
	make_call()
