# Article artwork

AI-generated raster illustration, created for this article with OpenAI image generation.
The original PNG is retained beside this file; optimized WebP and social JPG live in posts/covers.

Creative brief: warm off-white paper, graphite and violet watercolor; a visitor with
headphones and laptop faces two opposing audio ribbons. A microphone represents the
voice frontend, a small tool workstation represents delegated work, and a calendar
with a check represents the guarded simulated outcome. No provider logos, invented
dashboard text, or photorealistic robot. This illustration is conceptual, not a
screenshot of the running agent. The brief is a summary, not an exact prompt log.

The architecture and correction diagrams are authored in reladraw. Their editable
sources are stored here and the SVG exports live in posts/figures/gpt-live. They
describe control flow rather than measured timing. Rendered diagrams were inspected
for text overlap, clipping, and flow direction.

## Transparent revision — October 6, 2026

Built-in OpenAI image generation edited the original illustration, preserving the visitor, laptop, purple conversational waves, microphone, tools and calendar. Prompt: “Edit this blog illustration into a genuine transparent watercolor cutout. Preserve the woman, laptop, conversational purple waves, microphone, tool objects and calendar as a coherent wide composition. Remove the beige paper background completely, including empty space above and between objects. No rectangular backdrop, no checkerboard painted into image. Organic watercolor edges and isolated subtle washes immediately around objects only, fading to actual alpha. Clear charcoal outlines and lavender accents readable on both near-white and near-black webpage backgrounds. Keep original editorial watercolor and pencil detail; no words, no logos. All important objects fully visible with comfortable transparent margin. Wide approximately 2:1 composition.”

The WebP retains alpha; the social JPEG is flattened on the site's light background. Reladraw sources now include icons and semantic theme colors. The site inlines the SVGs through ReladrawFigure, maps the renderer palette to site tokens, and selects a narrow layout below 600px. No animation or client JavaScript is needed.
