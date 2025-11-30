BlogAI Agent

A lightweight autonomous writing agent that thinks through topics, creates structured outlines, writes drafts, and refines them into clean, human-like articles.
This repo contains only the agent backend — no frontend yet.

Features

1. Multi-step reasoning pipeline

2. Topic interpretation

3. Outline generation

4. Draft writing

5. Self-refinement

6. Single-command execution

Getting Started
1. Move back to the project root
    If you’re inside a subfolder:
    cd ..

2. Create your .env file

At the root of your project, create a file named .env:

GOOGLE_API_KEY=your_key_here

3. Activate the virtual environment

PowerShell:

./venv/Scripts/Activate.ps1


If PowerShell blocks it:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

4. Run the agent
adk run my_agent

Project Structure
/my_agent/
    ├── agents/
    ├── workflows/
    ├── prompts/
    ├── .env
    ├── venv/
    └── README.md

How It Works
1. BlogAI runs through a clear reasoning sequence:
2. Interprets the topic
3. Breaks it into logical steps
4. Creates an outline
5. Writes a draft
6. Refines and cleans the final output
7. This ensures the writing feels intentional, not machine-dumped.

Current Status
1. Backend agent completed
2 .No UI
3. Fully functional autonomous writing pipeline

Planned Improvements
1. Add frontend for input/output
2. Add persistent memory for writing style
3. Add fact-checking sub-agent
4. Add SEO optimization mode
5. Support batch article generation
