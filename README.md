
# PolicyPilot AI

PolicyPilot AI is an AI-powered assistant that recommends government schemes based on a user's profile and questions.

The system uses semantic search, embeddings, and a multi-agent architecture to match users with relevant policies.

## Features

- Eligibility scoring
- Scheme recommendation
- Semantic policy search
- AI policy assistant chatbot
- Streamlit web interface

## Tech Stack

Python  
Streamlit  
Sentence Transformers  
FAISS Vector Database  
Pandas  

## Project Structure

PolicyPilot_AI

app/ – Streamlit web interface  
agents/ – AI agents for eligibility, recommendation, retrieval, and chat  
data/ – policy dataset  

## Installation

Clone the repository

git clone https://github.com/yourusername/PolicyPilot-AI.git

Install dependencies

pip install -r requirements.txt

Run the application

streamlit run app/app.py

## Example

User input

Occupation: Farmer  
Income: 200000  

Output

Recommended schemes:

PM-KISAN  
Ayushman Bharat  
PM Fasal Bima Yojana

## Future Improvements

- Larger policy dataset
- Deployment to cloud
- Advanced agent orchestration
=======
# PolicyPilot-AI
AI-powered government policy recommendation system using RAG, embeddings, and multi-agent architecture.

