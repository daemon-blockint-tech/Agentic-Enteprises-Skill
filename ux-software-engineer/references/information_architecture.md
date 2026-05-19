# Information Architecture in Product

## IA deliverables in engineering context

| Artifact | Use |
|----------|-----|
| Sitemap / nav tree | Routes, menus, breadcrumbs |
| Object taxonomy | Filters, categories, tags |
| Labeling system | Nav, headings, metadata |
| Cross-links | Related items, upsell, help |

## Navigation patterns

| Pattern | Good for | Watch |
|---------|----------|-------|
| Top nav | Few top-level areas | Mobile collapse |
| Sidebar | Many sections, app shell | Active state, scroll |
| Tabs | Peer views same object | Too many tabs |
| Wizard | Linear setup | Escape hatch |
| Hub | Dashboard landing | Overwhelming cards |

## Findability checklist

- Can user reach any primary task in ≤3 clicks from home?
- Search covers the objects users name in support tickets?
- Filters match how users describe segments (not only DB fields)?
- Breadcrumbs reflect hierarchy, not history stack only?
- Settings vs product features clearly separated?

## URL and routing UX

- Human-readable slugs where shareable
- Stable URLs for bookmarked admin views
- Redirect old paths after IA change
- 404 with recovery paths (search, home, support)

## Empty and overflow states

| State | UX requirement |
|-------|----------------|
| Zero data | Explain why + primary CTA to fix |
| Partial data | Show scope ("Last 30 days") |
| Too many results | Sort, filter, paginate with count |
| Permission denied | What they can do instead |

## IA change process

1. Inventory current routes and analytics top paths
2. Card sort or tree test if labels contested (`product-designer` may lead)
3. Map old → new URLs and comms for breaking changes
4. Ship with analytics on nav clicks and search queries
5. Review 2 weeks post-launch

## Handoff to engineering

Provide:

- Nav component spec (items, icons, badges, roles)
- Route table with auth requirements
- Redirect map
- Analytics event names for nav interactions
