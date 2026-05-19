# Tools & Frameworks

## Ontology Editors

| Tool | Best For | Key Features |
|---|---|---|
| Protege | Development, OWL editing | Reasoner integration, visualization, plugins |
| TopBraid Composer | Enterprise, SHACL | GraphQL generation, EDG platform |
| WebProtégé | Collaboration, review | Web-based, comments, change tracking |
| OntoWiki | Lightweight, publishing | Semantic wiki, faceted browsing |

## Triple Stores / RDF Databases

| Store | License | Scaling | Reasoning | Best For |
|---|---|---|---|---|
| Apache Jena | Open source | Medium | Yes (OWL, rules) | Research, Java stack |
| GraphDB (Ontotext) | Commercial/Free | High | Yes (OWL, SHACL) | Enterprise, knowledge graphs |
| Virtuoso | Open/Commercial | High | Limited | Linked data, SPARQL endpoint |
| Stardog | Commercial | High | Yes (OWL, rules, ML) | Enterprise, data virtualization |
| Amazon Neptune | Cloud | Auto | Limited | AWS-native graphs |
| AllegroGraph | Commercial | High | Yes | Lisp/CL stack, geospatial |
| Blazegraph | Open source | Medium | Limited | Wikidata, research |

## Graph Databases (Property Graph)

| Database | Query | Ecosystem | Best For |
|---|---|---|---|
| Neo4j | Cypher | Mature, Graph Data Science | Recommendations, fraud |
| Amazon Neptune | Gremlin, SPARQL | AWS integration | Multi-model, cloud |
| ArangoDB | AQL | Multi-model | Documents + graph |
| JanusGraph | Gremlin | Open, pluggable | Large-scale, distributed |
| TigerGraph | GSQL | Analytics | Real-time analytics |

## Programming Frameworks

### Python

| Library | Purpose |
|---|---|
| rdflib | RDF parsing, serialization, SPARQL |
| owlready2 | OWL reasoning, ontology manipulation |
| pyshacl | SHACL validation |
| SPARQLWrapper | Remote SPARQL endpoint queries |
| networkx | General graph algorithms |
| neo4j-python-driver | Neo4j connectivity |

```python
# rdflib example
from rdflib import Graph, Namespace, RDF, RDFS, OWL

g = Graph()
ns = Namespace("http://example.org/")

g.add((ns.Person, RDF.type, OWL.Class))
g.add((ns.Employee, RDFS.subClassOf, ns.Person))

# Parse from file
g.parse("ontology.ttl", format="turtle")

# Query
results = g.query("""
    SELECT ?class WHERE { ?class rdfs:subClassOf* ns:Person }
""")
```

### Java

| Library | Purpose |
|---|---|
| Apache Jena | Full RDF/OWL stack |
| OWL API | OWL ontology manipulation |
| RDF4J (Eclipse) | Storage, SPARQL, reasoning |

## Linked Data Platforms

| Platform | Features |
|---|---|
| LOD Cloud | Linked open data catalog |
| DBpedia | Structured Wikipedia |
| Wikidata | Collaborative knowledge base |
| YAGO | Wikipedia + WordNet + GeoNames |
| BabelNet | Multilingual encyclopedic dictionary |
| BioPortal | Biomedical ontologies repository |

## NLP for Knowledge Extraction

| Tool | Task | Model |
|---|---|---|
| spaCy | NER, parsing | en_core_web_trf (transformer) |
| Stanza | Multilingual NLP | BiLSTM + transformers |
| Hugging Face | General NLP | BERT, RoBERTa, custom |
| REBEL | Relation extraction | BART-based |
| OpenIE (Stanford) | Open relation extraction | Rule + ML hybrid |
| DBpedia Spotlight | Entity linking | TF-IDF + context |

## Visualization Tools

| Tool | Graph Type | Interaction |
|---|---|---|
| WebVOWL | OWL ontologies | Web, export SVG |
| Cytoscape | General graphs | Desktop, highly customizable |
| D3.js | Custom | Web, code-based |
| yFiles | Enterprise graphs | Commercial, layout algorithms |
| Graphviz | Static diagrams | DOT language |
| Gephi | Large networks | Desktop, community detection |

## Validation Tools

| Tool | Checks |
|---|---|
| OOPS! (OntOlogy Pitfall Scanner) | 21 common pitfalls |
| RDF Validator (W3C) | Syntax compliance |
| Protege Reasoner | Consistency, classification |
| SHACL Play | SHACL shape validation |
| VoID (Vocabulary of Interlinked Datasets) | Dataset metadata |

## Testing Ontologies

### Unit Tests for Ontologies
```python
import unittest
from owlready2 import *

class TestOntology(unittest.TestCase):
    def setUp(self):
        self.onto = get_ontology("file://ontology.owl").load()

    def test_consistency(self):
        # All classes should be satisfiable
        with self.onto:
            sync_reasoner()
        # If unsatisfiable classes exist, test fails
        unsatisfiable = [c for c in self.onto.classes() if not c.instances()]
        # Additional logic to check reasoner output
```

### Competency Question Tests
```sparql
# Encode competency question as ASK/SELECT test
ASK {
  ?drug a ex:Drug .
  ?drug ex:interactsWith ?protein .
  ?protein ex:encodedBy ?gene .
  FILTER (?gene = ex:BRCA1)
}
# Expected: true (if data supports)
```

## Cloud Services

| Service | Provider | Offering |
|---|---|---|
| Amazon Neptune | AWS | Managed graph (RDF + property) |
| Azure Cosmos DB | Microsoft | Gremlin API |
| Google Cloud | GCP | Neo4j on marketplace, custom |
| Ontotext Platform | Ontotext | GraphDB as a service |
| Stardog Cloud | Stardog | Managed knowledge graph |
