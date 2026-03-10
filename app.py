import os

import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv(override=True)

APP_TITLE = "ContentForge AI"

google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise RuntimeError(
        "GOOGLE_API_KEY is not set. Add it in Hugging Face Spaces → Settings → Secrets."
    )

gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
gemini = OpenAI(api_key=google_api_key, base_url=gemini_url)

# Matches your notebook; you can override in Spaces with GEMINI_MODEL
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")


def _build_prompt(tool: str, text: str) -> str:
    if tool == "Tweet Generator":
        return f"Generate a tweet under 280 characters about: {text}"
    if tool == "Hashtag Generator":
        return f"Generate 10 trending hashtags for the topic: {text}"
    if tool == "Caption Generator":
        return f"Generate an engaging Instagram caption about: {text}"
    if tool == "Story Generator":
        return f"Write a short creative story about: {text} under 150 words"
    if tool == "Text Summarizer":
        return f"Summarize the following text in 3 sentences:\n{text}"
    raise ValueError(f"Unknown tool: {tool}")


def generate_content(tool: str, text: str):
    prompt = _build_prompt(tool, text)
    stream = gemini.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful AI content generator."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        stream=True,
    )

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response


with gr.Blocks(title=APP_TITLE) as interface:
    gr.Markdown(
        f"""# {APP_TITLE}
A simple content studio to generate tweets, hashtags, captions, short stories, and summaries from a single prompt.
"""
    )

    with gr.Row():
        tool = gr.Dropdown(
            [
                "Tweet Generator",
                "Hashtag Generator",
                "Caption Generator",
                "Story Generator",
                "Text Summarizer",
            ],
            label="Content Type",
            value="Tweet Generator",
        )

    with gr.Row():
        with gr.Column(scale=1):
            user_input = gr.Textbox(
                label="Topic or Text",
                placeholder="e.g. Launching a new AI-powered productivity app",
                lines=8,
            )
            generate_button = gr.Button("Generate", variant="primary")

        with gr.Column(scale=1):
            output = gr.Textbox(
                label="Generated Content",
                lines=12,
            )

    gr.Markdown(
        """---
**Tip:** Refine your topic or text and click **Generate** again for alternative versions.
"""
    )

    generate_button.click(fn=generate_content, inputs=[tool, user_input], outputs=output)


if __name__ == "__main__":
    # Hugging Face Spaces sets PORT; use 7860 locally.
    port_env = os.getenv("PORT")
    server_port = int(port_env) if port_env else None
    # Locally, bind to 127.0.0.1 so the printed URL is reachable in your browser.
    # On Spaces, we must bind to 0.0.0.0.
    server_name = "0.0.0.0" if port_env else "127.0.0.1"
    interface.queue().launch(
        server_name=server_name,
        server_port=server_port,
        show_error=True,
        share=True,
    )
