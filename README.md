# Implement RAG with Azure Open AI Service and Azure AI Search Service
This Repo contains code to implement rag using azure open ai and azure ai search

# Project Overview


# About RAG
Retrieval Augmented Generation (RAG) is an architecture that augments the capabilities of a Large Language Model (LLM) like ChatGPT by adding an information retrieval system that provides grounding data.
Two main components for implementing RAG is retriver and generator. In this project Azure AI Search Service is used as retriever and Azure Open AI Service as generator.

# Architecture diagram

![screenshot](archdiagram.png)!

 * App UX (web app) for the user experience
 * App server or orchestrator (integration and coordination layer)
 * Azure AI Search (information retrieval system)
 * Azure OpenAI (LLM for generative AI)

# Data Ingestion Overview





# Application Overview

Following azure services have been used to build this application. pfb..screenshot of the resource group. 

![screenshot](resourcegroup.png)!

 * AppService
 * Azure AI Search(used as Retriever)
 * Azure Open AI Service(Generative AI)
 * Azure Container Registry(Host docker images)
 * Azure Blob Storage(Data Source to upload files)

 * Gradio+FastAPI+python is used to design the chat application.

