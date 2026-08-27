# mahimai.blogs

Source of truth for the [mahimai.ca](https://mahimai.ca) blog. This repo holds
**only** blog content, so access can be granted to writers without exposing the
site's source code.

```
posts/*.mdx          one file per post (filename = slug = URL segment)
posts/covers/*       cover images referenced from post frontmatter as ./covers/<file>
```

## How it reaches the site

`mahimai.ca` does not store these posts. At build time it fetches `posts/` from
this repo into its blog content collection (`scripts/sync-blog.ts`). A push to
`main` here triggers a `mahimai.ca` rebuild via a Cloudflare deploy hook
(`.github/workflows/deploy-site.yml`), so a merged post publishes automatically.

## Editing

Writers edit through the CMS at the `mahimai-admin` app (`/keystatic`), which is
configured to read and write this repo. A writer with read-only access here saves
via pull requests that a maintainer merges. Direct commits to `main` publish live.

## Post frontmatter

```yaml
title: string            # required
description: string      # required
pubDate: YYYY-MM-DD       # required
updatedDate: YYYY-MM-DD   # optional
author: string           # defaults to "Mahimai Raja J"
tags: [string]            # optional
draft: boolean            # optional, default false; drafts are not published
cover: ./covers/file.jpg  # optional
coverAlt: string          # optional
```
