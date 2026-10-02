# Cover prompt: WebRTC, on one page

Generate two files to match the series: a transparent watercolour WebP hero
(`posts/images/webrtc-one-pager/webrtc-one-pager-cover.webp`, about 1672 px wide) and a
1200 × 630 social JPEG (`webrtc-one-pager-social.jpg`).

Prompt:

> Loose watercolour illustration on a transparent background, lavender and charcoal
> palette with soft paper texture and bleeding edges, matching an editorial engineering
> blog. Two laptops on opposite sides of the frame, each with a person mid-conversation.
> Between them, a single flowing path of small envelope-like packets, drawn as one calm
> line, passes through four quiet waypoints shown only as simple shapes: a folded note
> (an offer and answer), a small lighthouse on a hill (a server telling each side its
> public address), a closed padlock, and a gentle wave of packets arriving at the far
> laptop. No text, no logos, no labels, no numbers. Calm, uncluttered, wide composition
> with generous empty space on the left for a title overlay.

Alt text: Two people talk across laptops while a single line of packets passes a note,
a lighthouse and a padlock on its way between them.

Once generated, add to the post frontmatter:

```yaml
cover: ./images/webrtc-one-pager/webrtc-one-pager-cover.webp
coverAlt: Two people talk across laptops while a single line of packets passes a note, a lighthouse and a padlock on its way between them.
socialImage: ./images/webrtc-one-pager/webrtc-one-pager-social.jpg
```
