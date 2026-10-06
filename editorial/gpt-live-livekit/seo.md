## SEO Validation Report: GPT-Live with LiveKit: Beyond the First Working Call

### Summary

- **Score:** 7/9 confirmed passes; 1 fix; 1 pending live validation.
- **Status:** NEEDS FIXES; source-level audit only, with external-link preflight pending.
- Scope: MDX draft and local Astro metadata/schema pathway. No external fetching or article edits.
- Exact title length: **52 characters**. Exact description length: **157 characters**.

### Detailed Results

| # | Check | Status | Details | Fix |
|---|---|---|---|---|
| 1 | Title Tag | PASS | Clear GPT-Live + LiveKit subject and application scope; 52 characters; no matching title among local blog posts. The layout uses this exact title. | None. |
| 2 | Meta Description | PASS | 157 characters; accurate and specific about prompts, changed requests, simulated bookings, and usage. Useful terms occur early. | None. |
| 3 | Heading Hierarchy | PASS | Layout supplies one H1; article has ten H2s and no skipped levels. Every H2 meets the user's 2–3-word requirement. | Preserve short headings during revisions. |
| 4 | Internal Links | FAIL | Two contextual links, both descriptive and locally resolvable, versus role target of 3–10 for a long post. They are distributed near beginning/end. Existing linked posts do not link back to this unpublished draft. | Add one useful link in Handling Interruptions to `/learn/components/turn-detection`, anchored as “turn-detection evaluation” or equivalent. Consider a backlink after publication when editorially useful, not as a release blocker. |
| 5 | External Links | PENDING | Eight source-link occurrences across six distinct URLs, all official OpenAI/LiveKit documentation. No sponsored links or explicit new-tab links require extra rel attributes. Source tiers pass; live validity is unverified. | Parent preflight Gate 5 must check URLs/fragments. Code and real-call evidence links are being added by parent; keep those pending. |
| 6 | Canonical URL | PASS | `getBlogPostSeo()` generates `https://mahimai.ca/blog/gpt-live-livekit-beyond-first-call`; Layout emits it. Absolute and no trailing slash, matching site convention. | Confirm rendered output after content sync/build. |
| 7 | OG Meta Tags | PASS | Shared Layout emits title, description, image, article type, URL, site name, image size/alt, and publication/modification dates. `socialImage` is a unique 1200×630 JPG. | None. A single accurate 157-character description is useful; no need to inflate to 2–4 sentences solely to satisfy a prose heuristic. |
| 8 | Twitter Card | PASS | `summary_large_image`, 52-character title, 157-character description, and same social image supplied. 1200×630 is a suitable common social-card ratio; exact 2:1 is not a material defect. | None. |
| 9 | URL Structure | PASS | Lowercase, hyphenated keyword-bearing filename, no dates or encoded characters. Seven tokens is longer than the role's ideal but readable and matches the topic. | No slug change needed. |

### Heading Tree

```text
H1 GPT-Live with LiveKit: Beyond the First Working Call [layout]
  H2 Changing Requests
  H2 How It Works
  H2 Separate Prompts
  H2 Context Controls
  H2 Running Tools
  H2 Handling Interruptions
  H2 Conversation Memory
  H2 API Surprises
  H2 Measuring Results
  H2 Real Conversation Tests
```

### Image Checks

All four referenced assets exist in the draft tree: 1672×941 WebP cover, 1200×630 JPG social image, architecture SVG, and correction SVG. Cover uses Astro Image with responsive widths and meaningful alt text. Both diagrams have descriptive alt, captions, lazy loading, and explicit imported dimensions. No missing-alt issue found. This audit checked image metadata/references rather than rendered visual quality. Parent should retain asset paths during sync and verify MDX/SVG imports through a build.

### Schema Pathway

`src/content.config.ts` accepts all frontmatter fields and resolves the image assets. `src/layouts/BlogPost.astro` passes title, description, dates, author, slug, and social image to `getBlogPostSeo()` in `src/server/seo.ts`. That function constructs a BlogPosting node with headline, description, author, publisher, image, publication/modification dates, and canonical mainEntityOfPage; it joins WebSite, Organization, Person, and available breadcrumb nodes. `src/layouts/Layout.astro:152` emits the JSON-LD script. Do not add duplicate article JSON-LD in MDX.

The draft currently lives outside the site's content collection and has `draft: true`. Production `src/pages/blog/[...slug].astro` excludes draft posts. This is expected staging behavior, not an SEO defect. The final publication step must sync the article/assets into the collection and deliberately release the draft before expecting a public indexed URL. No publish-state changes were made by this audit.

### Priority Fixes

1. Add the useful turn-detection internal link; this is the only present article-level SEO gap identified.
2. Complete the already-planned source-code and real-call evidence links so readers can reach the implementation and evidence behind exact version/test claims. Those additions are pending parent work, not presumed missing permanently.
3. Run external URL/fragment preflight and inspect built metadata/schema after syncing revised content. No broken URLs are asserted without live checks.

### Evidence Paths

- Draft: `/tmp/mahimai-blogs-gpt-live/posts/gpt-live-livekit-beyond-first-call.mdx`
- Site: `/Users/mahimai/code/year-2026/mahimai.ca/src/layouts/BlogPost.astro`
- Site: `/Users/mahimai/code/year-2026/mahimai.ca/src/layouts/Layout.astro`
- Site: `/Users/mahimai/code/year-2026/mahimai.ca/src/server/seo.ts`
- Site: `/Users/mahimai/code/year-2026/mahimai.ca/src/content.config.ts`
- Useful internal destination: `/Users/mahimai/code/year-2026/mahimai.ca/src/content/learn/turn-detection.mdx`
