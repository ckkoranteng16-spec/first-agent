import gradio as gr
from function_agent import run

print('Hello, how may i help you?.')

def chat(message,history):
    return run(message)

demo=gr.ChatInterface(
    fn=chat,
    title="My first agent",
    description="Chat with my AI assistant."
)

demo.launch(share=True)#(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 10000)))