import streamlit as st
from quiz_generator import generate_questions

class QuizApp:
    def __init__(self):
        self.initialize_session_state()
        self.setup_page_config()
        self.apply_custom_styles()
        self.render_ui()

    def initialize_session_state(self):
        """Initialize session state variables"""
        if "quiz_data" not in st.session_state:
            st.session_state.quiz_data = []
        if "user_answers" not in st.session_state:
            st.session_state.user_answers = []
        if "quiz_generated" not in st.session_state:
            st.session_state.quiz_generated = False
        if "score" not in st.session_state:
            st.session_state.score = 0

    def setup_page_config(self):
        """Configure the Streamlit page"""
        st.set_page_config(
            page_title="Interactive Quiz App",
            page_icon="📚",
            layout="centered"
        )

    def apply_custom_styles(self):
        """Apply custom CSS styles"""
        st.markdown("""
            <style>
            .stTitle {
                color: #2E4053;
                text-align: center;
                padding: 20px;
            }
            .quiz-container {
                border-radius: 15px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .topic-input {
                background-color: white;
                padding: 10px;
                border-radius: 8px;
            }
            .stRadio > label {
                font-size: 1.1rem;
            }
            </style>
        """, unsafe_allow_html=True)

    def parse_quiz(self, quiz_text: str) -> list:
        """Parse the quiz text into a structured format"""
        questions = []
        current_question = None
        
        if quiz_text:  # Check if quiz_text is not None
            lines = quiz_text.strip().split("\n")
            
            for line in lines:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                    
                if line.startswith("Question:"):
                    if current_question:
                        questions.append(current_question)
                    current_question = {"question": line.replace("Question:", "").strip(), 
                                      "options": [], 
                                      "correct": ""}
                elif line and line[0] in "abcd" and current_question is not None:
                    current_question["options"].append(line)
                elif line.startswith("Correct answer:") and current_question is not None:
                    current_question["correct"] = line.replace("Correct answer:", "").strip()[0]
            
            if current_question:  # Add the last question
                questions.append(current_question)
                
        return questions

    def generate_quiz(self, topic: str, n_questions: int):
        """Generate quiz questions"""
        try:
            questions_text = generate_questions(topic, n_questions)
            if questions_text:
                st.session_state.quiz_data = self.parse_quiz(questions_text)
                st.session_state.user_answers = [None] * len(st.session_state.quiz_data)
                st.session_state.quiz_generated = True
                # st.success("Quiz generated successfully! Scroll down to start.")
            else:
                st.error("Failed to generate quiz. Please try again.")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")

    def display_quiz(self):
        """Display the quiz questions"""
        st.markdown("---")
        for i, question in enumerate(st.session_state.quiz_data):
            with st.container():
                st.markdown(f"### Question {i + 1}")
                st.markdown(f"**{question['question']}**")
                st.session_state.user_answers[i] = st.radio(
                    "Select your answer:",
                    question['options'],
                    key=f"q{i + 1}_answer",
                    index=None,
                    horizontal=True
                )
            st.markdown("---")

    # def calculate_score(self):
    #     """Calculate the quiz score"""
    #     correct_count = 0
    #     for question, answer in zip(st.session_state.quiz_data, st.session_state.user_answers):
    #         if answer and answer[0] == question["correct"]:
    #             correct_count += 1
    #     return correct_count, (correct_count / len(st.session_state.quiz_data)) * 100

    def display_results(self):
        """Display quiz results"""
    #     correct_count, score_percentage = self.calculate_score()
    #     
    #     st.markdown(f"""
    #         <div style='text-align: center; padding: 20px; border-radius: 10px; background-color: #f0f2f6;'>
    #             <h2>Quiz Complete! 🎉</h2>
    #             <h3>Your Score: {correct_count}/{len(st.session_state.quiz_data)} ({score_percentage:.1f}%)</h3>
    #         </div>
    #     """, unsafe_allow_html=True)

        for i, (question, answer) in enumerate(zip(st.session_state.quiz_data, st.session_state.user_answers)):
            selected_letter = answer[0] if answer else "No answer"
            is_correct = answer and answer[0] == question["correct"]
            
            with st.expander(f"Question {i + 1} {'✅' if is_correct else '❌'}"):
                st.markdown(f"**{question['question']}**")
                for option in question['options']:
                    if option[0] == question["correct"]:
                        st.markdown(f"✅ **{option}** (Correct Answer)")
                    elif answer and option[0] == selected_letter:
                        st.markdown(f"❌ ~~{option}~~ (Your Answer)")
                    else:
                        st.markdown(f"- {option}")

    def reset_quiz(self):
        """Reset the quiz state"""
        if st.button("📝 Try Another Quiz", type="primary"):
            st.session_state.quiz_generated = False
            st.session_state.quiz_data = []
            st.session_state.user_answers = []
            st.session_state.score = 0
            st.experimental_rerun()

    def render_ui(self):
        """Render the main user interface"""
        st.markdown("""
            <h1 style='text-align: center; color: #2E4053; margin-bottom: 30px;'>
                🎓 Interactive Quiz Generator ✨
            </h1>
        """, unsafe_allow_html=True)

        with st.container():
            st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                topic = st.text_input(
                    "Quiz Topic",
                    value="General Knowledge",
                    placeholder="Enter topic..."
                )
            with col2:
                n_questions = st.number_input(
                    "Number of Questions",
                    min_value=1,
                    max_value=10,
                    value=3
                )

            if st.button("🎲 Generate Quiz", type="primary", use_container_width=True):
                self.generate_quiz(topic, n_questions)
            
            st.markdown("</div>", unsafe_allow_html=True)

        if st.session_state.quiz_generated:
            self.display_quiz()
            if st.button("📊 Show Results", type="primary"):
                self.display_results()
                self.reset_quiz()

if __name__ == "__main__":
    quiz_app = QuizApp()