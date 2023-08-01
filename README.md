# LLM_for_Marketing_PR
Facilitating marketing through AI
-->>  AI-Enabled Customer Support Chatbot: Develop a chatbot that uses AI and natural language processing to provide automated customer support. It can understand customer queries, provide relevant information, and assist with common support issues, freeing up human support agents for more complex tasks.

## 1. Scope and Description
Use case:

The assistance chatbot is developed for AES Technologies, an automation company specializing in both home automation (smart home, automated doors, etc.) and industrial automation.

Description/Scope:

When a prospective client is considering awarding their automation project, they typically go through a pitching stage where different automation companies market themselves as the best fit for the project. The implementation of the chatbot will be integrated into AES Technologies' website, providing a unique and personalized login for each client they serve.
Through the chatbot, clients can access a virtual assistant that assists with basic troubleshooting and problem-solving related to any AES system in their home. This immediate support offers critical stopgaps before technicians physically address the issues, ensuring a smoother and more efficient experience for the clients.

By providing clients with a personalized virtual assistant and timely support, AES Technologies gains a significant marketing edge over other companies. The chatbot's effectiveness in resolving issues and enhancing customer satisfaction leads to increased client retention and positions AES Technologies as a preferred automation company, ultimately resulting in securing more contracts after the pitching stage.


## 2. Installation

  Clone the repository on bash:
  
  git clone https://github.com/your_username/your_repository.git
  cd your_repository
  Install the required dependencies in requirements.txt file

## 3. Usage

-Ensure you have your API keys for OpenAI and Pinecone.

-Place the PDF file containing the knowledge base for the chatbot in a known location and update the file_path variable in the main() function with the appropriate file path.

-Run the Streamlit app

    Authentication
    Before accessing the chatbot, users will be prompted to enter their username and password. The default username and password are provided in the code. For      a production environment, implement a more secure authentication mechanism.
    
    Features
    
    Personalized Virtual Technical Assistant for automatic sliding door systems.
    
    Accurate responses based on a knowledge base from a PDF knowledge base.
    
    Handles queries related to error codes and general technical issues.
    
    Provides possible solutions and stopgaps while waiting for physical technician support.
    
    Greeting, personalization, and context-aware responses.
    
    Secure user authentication.
    
## 4. Acknowledgments

- Streamlit for the simple and powerful app creation platform.

- Langchain for the NLP framework used for question-answering.

- Pinecone for the vector index service used for fast and efficient retrieval.

- OpenAI for providing language models and embeddings.

## **PS:**

1.) marketing_PR.ipynb is the python file that implements the same project in a python notebook. Here, the pinecone database for storing embeddings is created and populated with the knowledge base embeddings(OPENAI).

2.) marketing_PR2.ipynb is also python notebook that implements the project but with hugging face.

3.) marketing_PR_streamlitapp.py is the optimized streamlit app nased on marketing_PR.ipynb notebook.

