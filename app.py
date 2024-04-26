import autogen

class TrackableAssistantAgent1(AssistantAgent):
    def _process_received_message(self, message, sender, silent):
        with st.chat_message(sender.name):
            output = message["name"] + ": " + message["content"]
            st.markdown(output)
        return super()._process_received_message(message, sender, silent)

class TrackableAssistantAgent2(AssistantAgent):
    def _process_received_message(self, message, sender, silent):
        with st.chat_message(sender.name):
            output = message["name"] + ": " + message["content"]
            st.markdown(output)
        return super()._process_received_message(message, sender, silent)

class TrackableAssistantAgent3(AssistantAgent):
    def _process_received_message(self, message, sender, silent):
        with st.chat_message(sender.name):
            output = message["name"] + ": " + message["content"]
            st.markdown(output)
        return super()._process_received_message(message, sender, silent)
    
class TrackableAssistantAgent4(AssistantAgent):
    def _process_received_message(self, message, sender, silent):
        with st.chat_message(sender.name):
            output = message["name"] + ": " + message["content"]
            st.markdown(output)
        return super()._process_received_message(message, sender, silent)


class TrackableUserProxyAgent(UserProxyAgent):
    def _process_received_message(self, message, sender, silent):
        with st.chat_message(sender.name):
            output = message["name"] + ": " + message["content"]
            st.markdown(output)
        return super()._process_received_message(message, sender, silent) 
      
with st.form("my_form"):
    st.write("Fill the following information about your group meeting. Then, click submit.")
        
    #User Proxy Agent
    system_message0 = st.text_area("Chairman of the meeting", height=300,
                                   placeholder = '''Enter detailed information about yourself as the Chairman of this group meeting''')
    user_proxy = TrackableUserProxyAgent(name="Admin", 
                                system_message = system_message0, 
                                code_execution_config=False,
                                llm_config=llm_config1,
                                human_input_mode='NEVER' 
                                )
    
    #Assistant Agent 1
    agent1_role = st.text_input("Agent One", placeholder = "Enter agent one's role in this meeting with  no spaces e.g. Research_Analyst")
    system_message1 = st.text_area("Agent One's instructions", height=300,
                                   placeholder = '''Example (replace with your own):''')
    agent1 = TrackableAssistantAgent1(name=agent1_role, 
                                     llm_config=llm_config1, 
                                     system_message=system_message1)
    
    
    #Assistant Agent 2
    agent2_role = st.text_input("Agent Two", placeholder = "Enter agent two's role in this meeting with no spaces e.g. Portfolio_Manager")
    system_message2 = st.text_area("Agent Two's instructions", height=300, 
                                   placeholder = '''Example (replace with your own): ''')
    agent2 = TrackableAssistantAgent2(name=agent2_role, 
                                     llm_config=llm_config1, 
                                     system_message=system_message2)
    
    #Assistant Agent 3
    agent3_role = st.text_input("Agent Three", placeholder = "Enter agent three's role in this meeting with no spaces e.g. Risk_analyst")
    system_message3 = st.text_area("Agent Three's instructions", height=300, 
                                   placeholder = '''Example (replace with your own): ''')
    agent3 = TrackableAssistantAgent3(name=agent3_role, 
                                     llm_config=llm_config1, 
                                     system_message=system_message3)
    
    #Assistant Agent 4
    agent4_role = st.text_input("Agent Four", placeholder = "Enter agent four's role in this meeting with no spaces e.g. Marketing_Manager")
    system_message4 = st.text_area("Agent Four's instructions", height=300,
                                   placeholder = '''Example (replace with your own): ''')
    agent4 = TrackableAssistantAgent4(name=agent4_role, 
                                     llm_config=llm_config1, 
                                     system_message=system_message4)
    
    #submit button
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.session_state.agent1_role = agent1_role
        st.session_state.agent2_role = agent2_role
        st.session_state.agent3_role = agent3_role
        st.session_state.agent4_role = agent4_role
        st.session_state.system_message1 = system_message1
        st.session_state.system_message2 = system_message2
        st.session_state.system_message3 = system_message3
        st.session_state.system_message4 = system_message4
        st.session_state.system_message0 = system_message0
        #st.write("info submitted. Type a greeting message below to start the meeting.")
        #print("info submitted")
        #st.experimental_rerun()
        #print("rerun")
        #st.container.empty()
        
 
 
 
 
 
 
 
 
 
user_input = st.chat_input("Start the meeting with a greeting message. e.g. Hello everyone, welcome to the meeting.") 
 
groupchat = GroupChat(
        agents=[user_proxy, agent1, agent2, agent3, agent4], 
        messages=[], max_round=50)
partner = GroupChatManager(groupchat=groupchat, llm_config=llm_config1)
  
if user_input: 
    
    # Create an event loop
    #loop = asyncio.new_event_loop()
    #asyncio.set_event_loop(loop)
    
    #Define aynchronous function
    async def initiate_chat():
        chat_messages = user_proxy.a_initiate_chat(
            partner,
            message=user_input,
            llm_config = llm_config1
        )
        await chat_messages
        print("Console Log" + chat_messages)
        messages = []
        for message in chat_messages.messages:
            if message not in messages:
                messages.append(message["name"] + ": " + message["content"])
                st.session_state.messages = messages
                st.write(message["name"] + ": " + message["content"])
            #return chat_messages
    
    #Run the asynchronous function
    asyncio.run(initiate_chat())
