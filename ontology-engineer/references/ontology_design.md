# Ontology Design

## Ontology Development Methodology

### 101 Methodology (Noy & McGuinness)

1. **Determine scope** — Competency questions
2. **Consider reuse** — Search existing ontologies
3. **Enumerate terms** — Brainstorm classes and properties
4. **Define classes** — Hierarchy, disjointness
5. **Define properties** — Domain, range, characteristics
6. **Define facets** — Cardinality, value types
7. **Create instances** — Populate with real data
8. **Check consistency** — Reasoner validation

### NeOn Methodology (Enterprise-focused)

- More elaborate, supports collaborative development
- Includes scenario-based requirements, modularization
- Recommended for large, distributed ontology projects

## Upper Ontologies (Foundational)

| Ontology | Focus | Use Case |
|---|---|---|
| BFO (Basic Formal Ontology) | Philosophy of reality | Biomedical ontologies (OBO) |
| DOLCE | Cognitive/linguistic | Natural language understanding |
| SUMO | General, comprehensive | Broad interoperability |
| schema.org | Web/markup | SEO, structured data |
| FOAF | People/social | Social web, identity |
| SKOS | Concepts/vocabularies | Taxonomies, thesauri |

**When to use upper ontologies:**
- Need cross-domain interoperability
- Complex reasoning over time, space, participation
- Academic or biomedical domains

**When to avoid:**
- Simple application ontologies
- Performance-critical scenarios
- Teams without ontology expertise

## Modeling Patterns

### Taxonomy Pattern
```turtle
ex:Animal a owl:Class .
ex:Mammal rdfs:subClassOf ex:Animal .
ex:Dog rdfs:subClassOf ex:Mammal .

ex:myDog a ex:Dog .
# Inferred: ex:myDog a ex:Mammal, ex:Animal
```

### Part-Whole Pattern (Mereology)
```turtle
ex:hasPart a owl:ObjectProperty, owl:TransitiveProperty ;
    rdfs:domain ex:Composite ;
    rdfs:range ex:Part .

ex:isPartOf owl:inverseOf ex:hasPart ;
    a owl:TransitiveProperty .
```

### Role Pattern
```turtle
# Roles as classes, not properties
ex:Employee a owl:Class ;
    owl:equivalentClass [
        a owl:Restriction ;
        owl:onProperty ex:employedBy ;
        owl:someValuesFrom ex:Organization
    ] .

# A person plays a role
ex:playsRole a owl:ObjectProperty ;
    rdfs:domain ex:Person ;
    rdfs:range ex:Role .
```

### N-ary Relations Pattern
```turtle
# Reify the relation as a class
ex:Employment a owl:Class ;
    rdfs:subClassOf [
        a owl:Restriction ; owl:onProperty ex:employee ; owl:cardinality 1 ;
        owl:Restriction ; owl:onProperty ex:employer ; owl:cardinality 1 ;
        owl:Restriction ; owl:onProperty ex:startDate ; owl:cardinality 1
    ] .
```

### Time & Change Pattern
```turtle
# Time-indexed statements (4D fluent)
ex:hasWeight a owl:ObjectProperty ;
    rdfs:range ex:WeightMeasurement .

ex:WeightMeasurement a owl:Class ;
    rdfs:subClassOf [
        owl:Restriction ; owl:onProperty ex:value ; owl:cardinality 1 ;
        owl:Restriction ; owl:onProperty ex:atTime ; owl:cardinality 1
    ] .
```

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| Class as property value | `ex:hasColor ex:Red` where Red is instance | Use datatype or defined class |
| Over-specification | Model every detail | Focus on competency questions |
| Class for instance | `ex:ToyotaCar` vs `ex:Car` | Instances belong to class, not be classes |
| Properties vs classes | `ex:isRed` property vs `ex:RedThing` class | Prefer properties for transient characteristics |
| Orphan classes | No properties or relations defined | Add outgoing/incoming edges |
| Circular definitions | A defined by B, B defined by A | Break cycle with primitive assertions |

## Reasoning & Inference

### OWL Reasoning Tasks

| Task | Description | Tool |
|---|---|---|
| Consistency | Is the ontology free of contradictions? | HermiT, Pellet, FaCT++ |
| Satisfiability | Can a class have any instances? | Same as above |
| Subsumption | Is A a subclass of B? | Same as above |
| Classification | Compute complete class hierarchy | Same as above |
| Instance retrieval | Find all instances of a class | SPARQL + inference |
| Realization | Find most specific class for instance | Same as above |

### Rule-Based Reasoning (OWL 2 RL / SWRL)

```turtle
# SWRL rule
ex:hasParent(?x, ?y) ^ ex:hasBrother(?y, ?z) -> ex:hasUncle(?x, ?z)
```

### Materialization vs Query-Time Reasoning

| Approach | Pros | Cons |
|---|---|---|
| Materialization | Fast queries | Stale data, storage overhead |
| Query-time | Always current | Slower, complex configuration |
| Hybrid | Balance | Requires careful design |

## Modularization

### Import Strategy
```turtle
@prefix ont: <http://example.org/ontology/> .

<http://example.org/my-domain> a owl:Ontology ;
    owl:imports <http://example.org/upper-ontology> ;
    owl:imports <http://example.org/shared-vocabulary> .
```

### Module Extraction
- **Star module**: All axioms mentioning signature entities
- **Bottom module**: All consequences for a set of classes
- **Top module**: All axioms that can affect a set of classes

**Use case:** Extract a small, self-contained module for mobile or edge deployment.

## Versioning & Evolution

### Best Practices
- Use versioned URIs: `http://example.org/ontology/1.2/`
- Maintain backward compatibility when possible
- Document breaking changes
- Provide migration mappings (ontology alignment)

### Change Types

| Change | Backward Compatible? | Example |
|---|---|---|
| Add class/property | Yes | Add `ex:Contractor` |
| Add subclass | Yes | `ex:Contractor ⊂ ex:Employee` |
| Remove class | No | Delete `ex:Intern` |
| Make class disjoint | No | `ex:Employee` disjoint `ex:Vendor` |
| Narrow property range | No | `ex:worksAt` range from `Thing` to `Organization` |

### Ontology Alignment
```turtle
# Map two ontologies
ex1:Employee owl:equivalentClass ex2:Worker .
ex1:worksAt owl:equivalentProperty ex2:employedBy .
```
