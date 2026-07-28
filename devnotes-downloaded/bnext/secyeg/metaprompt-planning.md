# Meta-Prompt: Generate AI Agent Planning Documentation from Domain Research

## Context
You are assisting in creating AI agent-friendly planning documentation for a specialized domain (e.g., synthetic biology, research platform). A researcher has provided domain-specific documents (protocols, specifications, style guides, etc.). Your task is to generate a comprehensive planning framework that enables AI agents to autonomously create high-quality, consistent documentation within that domain.

## Input Analysis Phase

Before generating output, analyze the provided materials for:

### 1. Document Ecosystem
- What types of documents exist? (protocols, specs, tutorials, references, etc.)
- How do they relate to each other? (hierarchies, dependencies, cross-references)
- What is the primary use case? (research, implementation, education, reference)
- Who are the primary users? (researchers, developers, learners, practitioners)

### 2. Semantic Patterns
- What makes each document type semantically distinct?
- Are there consistent structural patterns within document types?
- How do documents signal purpose/intent to readers?
- What information appears in every document type vs. conditionally?

### 3. Syntax and Formatting Conventions
- What markup language/tool is used? (Markdown, MyST, reStructuredText, etc.)
- Are there domain-specific syntax patterns or custom directives?
- What formatting conventions are consistent across documents?
- Are there "anti-patterns" (things to avoid)?
- What Unicode characters or special symbols are used?

### 4. Quality Standards
- What makes a "good" document in this domain?
- What are common errors or validation issues?
- What cross-referencing patterns exist?
- Are there checklists or quality gates mentioned?

### 5. Terminology and Naming Conventions
- How are document titles constructed?
- Are there naming patterns for labels, links, references?
- What capitalization conventions are used?
- Are there domain-specific terms that need consistent treatment?

## Output Generation Phase

Generate two complementary guides:

### Guide 1: [Domain] Document Template Guide

**Purpose:** Help AI agents select and understand the appropriate structure for each document type.

**Structure:**
1. **Introduction** - What this guide is for and how to use it
2. **[For each document type]:**
   - Purpose statement (1 sentence)
   - YAML front matter template
   - Mandatory sections and ordering
   - Optional sections
   - Length expectations
   - Example titles/subtitles
   - Key features specific to this type
3. **Common Patterns** - Elements appearing across multiple types
4. **Selection Matrix** - Decision table: "I want to... → use this template"
5. **Validation Conventions** - Standards all documents must meet
6. **Document Relationship Diagram** (if complex) - How types connect

**Tone:** Directive and clear. Write as if instructing an AI agent.

### Guide 2: [Domain] Syntax Reference

**Purpose:** Document all syntax, directives, conventions, and patterns used in the domain.

**Structure:**
1. **Introduction** - Scope and how to use this reference
2. **[For each syntax element/directive]:**
   - Syntax/code block showing usage
   - Parameters and options
   - When to use it (semantic guidance)
   - Common variations
   - Examples in context
3. **Quick Reference Table** - All elements in compact form
4. **Common Errors** - Table of mistakes with solutions
5. **Validation Checklist** - What to verify before finalizing
6. **Index/Quick Lookup** - Easy navigation

**Tone:** Reference manual style. Be comprehensive and precise.

## Validation and Iteration Guidance

### Ask Yourself:
- Could an AI agent autonomously create a high-quality document using only these guides?
- Would an AI agent be able to catch its own errors using the validation checklist?
- Are the distinctions between document types clear enough to distinguish them?
- Have I captured the "why" behind conventions, not just the "what"?
- Would a domain expert recognize all the patterns and conventions?

### Questions for the Research Team:
1. Are there document types I missed?
2. Are the distinctions between types accurate?
3. Are there semantic or stylistic patterns I didn't capture?
4. What are the most common mistakes in documents?
5. Are there custom directives or extensions not documented?
6. How would you prioritize documents if resources were limited?
7. Are there edge cases or special scenarios I should document?

### Iteration Cycle:
1. Generate initial guides from domain materials
2. Have domain expert review for completeness/accuracy
3. Test with AI agent on sample document creation
4. Collect error patterns from AI-generated documents
5. Add those patterns to "Common Errors" section
6. Refine templates and syntax reference based on real-world usage
7. Repeat until consistency and quality thresholds are met

## Structure and Formatting Guidelines

### For Both Guides:
- Use consistent heading hierarchy
- Provide code/syntax examples for every concept
- Include tables for structured comparison
- Use descriptive section titles (not just "Example")
- Number sections for easy cross-reference
- Create visual distinction between directive and explanation
- Include "why" explanations, not just syntax

### For Templates Guide:
- Show actual YAML examples, not templates
- Include realistic subtitle/title examples
- Use "Example title formats" not generic placeholders
- Specify mandatory vs. optional sections clearly
- Explain section ordering when it matters

### For Syntax Reference:
- Show before/after: syntax → result
- Include parameter descriptions in table format
- Provide both simple and complex examples
- Highlight "Nucleus conventions" or "[Domain] conventions"
- Group related directives together

## Output Checklist

Before considering your work complete:

- [ ] Guide 1 helps identify correct document type
- [ ] Guide 1 provides all structural information needed
- [ ] Guide 2 covers all syntax/directives used in domain materials
- [ ] Guide 2 includes parameter explanations
- [ ] Both guides have clear "when to use" guidance
- [ ] Common errors are documented with solutions
- [ ] Validation checklists are present in both guides
- [ ] Examples are realistic and taken from actual documents
- [ ] Terminology is consistent with domain
- [ ] Cross-references between guides exist
- [ ] Unicode/special character conventions are specified
- [ ] Both guides assume an AI agent reader
- [ ] A domain expert would recognize all patterns

## Example Application

If you were given:
- 15 Process protocol documents
- 8 Module specification documents
- 3 DevNote examples
- 1 existing style guide
- 4 reference documents

You would:
1. Analyze each for semantic patterns
2. Identify the 7+ document types present
3. Create templates for each type
4. Document all directives and syntax used
5. Extract validation rules from existing documents
6. Create decision matrix showing when to use which type
7. Build quick-reference tables for lookup
8. Test against sample documents for completeness

---

## Refinement Prompts for Future Iterations

### When domain materials change:
"I have [added/modified/removed] the following [document types/syntax/conventions]. How should this affect the [Template Guide / Syntax Reference]?"

### When AI agents make mistakes:
"AI agents have made the following mistakes: [list]. How should the [Template Guide / Syntax Reference / validation checklist] be updated to prevent these?"

### When you need to add new document types:
"I need to create a new document type for [purpose]. Based on the existing structure, how should this fit into the Template Guide and Syntax Reference?"

### When testing with an AI agent:
"Generate a [document type] for [topic] using only the provided guides. Then validate it against the validation checklist. Report any ambiguities or missing information in the guides."