import blog_generate
import blog_summarise
from fastapi import FastAPI
from langserve import add_routes
import uvicorn

# LLM and chains to be used
llm = blog_generate.llm
chain = blog_generate.chain
rag_chain = blog_summarise.rag_chain

app = FastAPI(title = 'blog-generation',
              version = '1.8',
              description = 'An API for blog generation')
#Blog genreation
add_routes(
    app,
    chain, 
    path = "/blog-gen"
)

#Blog Summarization
add_routes(
    app,
    rag_chain,
    path = '/summarize/'
)

if __name__ == '__main__':
    uvicorn.run(app, host = 'localhost', port = 8000)
