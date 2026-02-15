from langchain_core.prompts import PromptTemplate
# template
template=PromptTemplate(
    
    template="""Please summarize the research paper titled '{paper_input}' with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    1. Mathematical Details:
     - Include relevant mathematical equations if present in the paper.
     - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
    2. Analogies:
     - Use relatable analogies to simplify complex ideas.
    Ensure the summary is clear, concise, accurate, and aligned with the provided style.""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True,  # validates where all the variables mentioned in the template matches with the variables mentioned in the input_variables
)

template.save('template.json')