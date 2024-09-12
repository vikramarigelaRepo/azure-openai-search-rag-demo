# Implement RAG with Azure Open AI Service and Azure AI Search Service
This Repo contains code to implement rag using azure open ai and azure ai search

# Project Overview
Employee Assistant is an Chat bot built using Azure open ai, Azure Search and python where employees can find answers to their ![alt text](image.png)questions regarding healthcare plans and company policies for a fictitious company called contoso.

![screenshot](application.png)!


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

 * Gradio+FastAPI+python is used to design UI for the chat application.

 * Key less authentication has been used for all services in this project. Azure AD Auth has been implemented for improved security for services to communicate with each other.

 * Following Roles have been used
 
   * For Azure App Service to connect with Azure Open AI Service
     * Role : Azure AI Developer

   * For Azure App Service to connect with Azure AI Search Service
     * Role: Search Service Contributor

   * For Azure Open AI Service to connect with Azure AI Search Service
     * Role: Search Index Data Reader
     * Role: Search Service Contributor
