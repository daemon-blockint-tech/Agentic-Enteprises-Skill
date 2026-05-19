# Semantic Web Standards

## RDF (Resource Description Framework)

### Core Model: Triples
```
Subject — Predicate — Object
```

**Example (Turtle syntax):**
```turtle
@prefix ex: <http://example.org/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .

ex:Alice a foaf:Person ;
    foaf:name "Alice Smith" ;
    foaf:age 30 ;
    ex:worksAt ex:ExampleCorp .

ex:ExampleCorp a ex:Organization ;
    ex:name "Example Corporation" ;
    ex:location "New York" .
```

### Serialization Formats

| Format | Readable | Compact | Use Case |
|---|---|---|---|
| Turtle (.ttl) | Yes | Medium | Human editing, development |
| N-Triples (.nt) | Somewhat | No | Streaming, line-based processing |
| RDF/XML (.rdf) | No | No | Legacy, XML ecosystems |
| JSON-LD (.jsonld) | Yes | Yes | Web APIs, JavaScript apps |
| TriG | Yes | Medium | Named graphs |

## RDFS (RDF Schema)

### Core Constructs

```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex:Person a rdfs:Class ;
    rdfs:label "Person" ;
    rdfs:comment "A human being" .

ex:Employee rdfs:subClassOf ex:Person .

ex:worksAt a rdf:Property ;
    rdfs:domain ex:Person ;
    rdfs:range ex:Organization .
```

**RDFS inference rules:**
- Subclass transitivity: `A ⊂ B`, `B ⊂ C` → `A ⊂ C`
- Domain/range: If `ex:worksAt rdfs:domain ex:Person`, then `?x ex:worksAt ?y` → `?x a ex:Person`

## OWL (Web Ontology Language)

### OWL 2 Profiles

| Profile | Expressivity | Reasoning | Best For |
|---|---|---|---|
| OWL 2 DL | High | Complete (but slow) | Complex domain modeling |
| OWL 2 EL | Polynomial | Fast | Large biomedical ontologies (SNOMED CT) |
| OWL 2 QL | Query rewriting | Fast | Integration with relational DBs |
| OWL 2 RL | Rule-based | Fast | Scalable reasoning, streaming |

### Common OWL Constructs

```turtle
@prefix owl: <http://www.w3.org/2002/07/owl#> .

# Class equivalence
ex:Employee owl:equivalentClass [
    a owl:Restriction ;
    owl:onProperty ex:worksAt ;
    owl:someValuesFrom ex:Organization
] .

# Property characteristics
ex:hasPart a owl:ObjectProperty ;
    a owl:TransitiveProperty .

ex:isPartOf owl:inverseOf ex:hasPart .

ex:marriedTo a owl:SymmetricProperty .

# Disjoint classes
ex:Man owl:disjointWith ex:Woman .

# Cardinality restrictions
ex:Parent a owl:Restriction ;
    owl:onProperty ex:hasChild ;
    owl:minQualifiedCardinality "1"^^xsd:nonNegativeInteger ;
    owl:onClass ex:Person .

# Datatype restrictions
ex:Adult a owl:Restriction ;
    owl:onProperty ex:age ;
    owl:someValuesFrom [
        a rdfs:Datatype ;
        owl:onDatatype xsd:integer ;
        owl:withRestrictions (
            [xsd:minExclusive 17]
        )
    ] .
```

## SPARQL Query Language

### Basic Patterns

```sparql
# Select all employees and their companies
SELECT ?person ?company
WHERE {
  ?person a ex:Employee .
  ?person ex:worksAt ?company .
}

# With FILTER and OPTIONAL
SELECT ?person ?name ?age
WHERE {
  ?person a ex:Person ;
          ex:name ?name .
  OPTIONAL { ?person ex:age ?age }
  FILTER (strstarts(?name, "A"))
}
```

### Advanced Patterns

```sparql
# Property paths: find all ancestors
SELECT ?ancestor
WHERE {
  ex:Alice ex:hasParent+ ?ancestor .
}

# Aggregation
SELECT ?company (COUNT(?employee) AS ?count)
WHERE {
  ?employee ex:worksAt ?company .
}
GROUP BY ?company
HAVING (?count > 10)

# Subqueries
SELECT ?person ?avgSalary
WHERE {
  {
    SELECT ?person (AVG(?salary) AS ?avgSalary)
    WHERE { ?person ex:hasSalary ?salary }
    GROUP BY ?person
  }
  FILTER (?avgSalary > 50000)
}

# Federated query (query remote endpoint)
SELECT ?drug ?condition
WHERE {
  SERVICE <http://dbpedia.org/sparql> {
    ?drug a dbo:Drug .
    ?drug dbo:indication ?condition .
  }
}
```

### SPARQL Update

```sparql
# Insert data
INSERT DATA {
  ex:Bob a ex:Employee ;
         ex:name "Bob Jones" ;
         ex:worksAt ex:ExampleCorp .
}

# Delete + insert (transactional)
DELETE { ex:Alice ex:age 30 }
INSERT { ex:Alice ex:age 31 }
WHERE { ex:Alice ex:age 30 }
```

## Linked Data Principles

1. Use URIs as names for things
2. Use HTTP URIs so people can look them up
3. Provide useful information using standards (RDF, SPARQL)
4. Include links to other URIs to discover more

**URI design best practices:**
- Persistent: don't change when content changes
- Dereferenceable: `curl http://example.org/Alice` returns RDF
- Human-readable: `http://example.org/person/Alice` not `http://example.org/id/12345`
- Content negotiation: serve HTML to browsers, RDF to agents

## SHACL (Shapes Constraint Language)

```turtle
@prefix sh: <http://www.w3.org/ns/shacl#> .

ex:PersonShape a sh:NodeShape ;
    sh:targetClass ex:Person ;
    sh:property [
        sh:path ex:name ;
        sh:datatype xsd:string ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] ;
    sh:property [
        sh:path ex:age ;
        sh:datatype xsd:integer ;
        sh:minInclusive 0 ;
        sh:maxInclusive 150 ;
    ] ;
    sh:property [
        sh:path ex:worksAt ;
        sh:class ex:Organization ;
        sh:minCount 0 ;
    ] .
```
