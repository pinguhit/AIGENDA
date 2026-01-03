# CalcBot – AI-Powered Calculus Problem Solver

## Overview
CalcBot is an AI-powered application designed to solve calculus problems from both text and images. The system supports step-by-step solutions for calculus operations such as differentiation and integration.

The application uses a large language model through the Google Gemini API and integrates OCR-based image handling to process handwritten or printed calculus problems. The interface is built using Streamlit for ease of use and rapid interaction.

## Features
- Solves calculus problems from text input
- Supports image-based problem input using OCR
- Step-by-step solution generation
- Handles differentiation and integration problems
- Simple and interactive web-based interface

## System Architecture
- Frontend: Streamlit web application
- Backend: Python-based inference pipeline
- AI Model: Google Gemini API
- OCR: Image-to-text processing for math problems

## Tech Stack
- Programming Language: Python
- Web Framework: Streamlit
- AI Model API: Google Gemini
- OCR: Image processing pipeline
- Tools: VS Code, Google Colab

## Workflow
1. User inputs a calculus problem as text or uploads an image
2. Image inputs are processed using OCR to extract mathematical expressions
3. The extracted text is sent to the Gemini API
4. The model generates a step-by-step solution
5. The solution is displayed through the Streamlit interface


## Use Cases
- Solving calculus homework problems
- Educational assistance for students
- AI-assisted mathematical problem solving
- Demonstrating applied generative AI workflows

## Future Improvements
- Support for advanced calculus topics
- Improved OCR accuracy for handwritten equations
- Expression parsing using symbolic math libraries
- Deployment as a hosted web application
