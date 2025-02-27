import streamlit as st
import random

# Welcome message
st.title("📚 WRT 102 Study Chatbot")
st.write("""
This study tool was created in collaboration with **Professor Zoë** to help you engage with key vocabulary and concepts from class.

**Important disclaimer:** To make studying more fun, this bot generates example sentences featuring **Professor Zoë**—grading papers, doing research, making arguments, and more. If you see them hypothetically publishing a groundbreaking theory or single-handedly revolutionizing composition studies… well, that’s just the bot getting creative.

### Choose your study mode:
""")

# User selects difficulty mode
difficulty = st.radio("Select a mode:", ["Easy Mode (hints available)", "Challenge Mode (no hints)"])

# Initialize session state for tracking stats
if "session_stats" not in st.session_state:
    st.session_state.session_stats = {"correct": 0, "incorrect": 0, "attempts": 0}

# Full Vocabulary List
vocab_list = [
    ("Eloquence", "The ability to communicate ideas effectively and persuasively through speech or writing.",
     "Professor Zoë delivers a lecture on rhetorical strategies with such clarity and persuasion that students feel inspired to refine their own writing."),
    
    ("Critical Thinking", "The process of analyzing and evaluating information objectively to form a reasoned judgment.",
     "Professor Zoë evaluates a new AI writing tool by questioning its biases, accuracy, and implications for student learning."),
    
    ("Rhetorical Situation", "The relationship between author, audience, and text.",
     "Before designing an assignment, Professor Zoë considers their students' prior knowledge, the course goals, and the best way to structure instructions to guide learning."),
    
    ("Objective", "Information that is based on facts, independent of personal feelings or opinions.",
     "When grading essays, Professor Zoë uses a rubric to ensure fairness and consistency rather than relying on personal preferences."),
    
    ("Subjective", "Information influenced by personal opinions, emotions, or perspectives.",
     "Professor Zoë prefers essays with strong narrative elements, but they recognize that preference as a personal perspective rather than an objective rule."),
    
    ("Analyze", "To examine something carefully by breaking it into parts and determining how those parts relate to each other.",
     "Before presenting a research paper at a conference, Professor Zoë breaks down key arguments, examines their supporting evidence, and identifies possible counterarguments."),

    ("Evaluation", "The process of making a judgment about the quality, significance, or effectiveness of something.",
     "Professor Zoë assesses a student’s essay by determining whether the thesis is well-supported with clear reasoning and strong evidence."),

    ("Reason (verb)", "To think logically and draw conclusions based on evidence and analysis.",
     "Professor Zoë constructs an argument about multimodal literacy by logically linking research findings with classroom observations."),

    ("Primary Source", "An original document or firsthand account created at the time of an event or by someone with direct experience.",
     "To study historical rhetoric, Professor Zoë examines an original speech by Sojourner Truth rather than relying on secondary analyses."),

    ("Secondary Source", "A text that analyzes, interprets, or summarizes information from primary sources.",
     "For an upcoming journal article, Professor Zoë cites scholarly essays that analyze classical rhetorical theories."),

    ("Scholarly and Peer-reviewed", "Work that has been evaluated by experts in the field before publication to ensure quality and credibility.",
     "Professor Zoë submits an article on digital rhetoric to an academic journal, where it undergoes review by other experts before publication."),

    ("Close Reading", "A detailed and careful analysis of a text’s language, structure, and meaning.",
     "While preparing for a lecture, Professor Zoë carefully examines a passage from *Writing About Writing* to highlight its rhetorical strategies."),

    ("Conversational Inquiry", "A method of exploring ideas by engaging in dialogue and questioning assumptions.",
     "During a faculty meeting, Professor Zoë poses an open-ended question about AI in writing instruction, prompting discussion among colleagues."),

    ("Literary Analysis", "The study of literature by examining themes, structure, and writing techniques to interpret meaning.",
     "Professor Zoë writes an article on how 19th-century literature reflects shifting views on authorship and originality."),

    ("Genre Analysis", "The study of how different types of writing follow specific conventions based on audience and purpose.",
     "Professor Zoë studies how professional cover letters differ from academic essays to help students adapt their writing to different audiences."),

    ("Rhetorical Analysis", "The examination of how an author persuades an audience using rhetorical strategies like ethos, pathos, and logos.",
     "For a conference presentation, Professor Zoë analyzes how politicians use social media to craft persuasive narratives."),

    ("Research Paper", "An academic document that presents an argument supported by evidence from credible sources.",
     "Professor Zoë writes a research paper on how first-year composition students transfer writing skills to other disciplines."),

    ("Thesis", "A clear, specific claim that expresses the main argument of an essay or research paper.",
     "Professor Zoë argues in a published article that multimodal composition should be a core part of first-year writing curricula."),

    ("Hypothesis", "A testable statement predicting a possible outcome, often used in research.",
     "Professor Zoë predicts that students who engage in regular peer feedback will show greater improvements in revision skills."),

    ("Term Paper", "A long academic essay, usually written over a semester, that demonstrates deep research and analysis on a topic.",
     "Professor Zoë assigns a final research paper that requires students to synthesize multiple sources on a rhetorical concept."),

    ("Threshold Concept", "A core idea in a discipline that changes how students understand a subject and enables deeper learning.",
     "Professor Zoë teaches that writing is a recursive process, a fundamental idea students must grasp to develop as writers."),

    ("Writing as Product", "The final version of a written work, completed and polished for submission or publication.",
     "After months of research and revisions, Professor Zoë submits a finalized book chapter for publication."),

    ("Writing as Process", "The steps involved in developing a piece of writing, including brainstorming, drafting, revising, and editing.",
     "Professor Zoë revises a manuscript multiple times, incorporating peer feedback and refining their argument before submission."),

    ("Construct (noun)", "An idea or concept that is socially or culturally developed rather than naturally occurring.",
     "Professor Zoë challenges students to rethink the construct that 'good writing' always follows a rigid five-paragraph structure."),

    ("Transfer", "The ability to apply skills or knowledge learned in one context to a new, different context.",
     "Professor Zoë helps students apply rhetorical strategies learned in class to their professional emails and job applications."),

    ("Near Transfer", "Applying knowledge to a similar situation, where the differences are minimal.",
     "Professor Zoë designs an assignment where students apply rhetorical strategies from essay writing to writing discussion posts."),

    ("Far Transfer", "Applying knowledge to a completely different situation that requires adaptation.",
     "Professor Zoë explores how students use storytelling techniques from composition courses in public speaking contexts."),

    ("Form vs. Content", "The distinction between how something is structured (form) and what it communicates (content).",
     "Professor Zoë reminds students that a beautifully formatted paper (form) still needs strong ideas and evidence (content) to be persuasive."),

    ("Narrative", "A form of writing that tells a story or recounts events in a structured way.",
     "Professor Zoë shares a personal story in a journal article to illustrate how their teaching philosophy developed over time."),

    ("Essay", "A structured written composition that presents an argument or explores a topic in depth.",
     "Professor Zoë assigns an essay where students argue for the most effective way to teach writing in the digital age."),

    ("Paragraph", "A group of related sentences that develop a single main idea within a larger piece of writing.",
     "Professor Zoë revises a paragraph in their research paper to ensure each sentence clearly builds on the previous one."),

    ("Point of View (1st person)", "A writing perspective where the narrator is the speaker, using 'I' or 'we'.",
     "In an article, Professor Zoë writes: 'I have observed that students engage more deeply when given real-world writing tasks.'"),

    ("Point of View (2nd person)", "A writing perspective where the narrator addresses the reader directly, using 'you'.",
         "In a syllabus, Professor Zoë writes: 'You will develop critical reading and writing skills throughout this course.'"),

    ("Point of View (3rd person)", "A writing perspective where the narrator is outside the story, using 'he,' 'she,' or 'they'.",
         "In a research article, Professor Zoë writes: 'The study found that first-year students benefit from structured peer feedback sessions.'"),

    ("Focus", "The clarity and specificity of a written work’s main idea or purpose.",
         "Professor Zoë advises a student to narrow their essay focus from 'education reform' to 'the impact of grading policies on student motivation.'"),

    ("Scope of Essay", "The range and limitations of what an essay will cover.",
         "Professor Zoë structures a writing assignment to ensure students don’t tackle overly broad topics in their essays."),

    ("Citation Style", "A standardized format for documenting sources, such as MLA, APA, or Chicago.",
         "Professor Zoë reminds students to format their citations correctly in MLA or APA style depending on their discipline."),

    ("Convention vs. Rule", "A writing convention is a generally accepted practice, while a rule is a strict requirement.",
         "Professor Zoë explains that using contractions in academic writing is a convention, while citing sources is a strict rule."),

    ("Brainstorm/Prewrite", "A method of generating ideas before starting a draft, such as listing, clustering, or freewriting.",
         "Before drafting an article, Professor Zoë lists all potential research angles and organizes their thoughts."),

    ("Free-write", "A technique where a writer continuously writes without concern for structure or correctness to generate ideas.",
         "Before revising a conference talk, Professor Zoë free-writes ideas to refine their key points."),

    ("Outline", "A structured plan that organizes main points and supporting details before drafting an essay.",
         "Professor Zoë outlines a book chapter, ensuring each section builds logically toward the main argument."),

    ("Draft", "A preliminary version of a written work, which undergoes revision before completion.",
         "Professor Zoë writes a first draft of an article, knowing that revisions will come later."),

    ("Compose", "The act of writing or assembling a text with intention and structure.",
         "Professor Zoë sits down to compose a keynote speech for an academic conference."),

    ("Revise", "The process of improving a written work by reorganizing content, clarifying ideas, and strengthening arguments.",
         "Professor Zoë reworks a journal submission after receiving peer review feedback."),

    ("Edit", "The process of correcting grammar, spelling, punctuation, and mechanics in a written work.",
         "Before submitting an article, Professor Zoë corrects typos, grammar mistakes, and formatting inconsistencies."),

    ("Format", "The way a document is arranged according to specific guidelines, including margins, font, and spacing.",
         "Professor Zoë ensures their manuscript follows the journal’s formatting guidelines before submission."),

    ("Peer Workshop", "A session where writers share drafts and receive constructive feedback from peers.",
         "Professor Zoë facilitates a peer workshop where students give each other constructive feedback on drafts."),

    ("Conference (1:1)", "A meeting between a writer and an instructor or mentor to discuss writing progress and receive feedback.",
         "Professor Zoë meets with a student one-on-one to discuss how to refine their thesis statement."),

]

# Flashcard mode
st.write("\n---\n### 📖 Flashcard Review Mode")
st.write("Use flashcards to review key vocabulary words before testing yourself in the quiz. Each time you click 'Give me a Word!', a new word will appear.")

if st.button("Give me a Word!"):
    term, definition, example = random.choice(vocab_list)
    st.subheader(f"📖 Term: {term}")
    st.write(f"**Definition:** {definition}")
    st.write(f"**Example:** {example}")

# Quiz mode - Displaying all 15 questions at once
st.write("\n---\n### 📝 Quiz Mode")

# Initialize session state for quiz if not already set
if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = random.sample(vocab_list, 15)
    st.session_state.user_answers = {}
    st.session_state.quiz_options = {}  # Store answer options to prevent reshuffling
    st.session_state.quiz_types = {}  # Store question type for stability

# Ensure `quiz_types` exists before accessing it
if "quiz_types" not in st.session_state:
    st.session_state.quiz_types = {}

# Store user selections
for i, (term, correct_definition, correct_example) in enumerate(st.session_state.quiz_questions):

    # Ensure each question keeps the same type (definition or example) throughout
    if i not in st.session_state.quiz_types:
        st.session_state.quiz_types[i] = random.choice(["definition", "example"])

    question_type = st.session_state.quiz_types[i]  # Retrieve stored type

    # Store options in session state so they don't reshuffle
    if i not in st.session_state.quiz_options:
        if question_type == "definition":
            options = random.sample([d for _, d, _ in vocab_list if d != correct_definition], 2)
            options.append(correct_definition)
            random.shuffle(options)
        else:
            options = random.sample([e for _, _, e in vocab_list if e != correct_example], 2)
            options.append(correct_example)
            random.shuffle(options)

        st.session_state.quiz_options[i] = options  # Save options for this question

    # Display question with stable options and question type
    st.subheader(f"🔹 Question {i+1}: {'What is the best definition of' if question_type == 'definition' else 'Which is the best example of'} '{term}'?")
    st.session_state.user_answers[i] = st.radio(f"Select an answer for Question {i+1}:", st.session_state.quiz_options[i], key=f"q{i}")

# Button to submit answers and grade all at once
if st.button("Submit Answers"):
    correct_count = 0

    # Grade answers
    for i, (term, correct_definition, correct_example) in enumerate(st.session_state.quiz_questions):
        question_type = st.session_state.quiz_types[i]  # Use the stored question type
        correct_answer = correct_definition if question_type == "definition" else correct_example

        if st.session_state.user_answers[i] == correct_answer:
            correct_count += 1
        else:
            st.error(f"❌ Question {i+1}: Incorrect! The correct answer was: {correct_answer}")

    # Display summary
    st.success(f"✅ You got {correct_count} out of 15 correct!")

    # Instructions for reloading the quiz
    st.write("\n---\n")
    st.write("🔄 **Want to try again?** Refresh the page to get 15 new words! Click the reload button in your browser or press **Cmd + R** (Mac) / **Ctrl + R** (Windows).")