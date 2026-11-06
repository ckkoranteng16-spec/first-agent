import gradio as gr
from function_agent import run

def chat(message,history):
    return "Your message was:"+ message

demo=gr.ChatInterface(
    fn=chat,
    title="My first agent",
    description="Chat with my AI assistant."
)

demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 10000)))