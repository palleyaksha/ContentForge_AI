---
title: ContentForge AI
emoji: "🚀"
colorFrom: indigo
colorTo: pink
sdk: gradio
python_version: "3.11"
app_file: app.py
pinned: false
---

# AI Content Toolkit using LLMs 🚀

**ContentForge AI** is a multi-feature AI application that generates different types of content using Large Language Models (LLMs).
The application allows users to quickly generate tweets, hashtags, captions, short stories, and text summaries through a simple interactive interface.

---

## ✨ Features

- 🐦 **Tweet Generator**  
  Generate short tweets based on a topic.

- #️⃣ **Hashtag Generator**  
  Create trending hashtags for social media posts.

- 📸 **Caption Generator**  
  Produce engaging captions for Instagram or social media.

- 📖 **Story Generator**  
  Generate creative short stories from a given idea.

- 📝 **Text Summarizer**  
  Summarize long text into concise key points.

---

## 🧠 Tech Stack

- **Python**
- **Gradio** – for the web interface
- **Google Gemini API** – for LLM-based text generation (via Google’s OpenAI-compatible endpoint)
- **Hugging Face Spaces** – for free cloud deployment

---

## 📂 Project Structure

```text
project1/
├── app.py              # Main application file
├── requirements.txt    # Required Python libraries
└── README.md           # Project documentation
```

---

## ⚙️ Installation (Local Setup)

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your API key:

Create a `.env` file and add:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

Run the application:

```bash
python app.py
```

---



## 📸 Example Usage

Input:

```text
Topic: Artificial Intelligence
```

Output:

```text
Tweet:
AI is transforming the future one algorithm at a time 🚀
```

---

## 🧾 How the code works

Key parts in `app.py`:

- **Gemini client setup**: reads `GOOGLE_API_KEY` and creates an `OpenAI(...)` client using the Gemini OpenAI-compatible base URL.
- **`_build_prompt(tool, text)`**: converts your chosen tool + input into a prompt.
- **`generate_content(tool, text)`**: calls `gemini.chat.completions.create(..., stream=True)` and streams output to the UI.
- **Gradio UI**: built with `gr.Blocks` and shows input/output side-by-side.

---

## 🚀 Future Improvements

- Content style selector (funny / professional / marketing)
- Multi-language support
- Content history storage
- Better error handling + retries for rate limits

---

## 👨‍💻 Author

**Palle Yaksha Reddy**  

---

## 📜 License

This project is licensed under the MIT License.

