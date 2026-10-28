# Gx_Rajput — Personal Portfolio

A responsive, static portfolio for **Noor Ul Hassan (Gx_Rajput)**, a graphic designer, video editor and web/app developer based in Layyah, Punjab, Pakistan.

- Live site: <https://rajputbrothers8184.github.io/Gx_Rajput/>
- Repository: <https://github.com/Rajputbrothers8184/Gx_Rajput>
- Built with HTML, CSS and vanilla JavaScript. There is no build step or application backend.

## What's included

- An editorial dark theme using the supplied palette: `#0B0B0D`, `#171719`, `#F5A623`, `#FFC247`, `#168BFF`, `#F5F5F5`, `#B8B8B8`, and `#34343A`.
- The supplied photos in the hero and About section. They are optimized/cropped copies of the supplied images; the face has not been AI-edited.
- **Seven portfolio concepts**, one each for Logo Design, Social Media, Thumbnails, Banners & Covers, Business Cards, Print & Packaging, and Web & App. Filters and a keyboard-accessible full-size viewer are included. Video editing is not a portfolio category; the existing video-editing skill and service remain available.
- About, skills, existing packages and rates, process, social/contact links, a downloadable vCard, and a form that opens a pre-filled WhatsApp message.
- Self-hosted Inter and Space Grotesk fonts, a responsive mobile menu, reduced-motion support, and social-sharing metadata.

> **Portfolio samples:** The seven new images are AI-generated concept previews, not client projects. They are labelled as concepts on the site. Replace them with your own work before presenting them as actual completed projects.

## Run locally

```bash
python3 -m http.server 8080
# Open http://localhost:8080
```

Run the dependency-free structural checks with:

```bash
python3 -m unittest discover -s tests
```

## Customize

| Change | Location |
|---|---|
| Text, experience, skills, rates, services and contacts | `index.html` |
| Palette and layout | CSS variables at the top of `css/style.css` |
| Filters, preview viewer and WhatsApp form | `js/main.js` |
| Hero and About photos | `assets/img/noor-portrait.webp`, `noor-about.webp`, `noor-studio.webp` |
| Social share image | `assets/img/noor-og.jpg` |
| Gallery images | `assets/img/work/selected-*.webp` |
| Downloadable contact | `assets/Gx_Rajput.vcf` |

For skill bars, update the visible percentage, the `data-w` value and the inline `--bar-width` value together (the inline value is a no-JavaScript fallback).

### Replace a gallery concept

1. Add your own image under `assets/img/work/`.
2. Find the matching `<article class="card" data-cat="…">` in `index.html`. Update the image path and alt text, the accessible button label, title, description, and concept label as appropriate.
3. Keep the filter's `data-f` value equal to the card's `data-cat` value. Update the gallery's counts if the number of samples changes.
4. Update or remove the AI-concept disclosure once the displayed images have been replaced.

The existing `tools/gen_sample_assets.py` and older images remain in the repository for reference; they are not used by the current gallery.

## Contact and deployment

The existing links use WhatsApp **+92 311 0682944**, email **n88908410@gmail.com**, Instagram **@noor_ul8184**, and the other social accounts listed in the page. Printing is on demand and charged separately. Review the displayed statistics, prices and availability before publishing.

GitHub Pages configuration is in `.github/workflows/pages.yml`. To enable deployment, choose **GitHub Actions** under the repository's **Settings → Pages → Build and deployment**. Merge changes into the deployment branch when ready to publish.

The bundled fonts are distributed under the SIL Open Font License; copies of their licenses are in `assets/fonts/`.
