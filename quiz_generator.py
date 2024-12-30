from typing import Dict, Optional
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

class QuizGenerator:
    def __init__(self, model: str = "gpt-4", temperature: float = 0.8):
        """Initialize QuizGenerator with model settings."""
        load_dotenv()  # Load environment variables from .env file
        self.llm = ChatOpenAI(model=model, temperature=temperature)
        self.prompt = self._create_question_prompt()

    def _create_question_prompt(self) -> PromptTemplate:
        """Create and return the question prompt template."""
        template = """
        Create {n} multiple-choice questions on the topic "{topic}".
        Each question should:
        - Be objective and based on verifiable facts
        - Have 4 options (a, b, c, d)
        - Include 1 correct and 3 plausible incorrect answers
        - Avoid subjective or opinion-based content
        
        Format each question exactly like this:
        Question: <question text>
        a) <option>
        b) <option>
        c) <option>
        d) <option>
        Correct answer: <letter>

        Make sure to include a blank line between questions.
        """
        return PromptTemplate.from_template(template)

    def generate(self, topic: str, n_questions: int) -> Optional[str]:
        """
        Generate quiz questions based on topic and number of questions.
        """
        try:
            chain = self.prompt | self.llm
            result = chain.invoke({
                "topic": topic,
                "n": n_questions
            })
            return result.content
        except Exception as e:
            print(f"Error generating questions: {e}")
            return None

# Function to be called from streamlit app
def generate_questions(topic: str, n_questions: int) -> str:
    generator = QuizGenerator()
    return generator.generate(topic, n_questions)