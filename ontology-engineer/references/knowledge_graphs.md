# Knowledge Graphs

## Property Graph vs RDF Triple Store

| Aspect | Property Graph (Neo4j) | RDF Triple Store |
|---|---|---|
| **Model** | Nodes + Relationships with properties | Subject-Predicate-Object triples |
| **Schema** | Flexible, optional | OWL/RDFS formal schema |
| **Query** | Cypher | SPARQL |
| **Reasoning** | Limited (APOC) | Full OWL reasoning |
| **Use case** | Recommendations, fraud detection | Semantic integration, linked data |

## Graph Database Patterns

### Neo4j / Cypher

**Node and relationship creation:**
```cypher
CREATE (a:Person {name: 'Alice', age: 30})
CREATE (b:Company {name: 'TechCorp'})
CREATE (a)-[:WORKS_AT {since: 2020}]->(b)
```

**Pattern matching:**
```cypher
// Find Alice's colleagues
MATCH (alice:Person {name: 'Alice'})-[:WORKS_AT]->(company:Company)<-[:WORKS_AT]-(colleague:Person)
RETURN colleague.name

// Shortest path between two people
MATCH path = shortestPath(
  (a:Person {name: 'Alice'})-[:KNOWS|WORKS_AT*]-(b:Person {name: 'Bob'})
)
RETURN path

// Recommendation: people who work at similar companies
MATCH (person:Person)-[:WORKS_AT]->(company:Company)-[:IN_INDUSTRY]->(industry:Industry)
WITH person, industry, count(company) AS companyCount
ORDER BY companyCount DESC
RETURN person.name, industry.name, companyCount
```

**Aggregation and analytics:**
```cypher
// PageRank for influence scoring
CALL gds.pageRank.stream('myGraph')
YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS name, score
ORDER BY score DESC

// Community detection (Louvain)
CALL gds.louvain.stream('myGraph')
YIELD nodeId, communityId
RETURN communityId, count(*) AS communitySize
ORDER BY communitySize DESC
```

### Amazon Neptune

**Supports both RDF/SPARQL and property graph/Gremlin:**
```java
// Gremlin example
g.V().hasLabel('Person').has('name', 'Alice')
  .out('WORKS_AT').values('name')
```

## Entity Resolution

### Resolution Pipeline

1. **Blocking**: Candidate pairs (same name, same location)
2. **Comparison**: Similarity features (Jaro-Winkler, cosine, embedding)
3. **Classification**: Match / non-match / uncertain
4. **Clustering**: Transitive closure to form canonical entities

### Techniques

| Technique | When | Example |
|---|---|---|
| Rule-based | High precision, known patterns | Same email → same person |
| Probabilistic | Medium data, explainable | Fellegi-Sunter record linkage |
| ML-based | Large data, complex features | Siamese networks, ER models |
| Embedding-based | Text-heavy, semantic matching | Entity embeddings, sentence transformers |

**Python example (dedupe.io):**
```python
import dedupe

fields = [
    {'field': 'name', 'type': 'String'},
    {'field': 'address', 'type': 'String'},
    {'field': 'phone', 'type': 'Exact'}
]

deduper = dedupe.Dedupe(fields)
deduper.prepare_training(data)
deduper.train()

clusters = deduper.partition(data, threshold=0.5)
```

## Taxonomy Construction

### Manual Approach
1. Extract candidate terms from corpus
2. Group into broader-narrower hierarchies
3. Define relationships (is-a, part-of, related-to)
4. Validate with domain experts
5. Publish in SKOS

### Automated Approach
```python
# Using text mining + embeddings
from sklearn.cluster import AgglomerativeClustering

# Embed terms, cluster hierarchically
clusters = AgglomerativeClustering(n_clusters=None, distance_threshold=0.5)
clusters.fit(term_embeddings)
```

### SKOS Representation
```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ex:industries a skos:ConceptScheme ;
    skos:prefLabel "Industries" .

ex:technology a skos:Concept ;
    skos:prefLabel "Technology" ;
    skos:broader ex:industries ;
    skos:narrower ex:software, ex:hardware ;
    skos:related ex:telecommunications .

ex:software a skos:Concept ;
    skos:prefLabel "Software" ;
    skos:broader ex:technology .
```

## Knowledge Extraction from Text

### Pipeline

```
Raw Text → Preprocessing → NER → Relation Extraction → Entity Linking → Graph Population
```

### Tools

| Task | Tools |
|---|---|
| NER | spaCy, Stanza, Flair, BERT-based ( transformers) |
| Relation Extraction | OpenIE, REBEL, spaCy-RE |
| Entity Linking | DBpedia Spotlight, Wikifier, BLINK |
| Coreference | CoreNLP, huggingface models |

**spaCy example:**
```python
import spacy
nlp = spacy.load("en_core_web_trf")

doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for ent in doc.ents:
    print(ent.text, ent.label_)  # Apple ORG, U.K. GPE, $1 billion MONEY
```

## Graph Embeddings

### Techniques

| Method | Approach | Best For |
|---|---|---|
| TransE | Translation-based | Simple relations |
| DistMult | Bilinear interactions | Dense multi-relational |
| ComplEx | Complex-valued | Asymmetric relations |
| RotatE | Rotation in complex space | Hierarchical patterns |
| Node2Vec | Random walks | Homophily + structural equivalence |

**Application:**
- Link prediction: `?company ex:acquired ex:Startup`
- Entity classification: Predict node type from neighbors
- Similarity: Find similar entities in embedding space

## Graph Quality Metrics

| Metric | Definition | Target |
|---|---|---|
| Coverage | % of real-world entities represented | >90% for core domains |
| Accuracy | % of triples that are factually correct | >99% for critical paths |
| Completeness | % of expected properties populated | >80% |
| Consistency | No contradictory assertions | Zero tolerance |
| Timeliness | Staleness of data | Hours for real-time, weeks for static |
| Connectivity | % of entities connected to main graph | >95% |
