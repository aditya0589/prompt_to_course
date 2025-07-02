# Prompt-to-Course 

**Prompt-to-Course ** is an AI-powered web application that transforms user prompts into detailed, multi-topic course outlines. Built with **Streamlit** and **Meta’s LLaMA model served via Groq API**, it empowers learners, educators, and curriculum designers to generate personalized learning paths instantly.

---

## Features

-  Converts plain natural language prompts into structured course outlines  
-  Generates multi-module, multi-topic educational content  
-  Fast and lightweight UI using Streamlit  
-  Powered by Groq’s high-speed LLaMA model API  
-  Easily extendable for exporting or curriculum publishing  

---

## Tech Stack

- **Language:** Python  
- **Frontend/UI:** Streamlit  
- **LLM Backend:** Meta’s LLaMA via Groq API  
- **Libraries:**  
  - `streamlit`  
  - `requests`  
  - `python-dotenv`  
  - `uuid`, `json`, etc.  

---

##  Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/prompt-to-course.git
   cd prompt-to-course
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file and add your Groq API key:**
   ```
   GROQ_API_KEY=your-groq-api-key
   ```

5. **Run the app:**
   ```bash
   streamlit run app.py
   ```

---

## How It Works

The app sends your prompt to Groq's hosted **LLaMA model**, which returns a structured response formatted into a human-readable course outline.  
It’s designed to be fast, adaptable, and extensible to future LLM providers or learning models.


## Contributing

Pull requests are welcome!  
To suggest a feature, improvement, or report a bug, please open an issue.

---


