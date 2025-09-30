# Raghav-Gupta-Langsmith-MAT496
## Langsmith Course Assignment - MAT496

This repository documents my progress through Modules 1 and 2 of the Langsmith course, fulfilling the requirements for video-by-video commits, learning summaries, and unique code examples.


## Module 1

### Lesson 1: Tracing Basics with @traceable
- **Learned:** Learned how to manually instrument Python functions using the @traceable decorator to create a nested run tree. This process is essential for logging custom code components and ensuring full observability of a Groq-based RAG pipeline within Langsmith.
- **Tweak:** Added custom name and descriptive metadata arguments (e.g., vectordb_type: FAISS, model_name: llama-3.3-70b-versatile) on the @traceable decorators for the core RAG functions to enrich the trace data with specific context.
- **Source File:** [lesson1_tracing_basics.ipynb](lesson1_tracing_basics.ipynb) 

 ### LESSON 2: Types Of Runs
 - **Learned:** Learned to correctly classify traces using the run_type parameter (llm, retriever) which enables special rendering in Langsmith. Also learned how to implement the reduce_fn for streaming outputs.
 - **Tweak:** Implemented all missing run_type and reduce_fn arguments, modified the LLM input to a coffee order, and customized the Retriever document content/metadata to create a unique example.
 - **Source File:** [lesson2_TypesOfRuns.ipynb](lesson2_TypesOfRuns.ipynb) 
