# 🎓 Multiple Choice Questions Quiz Application

An interactive web application that generates customized multiple-choice quizzes on any topic using OpenAI's GPT models and Streamlit. Perfect for educators, students, or anyone looking to test their knowledge.

## ✨ Features

-  Dynamic quiz generation on any topic
-  Customizable number of questions (1-10)
-  Multiple choice format with automatic grading
-  Objective, fact-based questions
-  Clean, user-friendly interface
-  Detailed review of answers

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/) - Web interface
- [LangChain](https://www.langchain.com/) - LLM framework
- [OpenAI GPT-4](https://openai.com/) - Question generation
- [Python](https://www.python.org/) - Backend logic

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- Internet connection

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/ibrahimsabouh/MCQ-Quiz-Application.git
cd interactive-quiz-generator
```

2. Create a virtual environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Unix/macOS
python3 -m venv .venv
source .venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

## 💻 Usage

1. Start the application:
```bash
streamlit run streamlit_app.py
```

2. Access the app in your browser (typically `http://localhost:8501`)

3. Enter your desired:
   - Quiz topic
   - Number of questions
   - Click "Generate Quiz"

4. Answer the questions and get instant results!

## 📁 Project Structure

```
MCQ-Quiz-Application/
├── streamlit_app.py        # Main Streamlit application
├── quiz_generator.py       # Quiz generation logic
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## ⚙️ Configuration

Modify the quiz settings in `quiz_generator.py`:
- Change GPT model
- Adjust temperature for creativity
- Customize question format
- Modify prompt template

## 👏 Acknowledgments

- OpenAI for providing the GPT API
- Streamlit team for the amazing framework
- LangChain for the LLM tooling

## 📧 Contact

Ibrahim Sabouh - [ibrahim.sabouh7@gmail.com](mailto:ibrahim.sabouh7@gmail.com)
