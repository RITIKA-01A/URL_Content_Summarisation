import validators,streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader


## Streamlit app
st.title(" Lnagchain:Summarize the text from YT or Website")
st.subheader('Summarise URL')

## Get the Groq api key amd the url
with st.sidebar:
    groq_api_key=st.text_input("Groq API Key" , value="",type="password")

generic_url=st.text_input("URL",label_visibility="collapsed")

## LLM Model
# llm=ChatGroq(groq_api_key=groq_api_key,model_name="Gemma-7b-It")
prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}
"""
prompt = PromptTemplate(
    template=prompt_template,
    input_variables=['text']

)

if st.button("Summarize the content from the YT or Website"):
    ## Validate the input
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information")

    elif not validators.url(generic_url):
        st.error("Please enter a vlaid url.It may be a YT video or a website url")

    else:
        try:
        #     with st.spinner("Waiting..."):
        #         ##loading the data
        #         if "youtube.com" in generic_url:
        #             loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=True)
        #         else:
        #             loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
        #                                          headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"})
                    
        #         docs = loader.load()

        #         ## Chain
        #         llm=ChatGroq(groq_api_key=groq_api_key,model_name="Gemma-7b-It")
        #         chain = load_summarize_chain(llm=llm,
        #                                      chain_type="stuff",
        #                                      prompt=prompt)
        #         summary = chain.run(docs)
        #         st.success(summary)

        # except Exception as e:
        #     # st.Exception(f"Exception:{e}")
        #     st.error(f"Exception: {e}")
        
            st.write(f"Trying: {generic_url}")
            
            if "youtube.com" in generic_url:
                loader = YoutubeLoader.from_youtube_url(generic_url)
            else:
                loader = UnstructuredURLLoader(
                    urls=[generic_url],
                    ssl_verify=False,
                    headers={
                        "User-Agent": "Mozilla/5.0",
                        "Accept": "text/html,application/xhtml+xml",
                        "Accept-Language": "en-US,en;q=0.9"
                    }
                )

            docs = loader.load()
            st.write(f"Loaded {len(docs)} docs")
            st.write(docs[0].page_content[:500])  # Preview content

            llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma-7b-It")
            chain = load_summarize_chain(llm=llm, chain_type="stuff", prompt=prompt)
            summary = chain.run(docs)
            st.success(summary)

        except Exception as e:
            st.error(f"Exception: {e}")
            st.exception(e)


