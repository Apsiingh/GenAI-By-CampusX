from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

# You can set it to a folder on C: drive, or remove this line to use the default (C:\Users\<YourUser>\.cache\huggingface)
os.environ['HF_HOME'] = 'C:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=512
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is coding ?")
print(result.content)