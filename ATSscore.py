import docx2txt
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import ssl

# Test stopwords
try:
    stop_words = set(stopwords.words('english'))
    print(f"Stopwords loaded successfully. Example: {list(stop_words)[:10]}")
except Exception as e:
    print(f"Error accessing stopwords: {e}")

# Step 1: Extract Text from Job Description and Resume
def extract_text(file_path):
    """
    Extract text from a DOCX file.
    :param file_path: Path to the file
    :return: Extracted text as a string
    """
    return docx2txt.process(file_path)

# Step 2: Preprocess the Text
def preprocess_text(text):
    """
    Preprocess text by removing special characters, stopwords, and converting to lowercase.
    :param text: Input text string
    :return: Cleaned text string
    """
    stop_words = set(stopwords.words('english'))
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower()  # Convert to lowercase
    text = ' '.join(word for word in text.split() if word not in stop_words)  # Remove stopwords
    return text

# Step 3: Calculate Similarity
def calculate_similarity(text1, text2):
    """
    Calculate the similarity between two texts using TF-IDF and cosine similarity.
    :param text1: First text (job description)
    :param text2: Second text (resume)
    :return: Similarity score (0 to 100)
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return round(similarity[0][0] * 100, 2)

# Step 4: Main Function
def ats_application(job_desc_file, resume_file):
    """
    Main function to compute ATS match score.
    :param job_desc_file: Path to the job description file (DOCX)
    :param resume_file: Path to the resume file (DOCX)
    :return: Match score as a percentage
    """
    # Extract text
    job_description = extract_text(job_desc_file)
    resume = extract_text(resume_file)

    # Preprocess text
    job_description_clean = preprocess_text(job_description)
    resume_clean = preprocess_text(resume)

    # Calculate similarity score
    score = calculate_similarity(job_description_clean, resume_clean)
    return score

# Run the ATS Application
if __name__ == "__main__":
    # Update these paths to match your file locations
    job_description_path = "/Users/kondurisrinath/Desktop/Resumes/reportinganalyst.docx"
    resume_path = "/Users/kondurisrinath/Desktop/Resumes/SrinathBusinessAnalyst.docx"  # Ensure this is also correct

    try:
        match_score = ats_application(job_description_path, resume_path)
        print(f"ATS Match Score: {match_score}%")
    except FileNotFoundError as e:
        print(f"Error: {e}")

