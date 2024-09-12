from fastapi import FastAPI
import gradio as gr
import time
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI
import os

app = FastAPI()


def sayhello(user_name):
    return "welcome" + user_name + "!!"

def chat_function(message, history):
    response = "You said: " + message
    history.append((message, response))
    return response


def chatCompletion(user_input):

 try: 

    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
    )

    azure_oai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
    azure_search_index = os.getenv("AZURE_SEARCH_INDEX")

    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
    )
        
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
            azure_endpoint=azure_oai_endpoint,
            azure_ad_token_provider= token_provider,
            api_version="2024-06-01")

        # Send request to Azure OpenAI model
    print("...Sending the following request to Azure OpenAI endpoint...")
    print("Request: " + user_input + "\n")

    response = client.chat.completions.create(
            model = "gpt-4o",
            temperature = 0.3,
            max_tokens = 1000,
            messages = [
                {"role": "system", "content": "You are a helpful AI Assistant that answers to the employees questions.You'll answer only from the data provided to you"},
                {"role": "user", "content": user_input}
            ],
            extra_body = {
                "data_sources": [{
                    "type": "azure_search",
                    "parameters": {
                        "endpoint": f"{azure_search_endpoint}",
                        "index_name": f"{azure_search_index}",
                        "semantic_configuration": "my-semantic-config",
                        "query_type": "semantic",
                        "fields_mapping": {},
                        "in_scope": True,
                        "role_information": "You are an AI assistant that helps people find information.",
                        "filter": None,
                        "strictness": 3,
                        "top_n_documents": 5,
                        "authentication": {
                        "type": "system_assigned_managed_identity",
                        #"key": f"{azure_search_key}"
                        }
                    }
                    }]
                }
        )
    return response.choices[0].message.content 
 except Exception as ex:
   return ex


chat_history = []
with gr.Blocks() as demo:
    chatbot = gr.Chatbot(label="Employee Assistant")
    
    msg = gr.Textbox(label="Ask me about company policies and healthcare plans.")
    clear = gr.Button("Clear")

    def user(user_message, chat_history):
        # Create a timer to measure the time it takes to complete the request
        start_time = time.time()
        # Get LLM completion
        response_payload = chatCompletion(user_message)
        print(response_payload)
        # Stop the timer
        end_time = time.time()
        elapsed_time = round((end_time - start_time) * 1000, 2)
        # Append user message and response to chat history
        details = f"\n (Time: {elapsed_time}ms)"
    
        chat_history.append([user_message, response_payload + details])

        return gr.update(value=""), chat_history
    
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False)

    clear.click(lambda: None, None, chatbot, queue=False)



app = gr.mount_gradio_app(app, demo, path="/")
