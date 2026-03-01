from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(resume_text, job_desc):
    # Vectorizing the text to convert words into numbers
    documents = [resume_text, job_desc]
    count_vectorizer = TfidfVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(documents)
    
    # Calculating Cosine Similarity (The 'Match' % )
    results = cosine_similarity(sparse_matrix)
    return round(results[0][1] * 100, 2)

if __name__ == "__main__":
    job_description = "Seeking a Python developer with experience in Web Scraping, APIs, and Automation."
    my_resume = "Python developer skilled in building web scrapers, managing APIs, and system automation."
    
    score = calculate_score(my_resume, job_description)
    print(f"--- Resume Match Result ---")
    print(f"Match Score: {score}%")
    
    if score > 70:
        print("Strong Match for this role!")
    else:
        print("Needs improvement for this job description.")
