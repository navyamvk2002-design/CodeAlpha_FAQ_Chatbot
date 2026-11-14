
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Step 1: Load FAQ dataset
faqs = pd.read_csv("faqs.csv")

# Step 2: Extract questions and answers
questions = faqs["question"].tolist()
answers = faqs["answer"].tolist()

# Step 3: Convert questions into numerical form
vectorizer = TfidfVectorizer(stop_words="english")
question_vectors = vectorizer.fit_transform(questions)


# Step 4: Create chatbot response function
def get_answer(user_question):

    # Convert user question into numerical form
    user_vector = vectorizer.transform([user_question])

    # Calculate similarity
    similarity_scores = cosine_similarity(
        user_vector, question_vectors
    )

    # Find the most similar question
    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[0][best_match_index]

    print("Similarity Score:", round(best_score, 2))

    # Check minimum similarity
    if best_score < 0.20:
        return "Sorry, I don't understand your question. Please try another question."

    # Return matching answer
    return answers[best_match_index]

