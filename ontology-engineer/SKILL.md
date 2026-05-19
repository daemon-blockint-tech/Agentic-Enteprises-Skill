---
name: ontology-engineer
description: |
  Design ontologies and build knowledge graphs.
  Cover OWL/RDF ontologies, SKOS taxonomies, SPARQL querying, knowledge graph construction,
  semantic reasoning, and linked data patterns.
  Triggers on "build ontology", "design knowledge graph", "create taxonomy",
  "SPARQL query", "semantic reasoning", "linked data", "RDF modeling",
  "ontology alignment", or "knowledge representation".
---

# Ontology Engineer

## Overview

Design ontologies and build knowledge graphs. This skill covers OWL/RDF ontologies, SKOS taxonomies,
SPARQL querying, knowledge graph construction, semantic reasoning, and linked data patterns.

## Features

- OWL/RDF ontology design: classes, properties, restrictions, axioms
- SKOS taxonomy creation: concepts, hierarchies, labels, mappings
- SPARQL querying: SELECT, CONSTRUCT, ASK, DESCRIBE patterns
- Knowledge graph construction: data extraction, entity resolution, graph loading
- Semantic reasoning: rule-based inference, OWL reasoning, consistency checking
- Linked data patterns: URIs, dereferencing, RDF serialization, data publishing

## Usage

1. Identify the user's ontology need (design, taxonomy, querying, or knowledge graph)
2. Follow the corresponding workflow below
3. Produce structured outputs: OWL files, SKOS taxonomies, SPARQL queries, or knowledge graph schemas

## Examples

- **User**: "Design an ontology for products"
  **Agent**: Runs Ontology Design workflow, defines classes (Product, Category, Feature), properties (hasCategory, hasFeature), produces OWL file

- **User**: "Write a SPARQL query"
  **Agent**: Runs Querying workflow, constructs SELECT query with graph patterns, filters, and aggregations

- **User**: "Build a knowledge graph"
  **Agent**: Runs Knowledge Graph Construction workflow, extracts entities, resolves duplicates, loads into triple store

## When to Use

- Scoping domains with competency questions and designing OWL/RDF ontologies
- Building knowledge graphs, entity resolution, and linked-data integration
- Writing SPARQL, Cypher, or graph validation and reasoning workflows
- Selecting semantic-web or property-graph tools and reuse from public ontologies

## When NOT to Use

- Relational warehouse star schemas or batch ETL → use `data-warehouse-engineer`
- Enterprise data platform vendor selection or mesh operating model → use `data-architect`
- LLM system prompts, agents, or RAG orchestration → use `prompt-engineer`
- Business requirements workshops without semantic modeling → use `business-analyst`

## Core Workflows

### 1. Ontology Design Workflow

**Phase checklist:**

1. **Scope & competency questions**
   - Define the domain boundaries
   - Write 5-10 competency questions the ontology must answer
   - Example: "Which drugs interact with proteins encoded by a given gene?"

2. **Reuse assessment**
   - Search existing ontologies (BioPortal, LOV, OntoBee)
   - Import and align relevant upper ontologies (DOLCE, BFO, schema.org)
   - Document reuse decisions and mappings

3. **Conceptual modeling**
   - Identify entities (classes), relationships (properties), instances
   - Create class hierarchy (is-a relations)
   - Define object properties (relations between classes) and data properties (attributes)

4. **Formalization in OWL/RDF**
   - Encode in OWL 2 (DL, RL, or QL profile based on reasoning needs)
   - Add restrictions (cardinality, value constraints)
   - Define inverse, transitive, symmetric properties

5. **Validation & reasoning**
   - Check consistency with reasoner (HermiT, Pellet, FaCT++)
   - Verify competency questions with SPARQL
   - Review with domain experts

### 2. Knowledge Graph Construction

**Construction pipeline:**

1. **Source identification**
   - Structured: relational databases, APIs, CSV
   - Semi-structured: JSON, XML, logs
   - Unstructured: text, documents, images

2. **Schema/ontology alignment**
   - Map source schemas to ontology
   - Handle property mapping, unit conversion, URI generation

3. **Entity extraction & resolution**
   - Extract entities from unstructured sources (NER, RE)
   - Resolve duplicates: "IBM" = "International Business Machines" = "IBM Corp."
   - Link to external identifiers (Wikidata, DBpedia, ORCID)

4. **Graph population**
   - Transform to RDF triples or property graph format
   - Load into triple store or graph database
   - Validate graph completeness and quality

### 3. Querying & Retrieval

**Choose query language by store type:**

| Store Type | Query Language | Use Case |
|---|---|---|
| RDF triple store | SPARQL | Semantic web, OWL reasoning, linked data |
| Labeled property graph | Cypher | Neo4j, pattern matching, path queries |
| GraphQL | GraphQL+ | API-layer graph queries |
| Gremlin | Gremlin | Traversal-heavy, multi-model graphs |

### 4. Validation & Reasoning

**Reasoning tasks:**
- **Consistency checking**: No contradictory class assertions
- **Classification**: Infer subclass hierarchies
- **Property entailment**: Infer transitive, inverse, symmetric relations
- **Instance checking**: Validate type assertions

**Validation checklist:**
- [ ] Ontology is consistent (no unsatisfiable classes)
- [ ] All competency questions answerable with queries
- [ ] No orphan classes or properties
- [ ] URIs are dereferenceable or resolvable
- [ ] Labels and descriptions in multiple languages if needed
