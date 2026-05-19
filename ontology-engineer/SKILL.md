---
name: ontology-engineer
description: |
  Guides ontology engineering and knowledge graph construction using semantic web standards
  and enterprise graph technologies. Covers OWL, RDF, RDFS, SPARQL, linked data, graph databases
  (Neo4j, Amazon Neptune), entity resolution, taxonomy construction, and reasoning.
  Use when designing ontologies, building knowledge graphs, modeling domain knowledge,
  writing SPARQL/Cypher queries, or implementing semantic web and enterprise data integration.
---

# Ontology Engineer

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

**See `references/ontology_design.md` for modeling patterns, anti-patterns, and reuse strategies.**

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

**See `references/knowledge_graphs.md` for extraction pipelines, resolution techniques, and graph database patterns.**

### 3. Querying & Retrieval

**Choose query language by store type:**

| Store Type | Query Language | Use Case |
|---|---|---|
| RDF triple store | SPARQL | Semantic web, OWL reasoning, linked data |
| Labeled property graph | Cypher | Neo4j, pattern matching, path queries |
| GraphQL | GraphQL+ | API-layer graph queries |
| Gremlin | Gremlin | Traversal-heavy, multi-model graphs |

**See `references/semantic_web.md` for SPARQL patterns and `references/knowledge_graphs.md` for Cypher patterns.**

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

**See `references/ontology_design.md` for reasoning profiles and validation frameworks.**

## When to Load References

- **Semantic web standards** → `references/semantic_web.md`
- **Knowledge graphs** → `references/knowledge_graphs.md`
- **Ontology design patterns** → `references/ontology_design.md`
- **Tools & frameworks** → `references/tools_frameworks.md`
