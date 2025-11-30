from google.adk.tools import google_search
from google.adk.agents import LlmAgent, SequentialAgent


# ----------------------------
# ORIGINAL AGENTS (UNCHANGED)
# ----------------------------

initial_writer = LlmAgent(
    model="gemini-2.5-flash",
    name='initial_writer_agent',
    description="Generates an SEO-friendly blog outline based on a topic.",
    instruction="""
You are BlogOutlineAgent.

Your job:
- Create a clear, SEO-friendly outline based on the given topic.

STRICT RULES:
1. Keep the entire output SHORT and TIGHT. No long titles, no long summaries.
2. Title must be under 50 characters.
3. Summary must be max 2 short sentences.
4. For each H2 section, give max 2 key points (very short).
5. DO NOT write paragraphs. Outline ONLY.
6. NO explanations of your process.
7. NO markdown (#, ##, etc).
8. NO backticks, NO triple quotes.
9. Output MUST be **valid JSON only** with the keys:
   {
      "title": "...",
      "summary": "...",
      "outline": {
         "Section 1": ["point 1", "point 2"],
         "Section 2": ["point 1", "point 2"]
      }
   }

If you include anything outside this JSON, you FAIL.
"""
)


content_writer = LlmAgent(
    model="gemini-2.5-flash",
    name="content_writer_agent",
    description="Expands the outline into a short plain-text blog using numbered sections.",
    instruction="""
You are ContentWriterAgent.

Your job:
- Expand the outline into a SHORT plain-text blog using ONLY numbers or simple bullets.
- DO NOT use markdown formatting (no #, ##, **, *, backticks, triple quotes).
- DO NOT output JSON, HTML, or markdown.
- DO NOT include tool messages, notes, or explanations.

OUTPUT RULES:
1. Use numeric section headers: "1. Section Title"
2. For subsections or points, use numbered subsections ("1.1 Subpoint") or simple bullets starting with "-" (choose one style per output).
3. Keep each section concise: MAX 2 short paragraphs per numbered section.
4. Preserve outline order exactly; do NOT add or remove sections.
5. Important sentences may be emphasized with surrounding asterisks only if necessary (e.g., *important sentence*), but avoid markdown syntax. Prefer plain text emphasis.
6. Keep total blog length SMALL (under 700–900 words).

FINAL OUTPUT:
Return ONLY the blog as plain text using the numeric/bullet format described above. No extra commentary, no metadata, no JSON.
""",

)



verify_witer = LlmAgent(
    model="gemini-2.5-flash",
    name="verify_writer_agent",
    description="Verifies the blog content against the original outline.",
    instruction="""
You are VerifierAgent.

Your output MUST be STRICT JSON ONLY.

FORMAT:
{
  "consistency_score": "0-100",
  "missing_sections": [],
  "accuracy_notes": [],
  "improvement_suggestions": []
}

RULES:
- NO markdown.
- NO paragraphs.
- NO natural language text.
- NO commentary.
- NO backticks.
- NO headings.
- Output JSON ONLY.
"""
)




# ... (Keep your initial_writer, content_writer, verify_witer definitions exactly as they are) ...

# ----------------------------
# FIXED PIPELINE
# ----------------------------


blog_pipeline = SequentialAgent(
    name="blog_pipeline_agent",
    description="Full blog generation pipeline: Outline -> Write -> Verify",
    sub_agents=[
        initial_writer,
        content_writer,
        verify_witer
    ]
)
# __all__ = ["initial_writer", "content_writer", "verify_witer"]





