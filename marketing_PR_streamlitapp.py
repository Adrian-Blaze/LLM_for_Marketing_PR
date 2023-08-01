import os
import pinecone
import streamlit as st
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms.openai import OpenAI
from langchain.vectorstores import Pinecone

def main():
    
    st.title("Integrated AI chatbot")

    file_path = f'C:/Users/user/Desktop/AES automatic electronic Slide user guide.pdf'
    os.environ["OPENAI_API_KEY"] = "sk-xxx"
    pinecone.init(api_key="xxx", environment="northamerica-northeast1-gcp")
    loader = UnstructuredPDFLoader(file_path)
    pages = loader.load()
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    doc_splitter = RecursiveCharacterTextSplitter(chunk_size = 512, chunk_overlap = 50)
    new_pdf2 = doc_splitter.split_documents(pages)
    embeddings = OpenAIEmbeddings()
    index_name = "marketing-pr"
    db = Pinecone.from_existing_index(index_name=index_name, embedding=embeddings)
    retriever = db.as_retriever()
    # Define the template for the language model prompt
    template =  """
            You are a virtual technician designed to provide support and information to clients on automatic sliding door systems.\
            Your objective is to provide accurate and simplified responses to a wide range of \
            automatic sliding door systems questions, based on your knowledge base. \

            If a user's query indicates an error code or number, go through document to give possible reasons and remedies to the issue\
            

            In your responses, ensure a tone of professionalism, understanding and expertise. Provide users with \
            possible solutions and stop gaps to their issues pending when the physical technician will arrive \
        

            Here are some specific interaction scenarios to guide your responses:
            - If the- user asks what you can do, respond with "I'm a virtual technician here to provide \
            first aid support and information on the technical issue you are experiencing. How can I assist you?"
            - If the user starts with a greeting, respond with 'Hello! How are you doing today? How can I assist you?' \
            or something related to that
            - If a user shares their name, use it in your responses when appropriate, to cultivate a more personal and \
            comforting conversation.

            - If the exact question is not available, ask the user to reboot the system and then provide a suggestion based on the second nearest answer from the pdf.\
            - If a user asks a question that is unrelated to automated systems, respond with \
            'This question is out of my scope as I'm built mainly as a first aid support for our electronic systems in your facility \
            Could you please ask a question related to our automated systems?'

            {context}
            Question: {question}
            Answer:"""

    # Create a prompt template
    prompt = PromptTemplate(template=template, input_variables=["context", "question"])
    chain_type_kwargs = {"prompt": prompt}
    #Initialize the OpenAI module, load and run the retrieval QA chain
    llm = OpenAI(temperature=0)
    chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs=chain_type_kwargs,
    verbose=True
    )
    #while True:
    password = 'zummit'
    user = st.text_input("Username",  key='user')
    pw = st.text_input("Password",  key='pw', type='password')
    validate = st.checkbox("Validate")
    if validate:

        if pw != password:
            st.error('Please, enter correct validation details')
            
                    
        else:
            st.success( 'Welcome, '+ user + '. Client access confirmed')
            st.subheader("AES First-Aid Virtual Technical Assistant")
            user_question = st.text_input("How can we assist you today?")

            if user_question:
                answer = chain.run(user_question)
                styled_container = '''
                    #   <div style="background-color: #F5F5F5; padding: 10px; border-radius: 5px;">
                    #  <p style="font-size: 20px; color: gray; font-weight: bold;">{}</p>
                    # </div>
                    #                '''.format(answer)

                st.write(styled_container, unsafe_allow_html=True)
                #st.write(answer)


    # Run the Streamlit app
if __name__ == "__main__":
    main()
