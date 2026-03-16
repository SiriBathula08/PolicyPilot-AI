# PolicyPilot AI — Government Scheme Recommendation System

## Overview

PolicyPilot AI is an intelligent assistant that helps users discover relevant government schemes based on their eligibility.
The system uses **Retrieval-Augmented Generation (RAG)** and **semantic search** to match user queries with policy datasets.

## Live Demo

https://your-streamlit-app-link

## Features

* AI-powered policy recommendation
* Semantic search using embeddings
* Eligibility-based scheme matching
* Interactive web interface
* Fast vector search using FAISS

## Tech Stack

* Python
* Streamlit
* FAISS
* Sentence Transformers
* Retrieval-Augmented Generation (RAG)

## Architecture

1. User enters eligibility information
2. Query converted into embeddings
3. FAISS retrieves relevant policy documents
4. RAG pipeline generates recommendations

## Installation

```bash
git clone https://github.com/SiriBathula08/policypilot-ai
cd policypilot-ai
pip install -r requirements.txt
streamlit run app.py
```

## Future Improvements

* Integration with live government APIs
* Advanced eligibility scoring
* Multi-language support

## Author

Siri Bathula
