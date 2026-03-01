# ai-resume-analyzer
An intelligent recruitment tool that uses Natural Language Processing (NLP) to automate the candidate screening process. This project calculates the semantic similarity between a Resume and a Job Description to identify the best-fit candidates.

The Logic Behind the Project
This isn't a simple keyword search. The tool uses:

TF-IDF Vectorization: Converts text data into a numerical matrix, highlighting unique technical terms while downplaying common words (like "the", "and").

Cosine Similarity: A mathematical metric used to measure how similar two documents are, regardless of their size. It calculates the cosine of the angle between two vectors in a multi-dimensional space.

 Key Features
Semantic Analysis: Goes beyond "keyword stuffing" to understand document context.

Automated Scoring: Provides a percentage-based match score (0-100%).

Hiring Logic: Integrated threshold alerts to flag "Strong Matches" automatically.

Efficiency: Capable of processing and comparing text data in milliseconds.

 Tech Stack
Language: Python 3.10+

ML Library: scikit-learn (Vectorization & Similarity metrics)

Data Handling: NumPy (Backend matrix operations)

📝 Future Enhancements
[ ] Integration with PyPDF2 to allow direct PDF uploads.

[ ] Multi-resume batch processing for HR teams.

[ ] Keyword extraction to suggest missing skills to the user.
